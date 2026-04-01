from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextType, TextNode

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

