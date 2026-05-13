"""
TextNode Class tests for equality and disequality.  
"""
import unittest


from textnode import TextNode, TextType
from textmodules import split_nodes_delimiter, extract_markdown_images


class TestTextNode(unittest.TestCase):
    """
    TextModules functions tests
    """

    # Test split_node_delimiter function

    def test_split_nodes_delimiter_bold(self):
        """
        Test split_nodes_delimiter method with bold delimiters
        """
        old_node = TextNode("This will be **bold** text")
        new_nodes = split_nodes_delimiter([old_node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text, "This will be ")
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[2].text, " text")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN)

    def test_split_nodes_delimiter_first_node_italic(self):
        """
        Test split_nodes_delimiter method with italic delimiters with first node delimited
        """
        another_node = TextNode("_All_ together now!")
        more_new_nodes = split_nodes_delimiter(
            [another_node], "_", TextType.ITALIC)
        self.assertEqual(more_new_nodes[0].text, "All")
        self.assertEqual(more_new_nodes[1].text, " together now!")
        self.assertEqual(more_new_nodes[0].text_type, TextType.ITALIC)
        self.assertEqual(more_new_nodes[1].text_type, TextType.PLAIN)

    def test_split_nodes_delimiter_last_node_italic(self):
        """
        Test split_nodes_delimiter method with italic delimiters with last node delimited
        """
        another_node = TextNode("All together _now!_")
        more_new_nodes = split_nodes_delimiter(
            [another_node], "_", TextType.ITALIC)
        self.assertEqual(more_new_nodes[0].text, "All together ")
        self.assertEqual(more_new_nodes[1].text, "now!")
        self.assertEqual(more_new_nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(more_new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(len(more_new_nodes), 2)

    def test_split_nodes_delimiter_not_plain_input(self):
        """
        Test split_nodes_delimiter method with italic delimiters but bold text_type
        """
        non_plain_text_node = TextNode("This is already _bold_", TextType.BOLD)
        one_new_node = split_nodes_delimiter(
            [non_plain_text_node], "_", TextType.ITALIC)
        self.assertEqual(one_new_node[0].text, "This is already _bold_")
        self.assertEqual(one_new_node[0].text_type, TextType.BOLD)
        self.assertEqual(len(one_new_node), 1)

    def test_split_nodes_delimiter_double_bold(self):
        """
        Test split_nodes_delimiter method with two bold delimiters
        """
        double_delimiter = TextNode(
            "This text is **bold** but this is **bolder**")
        double_delim_split = split_nodes_delimiter(
            [double_delimiter], "**", TextType.BOLD)
        self.assertEqual(double_delim_split[0].text, "This text is ")
        self.assertEqual(double_delim_split[1].text, "bold")
        self.assertEqual(double_delim_split[2].text, " but this is ")
        self.assertEqual(double_delim_split[3].text, "bolder")
        self.assertEqual(double_delim_split[0].text_type, TextType.PLAIN)
        self.assertEqual(double_delim_split[1].text_type, TextType.BOLD)
        self.assertEqual(double_delim_split[2].text_type, TextType.PLAIN)
        self.assertEqual(double_delim_split[3].text_type, TextType.BOLD)

    def test_split_nodes_delimiter_unmatched_delimiter(self):
        """
        Test split_nodes_delimiter method with one missing bold delimiter
        """
        broken_delimiter = TextNode(
            "There is only one **delimeter for this one")
        with self.assertRaises(ValueError):
            split_nodes_delimiter([broken_delimiter], "**", TextType.BOLD)

    def test_split_nodes_delimiter_no_delimiter(self):
        """
        Test split_nodes_delimiter without passing any delimiters in the input string.
        """
        plain_to_plain = TextNode(
            "This is entirely plain text", TextType.PLAIN)
        plain_no_split = split_nodes_delimiter(
            [plain_to_plain], "**", TextType.BOLD)
        self.assertEqual(plain_no_split[0].text, "This is entirely plain text")
        self.assertEqual(plain_no_split[0].text_type, TextType.PLAIN)

    def test_split_nodes_delimiter_empty_list(self):
        """
        Test split_nodes_delimiter method with empty input list
        """
        with self.assertRaises(ValueError):
            split_nodes_delimiter([], "**", TextType.BOLD)


if __name__ == "__main__":
    unittest.main()
