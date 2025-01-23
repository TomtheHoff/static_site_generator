import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_none(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_single(self):
        node = HTMLNode(props= {"href": "https://www.google.com"})
        node2 = ' href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), node2)

    def test_props_multi(self):
        node = HTMLNode(props= {"href": "https://www.google.com", "target": "_blank"})
        node2 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), node2)    

     
class TestLeafNode(unittest.TestCase):

    def test_props_none(self):
        node = LeafNode(tag = "p", value = "This is a paragraph of text.", props=None)
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>") 

    def test_tag_none(self):
        node = LeafNode(tag = None, value = "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "This is a paragraph of text.") 

    def test_raise_error(self):
        node = LeafNode(value=None)
        with self.assertRaises(ValueError):
            node.to_html()            

    def test_with_link(self):
        node = LeafNode(tag = "a", value = "Click me!", props = {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()