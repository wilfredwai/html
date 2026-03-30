#text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
#print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

#text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
#print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

#import re
#text = "I'm a little teapot, short and stout. Here is my handle, here is my spout."
#matches = re.findall(r"teapot", text)
#print(matches) # ['teapot']

#text = "My email is lane@example.com and my friend's email is hunter@example.com"
#matches = re.findall(r"(\w+)@(\w+\.\w+)", text)
#print(matches)  # [('lane', 'example.com'), ('hunter', 'example.com')]
import re

def extract_markdown_images(text):
    matches = []
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = []
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches