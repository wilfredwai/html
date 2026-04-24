from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
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
    return ParentNode(tag = "p", children = children)
     
def heading_to_html_node(block):
    splited = block.split(" ", 1)
    count = len(splited[0])
    children = text_to_children(splited[1])
    return ParentNode(tag = f"h{count}", children = children)

def code_to_html_node(block):
     l_splited = block.split("\n", 1)
     r_splited = l_splited[1].rsplit("```", 1)
     list_to_str = r_splited[0]
     raw_text_node = TextNode(text=list_to_str, text_type=TextType.TEXT)
     code_child = text_node_to_html_node(raw_text_node)
     code_node = ParentNode(tag = "code", children = [code_child])
     return ParentNode(tag = "pre", children = [code_node])

def quote_to_html_node(block):
    lines = block.split("\n")
    raw_text = []
    for line in lines:
        new_line = line.lstrip(">").strip()
        raw_text.append(new_line)
    text = " ".join(raw_text)
    children = text_to_children(text)
    return ParentNode(tag = "blockquote", children= children)

def ulist_to_html_node(block):
     li_node = []
     lines = block.split("\n")
     for line in lines:
        new_line = line[2:]
        children = text_to_children(new_line)
        li_node.append(ParentNode(tag = "li", children= children))
     return ParentNode(tag = "ul", children = li_node)

def olist_to_html_node(block):
    lines = block.split("\n")
    li_node = []
    for line in lines:
        new_line = line[line.index(" ") + 1:]
        children = text_to_children(new_line)
        li_node.append(ParentNode(tag = "li", children = children))
    return ParentNode(tag = "ol", children = li_node)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.ORDERED:
        return olist_to_html_node(block)
    if block_type == BlockType.UNORDERED:
        return ulist_to_html_node(block)
    raise ValueError("invalid block type")