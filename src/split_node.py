from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            return new_list
        split_node = node.text.split(delimiter)
        if len(split_node) == 1:
            new_list.append(TextNode(split_node), TextNode.TEXT)
            return new_list
        elif len(split_node) %2 != 0:
            raise Exception("invalid Markdown syntax")
        else:
            for i in range(0, len(split_node), 2):
                new_list.append(TextNode(split_node[0], TextType.TEXT))
                new_list.append(TextNode(split_node[1], text_type))
                new_list.append(TextNode(split_node[2], TextType.TEXT))
        
            
    return new_list