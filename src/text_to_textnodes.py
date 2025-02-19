from split_nodes import split_nodes_link, split_nodes_image
from textnode import TextNode, TextType


def text_to_textnodes(text):
    textnode = ()
    textnode += text, TextType.TEXT
    print(f"\033[93m{textnode=}\033[0m")


text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
text_to_textnodes(text)