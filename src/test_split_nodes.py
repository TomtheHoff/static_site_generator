import unittest
from textnode import TextType


class split_nodes_delimiter(unittest.TestCase):
    def test_normal(self):




'''
input:
node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

Output:
[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
]

'''







if __name__ == "__main__":
    unittest.main()