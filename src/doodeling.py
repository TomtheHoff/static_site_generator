import re
from textnode import TextNode, TextType
from regex_extract import extract_markdown_links, extract_markdown_images

node = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"



def split_nodes_link(old_nodes):
    """Splits text nodes into multiple nodes, separating links and normal text."""
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue  # Skip non-text nodes
        
        text = node.text
        links = extract_markdown_links(text)  # Extract (alt_text, url) pairs

        if not links:
            new_nodes.append(TextNode(text, TextType.TEXT))  # No links, keep as plain text
            continue

        # Process the text and insert links correctly
        while links:
            alt_text, url = links.pop(0)  # Extract first link

            before_link, rest = text.split(f"[{alt_text}]({url})", 1)
            if before_link:
                new_nodes.append(TextNode(before_link, TextType.TEXT))
            
            new_nodes.append(TextNode(alt_text, TextType.LINK, url))

            text = rest  # Continue processing remaining text

        if text:  # Add any remaining text
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

print (split_nodes_link(node))