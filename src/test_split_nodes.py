import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_normal(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        input = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(input, expected_nodes)

    def test_unmatched_delimiter(self):
        node = TextNode("This is text with a `broken code block", TextType.TEXT)
        with self.assertRaises(ValueError) as context: 
            split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(str(context.exception), f"Unmatched delimiter ` in text: {node.text}")

    def test_multi_delimiter(self):
        node = TextNode("This is text with one `code block` and another `code block`", TextType.TEXT)
        expected_nodes = [
            TextNode("This is text with one ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and another ", TextType.TEXT),
            TextNode("code block", TextType.CODE)
        ]
        
        result = split_nodes_delimiter([node], "`", TextType.CODE)  # Only using backticks
        self.assertEqual(result, expected_nodes)





if __name__ == "__main__":
    unittest.main()

