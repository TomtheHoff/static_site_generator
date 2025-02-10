

from textnode import TextNode, TextType



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # If it's not plain text, just add it as-is
            new_nodes.append(node)
            continue  # Skip the rest of the loop for this node
        
        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            # If there's an **uneven** number of parts, we are missing a closing delimiter
            raise ValueError(f"Unmatched delimiter {delimiter} in text: {node.text}")

        # Go through the parts and alternate between TEXT and the given text_type
        for i in range(len(parts)):
            if parts[i]:  # Only add non-empty parts
                new_text_type = text_type if i % 2 == 1 else TextType.TEXT
                new_nodes.append(TextNode(parts[i], new_text_type))


    return new_nodes


def split_nodes_image(old_nodes):
    pass




def split_nodes_link(old_nodes):
    pass


'''

node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]


'''