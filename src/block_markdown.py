from enum import Enum

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

