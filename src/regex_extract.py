import re

def extract_markdown_images(text):
    list = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    #print(f"\033[93m{list=}\033[0m")
    return list

def extract_markdown_links(text):
    list = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    #print(f"\033[93m{list=}\033[0m")
    return list



'''
node = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
new_nodes = extract_markdown_links(node)
#output = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
print(f"\033[93m{new_nodes=}\033[0m")
'''

