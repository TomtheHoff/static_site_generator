import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_link, split_nodes_image

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

class TestSplitNodesLink(unittest.TestCase):
    def test_normal(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        
        expected_nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]

        result = split_nodes_link([node])
        
        self.assertEqual(result, expected_nodes)

class TestSplitNodesImage(unittest.TestCase):
    def test_normal(self):
        node = TextNode(
            "This is text with an image ![alt text](https://www.example.com/image.png) and another ![another alt](https://www.example.com/another.png)",
            TextType.TEXT,
        )
        
        expected_nodes = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("alt text", TextType.LINK, "https://www.example.com/image.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("another alt", TextType.LINK, "https://www.example.com/another.png"),
        ]

        result = split_nodes_image([node])
        
        #print(f"Expected: {expected_nodes}")
        #print(f"Actual: {result}")
        
        self.assertEqual(result, expected_nodes)

    def test_no_image(self):
        node = TextNode(
            "This is text without any images.",
            TextType.TEXT,
        )
        
        expected_nodes = [
            TextNode("This is text without any images.", TextType.TEXT),
        ]

        result = split_nodes_image([node])
        
        #print(f"Expected: {expected_nodes}")
        #print(f"Actual: {result}")
        
        self.assertEqual(result, expected_nodes)

if __name__ == "__main__":
    unittest.main()

