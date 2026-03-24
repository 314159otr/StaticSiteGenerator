from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes.append(old_node)
            continue
        strings = old_node.text.split(delimiter)
        if len(strings) > 1 and len(strings) % 2 == 0:
            raise Exception("Invalid Markdown Syntax")
        for index, string in enumerate(strings):
            if string == "":
                continue
            if index % 2 == 0:
                    nodes.append(TextNode(string, TextType.TEXT))
            else:
                nodes.append(TextNode(string, text_type))
    return nodes
