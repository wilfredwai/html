from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from split_node import split_nodes_delimiter
from extract_markdown import extract_markdown_images, extract_markdown_links
from split_nodes_image_and_link import split_nodes_image, split_nodes_link

"""
This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
"""

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    splited_node = split_node(node,)