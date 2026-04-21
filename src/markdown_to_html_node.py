from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type
from htmlnode import HTMLNode, LeafNode, ParentNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)