import re
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

def extract_markdown_images(text):
    alt_texts = re.findall(r"!\[(.*?)\]\(.*?\)", text)
    urls = re.findall(r"!\[.*?\]\((.*?)\)", text)
    return list(zip(alt_texts, urls))

def extract_markdown_links(text):
    anchor_texts = re.findall(r"(?<!!)\[(.*?)\]\(.*?\)", text)
    urls = re.findall(r"(?<!!)\[.*?\]\((.*?)\)", text)
    return list(zip(anchor_texts, urls))

def split_nodes_image(old_nodes):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes.append(old_node)
            continue
        text = old_node.text
        images = extract_markdown_images(text)
        if len(images) == 0:
            nodes.append(old_node)
            continue
        for image in images:
            sections = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise Exception("Invalid Markdown Syntax, image section not closed")
            if sections[0] != "":
                nodes.append(TextNode(sections[0], TextType.TEXT))
            nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text = sections[1]
        if text != "":
            nodes.append(TextNode(text, TextType.TEXT))
    return nodes

def split_nodes_link(old_nodes):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes.append(old_node)
            continue
        text = old_node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            nodes.append(old_node)
            continue
        for link in links:
            sections = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise Exception("Invalid Markdown Syntax, link section not closed")
            if sections[0] != "":
                nodes.append(TextNode(sections[0], TextType.TEXT))
            nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text = sections[1]
        if text != "":
            nodes.append(TextNode(text, TextType.TEXT))
    return nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
