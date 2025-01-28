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

if __name__ == "__main__":
    unittest.main()