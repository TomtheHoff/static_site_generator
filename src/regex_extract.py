


def extract_markdown_images(text):
    list = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    print(f"\033[93m{list=}\033[0m")


    '''
    
text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    '''