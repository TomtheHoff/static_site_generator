import re

node = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
pattern = r"(\[.*?\]|\(.*?\)|[^()\[\]]+)"
parts = re.findall(pattern, node)

for i in parts:
    if i.startswith("[") and i.endswith("]"):
        i += ", TextType.LINK, "
    elif i.startswith("(") and i.endswith(")"):
        i = i[1:-1]
        # This is the actual link
    else:
        i += ", TextType.TEXT"


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