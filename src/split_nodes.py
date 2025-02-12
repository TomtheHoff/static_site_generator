
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

    sections = original_text.split(f"![{image_alt}]({image_link})", 1)

    pass





node = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"


def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.LINK:
            # If it's not plain text, just add it as-is
            new_nodes.append(node)
            continue  # Skip the rest of the loop for this node

        # Regex: Alles zwischen `[` und `]` ODER `(` und `)` oder normaler Text
    pattern = r"(\[.*?\]|\(.*?\)|[^()\[\]]+)"

    # `re.findall` extrahiert alle passenden Teile
    parts = re.findall(pattern, old_nodes)
    print (split_nodes_link(node))



'''

node = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
new_nodes = extract_markdown_links(node)
#output = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
print(f"\033[93m{new_nodes=}\033[0m")

'''

'''
********** Das ist die Aufgabenstellung **********

node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)

new_nodes = split_nodes_link([node])
 [
     TextNode("This is text with a link ", TextType.TEXT),
     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
     TextNode(" and ", TextType.TEXT),
     TextNode(
         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
    ),
]


'''






node = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

# Regex: Alles zwischen `[` und `]` ODER `(` und `)` oder normaler Text
pattern = r"(\[.*?\]|\(.*?\)|[^()\[\]]+)"

# `re.findall` extrahiert alle passenden Teile
parts = re.findall(pattern, node)

print(f"\033[93m{parts=}\033[0m")
