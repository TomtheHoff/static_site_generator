from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node == TextType.TEXT:
        return LeafNode(None, text_node, None, None)
         #This should become a LeafNode with no tag, just a raw text value.
    if text_node == TextType.BOLD:
        return LeafNode ("b", text_node, None ,None) #This should become a LeafNode with a "b" tag and the text
    if text_node == TextType.ITALIC: 
        return LeafNode ("i", text_node, None, None) #"i" tag, text
    if text_node == TextType.CODE:
        return LeafNode ("code", text_node, None, None) #"code" tag, text
    if text_node == TextType.LINK:
        return LeafNode ("a", text_node, None, TextNode(text_node) ) #"a" tag, anchor text, and "href" prop
    if text_node == TextType.IMAGE:
        return LeafNode ("img", "", None, TextNode(scr, alt)) #"img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
    else:
        raise Exception