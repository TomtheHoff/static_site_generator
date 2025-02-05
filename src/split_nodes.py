
from textnode import TextType



#noch komplett anpassen! habe vorerst nur kopiert was als assignement war
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)



