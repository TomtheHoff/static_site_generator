# test_text_to_html.py
import unittest
from textnode import TextNode, TextType
from htmlnode import LeafNode
from text_to_html import text_node_to_html_node

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_invalid_texttype(self):
        node = TextNode("some text", None)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)
    
    def test_bold_texttype(self):
        text_node = TextNode("this is a test", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "this is a test")

    def test_italic_texttype(self):
        text_node = TextNode("this is a test", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "this is a test")


if __name__ == "__main__":
    unittest.main()