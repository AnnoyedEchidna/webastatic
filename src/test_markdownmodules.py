"""
Tests for markdown modules
"""

import unittest

from markdownmodules import BlockType, block_to_block_type, markdown_to_blocks


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
        block = """```\nThis is supposed to be code```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type_improper_start_code(self):
        """
        Test block_to_block_type passing code block improperly formatted
        """
        block = """```This is supposed to be code```"""
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
        block = """1. Ordered list here!"""
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


if __name__ == "__main__":
    unittest.main()
