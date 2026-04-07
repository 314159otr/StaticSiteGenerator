
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    result_blocks = []
    for block in blocks:
        if block == "":
            continue
        result_blocks.append(block.strip())
    return result_blocks
