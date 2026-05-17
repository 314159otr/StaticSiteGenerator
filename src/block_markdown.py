from enum import Enum
from textnode import text_node_to_html_node, TextNode, TextType
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    result_blocks = []
    for block in blocks:
        if block == "":
            continue
        result_blocks.append(block.strip())
    return result_blocks

class BlockType(Enum):
    paragraph = 1
    heading = 2
    code = 3
    quote = 4
    unordered_list = 5
    ordered_list = 6

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.heading
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.code
    if block.startswith(">"):
        lines = block.split("\n")
        for line in lines:
            if not line.startswith(">"):
                return BlockType.paragraph
        return BlockType.quote
    if block.startswith("- "):
        lines = block.split("\n")
        for line in lines:
            if not line.startswith("- "):
                return BlockType.paragraph
        return BlockType.unordered_list
    n = None
    for chars in range(0, len(block)):
        if block[0:chars+1].isdigit():
            continue
        if chars > 0:
            n = block[0:chars]
        break
    if n is not None and block.startswith(". ", len(n)):
        n = int(n)
        lines = block.split("\n")
        for line in lines:
            if not line.startswith(str(n) + ". "):
                return BlockType.paragraph
            n += 1
        return BlockType.ordered_list

    return BlockType.paragraph

def text_to_children(text):
    children_nodes = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        children_nodes.append(text_node_to_html_node(text_node))
    return children_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.paragraph:
                tag = "p"
                text = block.replace("\n", " ")
                block_children = text_to_children(text)
                block_node = ParentNode(tag, block_children)
                parent_children.append(block_node)
            case BlockType.heading:
                heading_number = block.find(" ")
                tag = f"h{heading_number}"
                text = block[heading_number + 1:]
                block_children = text_to_children(text)
                block_node = ParentNode(tag, block_children)
                parent_children.append(block_node)
            case BlockType.code:
                tag = "pre"
                firstline = block.find("\n") + 1
                lastline = block.rfind("\n") + 1
                text = block[firstline:lastline]
                block_children = text_node_to_html_node(TextNode(text, TextType.CODE))
                block_node = ParentNode(tag, [block_children])
                parent_children.append(block_node)
            case BlockType.quote:
                tag = "blockquote"
                text = block.replace("> ", "").replace("\n", " ")
                block_children = text_to_children(text)
                block_node = ParentNode(tag, block_children)
                parent_children.append(block_node)
            case BlockType.unordered_list:
                tag = "ul"
                text = block.replace("- ", "")
                lines = text.split("\n")
                block_children = []
                for line in lines:
                    block_children.append(ParentNode("li",text_to_children(line)))
                block_node = ParentNode(tag, block_children)
                parent_children.append(block_node)
            case BlockType.ordered_list:
                tag = "ol"
                text = block
                lines = text.split("\n")
                block_children = []
                for line in lines:
                    index = line.find(". ") + 2
                    block_children.append(ParentNode("li",text_to_children(line[index:])))
                block_node = ParentNode(tag, block_children)
                parent_children.append(block_node)
            case _:
                raise ValueError("invalid block type")
    parent_node = ParentNode("div", parent_children)
    return parent_node
