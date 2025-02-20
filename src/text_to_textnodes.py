from split_nodes import *
from textnode import TextNode, TextType


def text_to_textnodes(text):
    textnode=[]
    textnode.append(TextNode(text, TextType.TEXT, None))
    #print(f"\033[93m{textnode=}\033[0m")
    textnode = split_nodes_image(textnode)
    #print(f"\033[93m{textnode=}\033[0m")
    textnode = split_nodes_link(textnode)
    #print(f"\033[93m{textnode=}\033[0m")
    textnode = split_nodes_delimiter(textnode, "**", TextType.BOLD)
    #print(f"\033[93m{textnode=}\033[0m")
    textnode = split_nodes_delimiter(textnode, "*", TextType.ITALIC)
    #print(f"\033[93m{textnode=}\033[0m")
    textnode = split_nodes_delimiter(textnode, "`", TextType.CODE)
    #print(f"\033[93m{textnode=}\033[0m")
    return textnode




text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
text_to_textnodes(text)