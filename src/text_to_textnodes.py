from split_nodes import *
from textnode import TextNode, TextType
from custom_print import *


def text_to_textnodes(text):
    textnode=[]
    textnode.append(TextNode(text, TextType.TEXT, None))
    print_red(textnode)
    textnode = split_nodes_image(textnode)
    print_green(textnode)
    textnode = split_nodes_link(textnode)
    #print_yellow(textnode)
    textnode = split_nodes_delimiter(textnode, "**", TextType.BOLD)
    #print_blue(textnode)
    textnode = split_nodes_delimiter(textnode, "*", TextType.ITALIC)
    #print_cyan(textnode)
    textnode = split_nodes_delimiter(textnode, "`", TextType.CODE)
    #print_violett(textnode)
    return textnode




#text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
#print_blue(text_to_textnodes(text))