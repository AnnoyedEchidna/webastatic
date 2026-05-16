"""
Tests for markdown modules
"""

import unittest

from markdownmodules import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks,
    markdown_to_html_node,
)


class TestMarkdownModules(unittest.TestCase):
    """
    Class for markdown modules testing
    """

    def test_markdown_to_blocks(self):
        """
        Test for markdown_to_blocks function with provided test
        """
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

    def test_markdown_to_blocks_first_example(self):
        """
        Test for markdown_to_blocks function with first provided example
        """
        md = """
        # This is a heading

        This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

        - This is the first list item in a list block
        - This is a list item
        - This is another list item

        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item",
            ],
        )

    def test_markdown_to_blocks_no_md(self):
        """
        Test markdown_to_blocks with passing no markdown text
        """
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    # TEST block_to_block_type
    def test_block_to_block_type_heading(self):
        """
        Test block_to_bloc_type using heading block with single #
        """
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_multi_heading(self):
        """
        Test block_to_bloc_type using heading block with single #
        """
        block = "##### This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        """
        Test block_to_block_type passing code block
        """
        block = """```\nThis is supposed to be code\n```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type_improper_start_code(self):
        """
        Test block_to_block_type passing code block improperly formatted
        """
        block = """```This is supposed to be code\n```"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_improper_end_code(self):
        """
        Test block_to_block_type passing code block improperly formatted
        """
        block = """```\nThis is supposed to be code``"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_quote(self):
        """
        Test block_to_block_type passing quote block
        """
        block = """> I am quoting someone special"""
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_block_type_u_l(self):
        """
        Test block_to_block_type passing unordered list
        """
        block = """- Unordered list here!"""
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_improper_u_l(self):
        """
        Test block_to_block_type passing unorderd list imporperly formatted
        """
        block = """-Unordered list here!"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_o_l(self):
        """
        Test block_to_block_type passing ordered list
        """
        block = """1. Ordered list here!\n2. Second ordered list item\n3. Third ordered list item"""
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_block_to_block_type_improper_o_l(self):
        """
        Test block_to_block_type passing ordered list
        """
        block = """1 Ordered list here!"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_improper_heading(self):
        """
        Test block_to_block_type passing ordered list
        """
        block = """ ## Bad heading"""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # TEST markdown_to_html function
    def test_markdown_to_html_node_heading(self):
        """
        Test markdown_to_html_node function passing a heading to verify the heading number output
        """
        md = "# Heading block"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><h1>Heading block</h1></div>")

    def test_markdown_to_html_node_blockquote(self):
        """
        Test markdown_to_html_node function passing a blockquote without a leading space
        """
        md = ">blockquote block without space"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html, "<div><blockquote>blockquote block without space</blockquote></div>"
        )

    def test_markdown_to_html_node_blockquote_space(self):
        """
        Test markdown_to_html_node function passing a block quote with a leading space
        """
        md = "> blockquote block with space"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html, "<div><blockquote>blockquote block with space</blockquote></div>"
        )

    def test_markdown_to_html_node_paragraph(self):
        """
        Test markdown_to_html_node function passing a paragraph with no formatting
        """
        md = "paragraph with no other formatting"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><p>paragraph with no other formatting</p></div>")

    def test_markdown_to_html_node_paragraph_formatting(self):
        """
        Test markdown_to_html_node function passing a paragraph with in-line formatting
        """
        md = "paragraph with **bold** and _italic_ formatting"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><p>paragraph with <b>bold</b> and <i>italic</i> formatting</p></div>",
        )

    def test_markdown_to_html_node_unordered_list(self):
        """
        Test markdown_to_html_node function passing an unorderd list
        """
        md = "- Unordered list item 1\n- UL list item 2\n- UL list 3"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Unordered list item 1</li><li>UL list item 2</li><li>UL list 3</li></ul></div>",
        )

    def test_markdown_to_html_node_ordered_list(self):
        """
        Test markdown_to_html_node function passing an orderd list
        """
        md = "1. Ordered list item 1\n2. OL list item 2\n3. OL list 3"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Ordered list item 1</li><li>OL list item 2</li><li>OL list 3</li></ol></div>",
        )

    def test_markdown_to_html_node_code(self):
        """
        Test markdown_to_html_node passing a code block

        """
        md = """```\nThis is supposed to be code\nwith some lines\ninbetween the ends\n```"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is supposed to be code\nwith some lines\ninbetween the ends\n</code></pre></div>",
        )

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


if __name__ == "__main__":
    unittest.main()
