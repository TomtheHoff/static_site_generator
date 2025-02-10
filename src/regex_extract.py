import re

def extract_markdown_images(text):
    list = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    #print(f"\033[93m{list=}\033[0m")
    return list

def extract_markdown_links(text):
    list = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    #print(f"\033[93m{list=}\033[0m")
    return list




