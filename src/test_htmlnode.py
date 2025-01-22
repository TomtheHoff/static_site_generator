import unittest

from htmlnode import HTMLNode

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

     




if __name__ == "__main__":
    unittest.main()