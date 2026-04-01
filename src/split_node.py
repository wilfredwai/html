from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        split_node = node.text.split(delimiter)
        if len(split_node) == 1:
            new_list.append(node)
        elif len(split_node) %2 == 0:
            raise Exception("invalid Markdown syntax")
        else:
            for i in range(0, len(split_node)):
                if split_node[i] != "":
                    if i %2 == 0:
                        new_list.append(TextNode(split_node[i], TextType.TEXT))
                    else:
                        new_list.append(TextNode(split_node[i], text_type))
    return new_list

def split_nodes_image(old_nodes):
    new_node = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_node.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_node.append(old_node)
            continue
        else:
            original_text = old_node.text
            for image in images:
                section = original_text.split(f"![{image[0]}]({image[1]})", 1)
                if section[0] != "":
                    new_node.append(TextNode(section[0], TextType.TEXT))
                new_node.append(TextNode(image[0], TextType.IMAGE, image[1]))
                original_text = section[1]
            if original_text != "":
                new_node.append(TextNode(original_text, TextType.TEXT))
    return new_node

def split_nodes_link(old_nodes):
    new_node = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_node.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            new_node.append(old_node)
            continue
        else:
            original_text = old_node.text
            for link in links:
                section = original_text.split(f"[{link[0]}]({link[1]})", 1)
                if section[0] != "":
                    new_node.append(TextNode(section[0], TextType.TEXT))
                new_node.append(TextNode(link[0], TextType.LINK, link[1]))
                original_text = section[1]
            if original_text != "":
                new_node.append(TextNode(original_text, TextType.TEXT))
    return new_node



# linki r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"