from textnode import TextType, TextNode
from split_node import split_nodes_delimiter
from split_nodes_image_and_link import split_nodes_image, split_nodes_link

"""
This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
"""

def text_to_textnodes(text):
    original_text = text
    input = []
    output = []
    node = TextNode(original_text, TextType.TEXT)
    input.append(node)
    bold_node = split_nodes_delimiter(input, "**", TextType.BOLD)
    
    italic_node = split_nodes_delimiter(bold_node, "_", TextType.ITALIC)
    
    code_node = split_nodes_delimiter(italic_node, "`", TextType.CODE)
    
    image_node = split_nodes_image(code_node)
    
    link_node = split_nodes_link(image_node)
    
    return link_node
    