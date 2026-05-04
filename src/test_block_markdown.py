import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_paragraph(self):
        block = "normal paragraph"
        result = block_to_block_type(block)
        expected = BlockType.paragraph
        self.assertEqual(result, expected)

    def test_block_to_heading(self):
        block = "# heading"
        result = block_to_block_type(block)
        expected = BlockType.heading
        self.assertEqual(result, expected)

    def test_block_to_code(self):
        block = "```\ncode block```"
        result = block_to_block_type(block)
        expected = BlockType.code
        self.assertEqual(result, expected)
        
    def test_block_to_quote(self):
        block = "> first quote line\n> second quote line"
        result = block_to_block_type(block)
        expected = BlockType.quote
        self.assertEqual(result, expected)
        
    def test_block_to_unordered_list(self):
        block = "- first item\n- second item"
        result = block_to_block_type(block)
        expected = BlockType.unordered_list
        self.assertEqual(result, expected)
        
    def test_block_to_ordered_list(self):
        block = "1. first item\n2. second item"
        result = block_to_block_type(block)
        expected = BlockType.ordered_list
        self.assertEqual(result, expected)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.quote)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

