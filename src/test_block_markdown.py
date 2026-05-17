import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

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

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_headers(self):
        md = """
# This is a 1# header

## This is a 2# header

### This is a 3# header

#### This is a 4# header

##### This is a 5# header

###### This is a 6# header

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a 1# header</h1><h2>This is a 2# header</h2><h3>This is a 3# header</h3><h4>This is a 4# header</h4><h5>This is a 5# header</h5><h6>This is a 6# header</h6></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_blockquotes(self):
        md = """
> This is a single line quote

> This is a
> Multiline quote

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a single line quote</blockquote><blockquote>This is a Multiline quote</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- This is the 1 item
- This is the 2 item

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is the 1 item</li><li>This is the 2 item</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. This is the 1 item
2. This is the 2 item

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is the 1 item</li><li>This is the 2 item</li></ol></div>",
        )


    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
