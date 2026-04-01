from textnode import TextType, TextNode

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
