from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    delimiters = ["'", "**", "_"]
    for nodes in old_nodes:
        if not nodes.text_type is TextType.TEXT:
            new_list.append(nodes)
        for dels in delimiters:
            if dels not in nodes.text:
                raise Exception("invalid Markdown syntax, no delimiter found in the node")
        