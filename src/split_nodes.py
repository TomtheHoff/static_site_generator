import re
from textnode import TextNode, TextType
from regex_extract import extract_markdown_images, extract_markdown_links




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
'''
node = TextNode("This is text with one `code block` and another `code block`", TextType.TEXT)
result = split_nodes_delimiter([node], "`", TextType.CODE)
#output = [TextNode("This is text with one ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" and another ", TextType.TEXT), TextNode("code block", TextType.CODE)]
print(f"\033[93m{result=}\033[0m")
'''




def split_nodes_image(old_nodes):
    pattern = r"(\!\[.*?\]\(.*?\)|\[.*?\]\(.*?\)|[^!\[\]()]+)"
    parts = re.findall(pattern, old_nodes[0].text)

    new_nodes = []
    link_text = None  # Temporary storage for alt-text

    for i in parts:
        if i.startswith("![") and i.endswith(")"):
            alt_text = re.search(r'\[.*?\]', i).group(0)[1:-1]  # Extract alt-text
            url = re.search(r'\(.*?\)', i).group(0)[1:-1]  # Extract URL
            new_nodes.append(TextNode(alt_text, TextType.LINK, url))
        elif i.startswith("[") and i.endswith(")"):
            link_text = i[1:-1]  # Remove brackets and store alt-text
        elif i.startswith("(") and i.endswith(")"):
            if link_text is not None:
                # Create a TextNode for the link with extracted text and URL
                new_nodes.append(TextNode(link_text, TextType.LINK, i[1:-1]))
                link_text = None  # Reset for next link
        else:
            new_nodes.append(TextNode(i, TextType.TEXT, None))  # Explicitly set url=None

    return new_nodes







def split_nodes_link(old_nodes):
    pattern = r"(\[.*?\]|\(.*?\)|[^()\[\]]+)"
    parts = re.findall(pattern, old_nodes[0].text)


    new_nodes = []
    link_text = None  # Temporary storage for alt-text

    for i in parts:
        if i.startswith("[") and i.endswith("]"):
            link_text = i[1:-1]  # Remove brackets and store alt-text

        elif i.startswith("(") and i.endswith(")"):
            if link_text is not None:
                # Create a TextNode for the link with extracted text and URL
                new_nodes.append(TextNode(link_text, TextType.LINK, i[1:-1]))
                link_text = None  # Reset for next link

        else:
            new_nodes.append(TextNode(i, TextType.TEXT, None))  # Explicitly set url=None

    return new_nodes









