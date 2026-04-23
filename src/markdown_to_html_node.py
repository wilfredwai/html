from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.appended(html_node)
    return ParentNode("div", children)

def text_to_children(text):
        text_nodes = text_to_textnodes(text)
        children = []
        for text_node in text_nodes:
            html_node = text_node_to_html_node(text_node)
            children.append(html_node)
        return children

def paragraph_to_html_node(block):
    clean_text = block.replace("\n", " ")
    children = text_to_children(clean_text)
    return ParentNode(tag="p", children = children)
     
def heading_to_html_node(block):
    count = block.count("#")
    if count == 0:
        return block