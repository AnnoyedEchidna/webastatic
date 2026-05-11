"""
TextNode Class tests for equality and disequality.  
"""
import unittest


from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    """
    TextNode class tests
    """

    def test_text_node_init(self):
        node = TextNode("This is plain text", TextType.PLAIN)
        self.assertEqual(node.text, "This is plain text")
        self.assertEqual(node.text_type.value, "plain")

        node2 = TextNode("This is bold text", TextType.BOLD)
        self.assertEqual(node2.text, "This is bold text")
        self.assertEqual(node2.text_type.value, "bold")

        node3 = TextNode("This is italic text", TextType.ITALIC)
        self.assertEqual(node3.text, "This is italic text")
        self.assertEqual(node3.text_type.value, "italic")

        node4 = TextNode("This is code text", TextType.CODE)
        self.assertEqual(node4.text, "This is code text")
        self.assertEqual(node4.text_type.value, "code")

        node5 = TextNode("This is link text", TextType.LINK,
                         "https://localhost:8888")
        self.assertEqual(node5.text, "This is link text")
        self.assertEqual(node5.text_type.value, "link")
        self.assertEqual(node5.url, "https://localhost:8888")

        node6 = TextNode("This is image text", TextType.IMAGE,
                         "src/images/favicon.ico")
        self.assertEqual(node6.text, "This is image text")
        self.assertEqual(node6.text_type.value, "image")
        self.assertEqual(node6.url, "src/images/favicon.ico")

        node7 = TextNode("Inferred plain text")
        self.assertEqual(node7.text, "Inferred plain text")
        self.assertEqual(node7.text_type.value, "plain")

        node8 = TextNode(None)
        self.assertEqual(node8.text, None)
        self.assertEqual(node8.text_type.value, "plain")

    def test_eq(self):
        """
        Test TextNode is __eq__ method
        """
        node = TextNode("This is a link node", TextType.LINK,
                        "https://localhost8888")
        node2 = TextNode("This is a link node", TextType.LINK,
                         "https://localhost8888")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        """
        Test TextNode not __eq__ method
        """
        # Test TextType != TextType
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

        # Test Text != Text
        node3 = TextNode("This is different text", TextType.PLAIN)
        node4 = TextNode("This text varies from above", TextType.PLAIN)
        self.assertNotEqual(node3, node4)

        # Test URL != URL
        node5 = TextNode("This is an image node with a url",
                         TextType.IMAGE, "src/img/image1")
        node6 = TextNode("This is an image node with a url",
                         TextType.IMAGE, "src/img/image2")
        self.assertNotEqual(node5, node6)

    def test_text_node_to_html_node(self):
        """
        Various tests for text_node_to_html_node function
        """
        # Test plain text
        plain_html_node = text_node_to_html_node(
            TextNode("This is plain text", "plain", None))
        self.assertEqual(plain_html_node.tag, None)
        self.assertEqual(plain_html_node.value, "This is plain text")

        # Test bold text
        bold_html_node = text_node_to_html_node(
            TextNode("This is bold text", "bold", None))
        self.assertEqual(bold_html_node.tag, "b")
        self.assertEqual(bold_html_node.value, "This is bold text")

        # Test italit text
        italic_html_node = text_node_to_html_node(
            TextNode("This is italic text", "italic", None))
        self.assertEqual(italic_html_node.tag, "i")
        self.assertEqual(italic_html_node.value, "This is italic text")

        # Test code text
        code_html_node = text_node_to_html_node(
            TextNode("This is code text", "code", None))
        self.assertEqual(code_html_node.tag, "code")
        self.assertEqual(code_html_node.value, "This is code text")

        # Test link text
        link_html_node = text_node_to_html_node(
            TextNode("This is link text", "link", "https://localhost:8888"))
        self.assertEqual(link_html_node.tag, "a")
        self.assertEqual(link_html_node.value, "This is link text")
        self.assertEqual(link_html_node.props_to_html(),
                         "href=\"https://localhost:8888\"")

        # Test img text
        img_html_node = text_node_to_html_node(
            TextNode("This is img alt text", "image", "src/img/favicon.jpg"))
        self.assertEqual(img_html_node.tag, "img")
        self.assertEqual(img_html_node.value, None)
        self.assertEqual(img_html_node.props_to_html(
        ), "src=\"src/img/favicon.jpg\" alt=\"This is img alt text\"")

    def test_text_node_to_html_node_no_type(self):
        """
        Test text node without text_type attribute; should raise ValueError
        """
        with self.assertRaises(ValueError):
            text_node_to_html_node(
                TextNode("This is untyped text", None, None))

    def test_split_nodes_delimiter(self):
        """
        Test split_nodes_delimiter method
        """
        old_node = TextNode("This will be **bold** text")
        new_nodes = split_nodes_delimiter([old_node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text, "This will be ")
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[2].text, " text")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN)

        another_node = TextNode("_All_ together now!")
        more_new_nodes = split_nodes_delimiter(
            [another_node], "_", TextType.ITALIC)
        self.assertEqual(more_new_nodes[0].text, "All")
        self.assertEqual(more_new_nodes[1].text, " together now!")
        self.assertEqual(more_new_nodes[0].text_type, TextType.ITALIC)
        self.assertEqual(more_new_nodes[1].text_type, TextType.PLAIN)

        non_plain_text_node = TextNode("This is already _bold_", TextType.BOLD)
        one_new_node = split_nodes_delimiter(
            [non_plain_text_node], "_", TextType.ITALIC)
        self.assertEqual(one_new_node[0].text, "This is already _bold_")
        self.assertEqual(one_new_node[0].text_type, TextType.BOLD)
        self.assertEqual(len(one_new_node), 1)

        broken_delimiter = TextNode(
            "There is only one **delimeter for this one")
        with self.assertRaises(ValueError):
            split_nodes_delimiter([broken_delimiter], "**", TextType.BOLD)

        with self.assertRaises(ValueError):
            split_nodes_delimiter([], "**", TextType.BOLD)


if __name__ == "__main__":
    unittest.main()
