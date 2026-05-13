"""
TextNode Class tests for equality and disequality.  
"""
import unittest


from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    """
    TextNode class tests
    """

    def test_text_node_init_plain(self):
        """
        Test TextNode init with plain text
        """
        node = TextNode("This is plain text", TextType.PLAIN)
        self.assertEqual(node.text, "This is plain text")
        self.assertEqual(node.text_type.value, "plain")

    def test_text_node_init_bold(self):
        """
        Test TextNode init with bold text
        """
        node2 = TextNode("This is bold text", TextType.BOLD)
        self.assertEqual(node2.text, "This is bold text")
        self.assertEqual(node2.text_type.value, "bold")

    def test_text_node_init_italic(self):
        """
        Test TextNode init with italic text
        """
        node3 = TextNode("This is italic text", TextType.ITALIC)
        self.assertEqual(node3.text, "This is italic text")
        self.assertEqual(node3.text_type.value, "italic")

    def test_text_node_init_code(self):
        """
        Test TextNode init with code text
        """
        node4 = TextNode("This is code text", TextType.CODE)
        self.assertEqual(node4.text, "This is code text")
        self.assertEqual(node4.text_type.value, "code")

    def test_text_node_init_link(self):
        """
        Test TextNode init with link text and url
        """
        node5 = TextNode("This is link text", TextType.LINK,
                         "https://localhost:8888")
        self.assertEqual(node5.text, "This is link text")
        self.assertEqual(node5.text_type.value, "link")
        self.assertEqual(node5.url, "https://localhost:8888")

    def test_text_node_init_image(self):
        """
        Test TextNode init with image text with url
        """
        node6 = TextNode("This is image text", TextType.IMAGE,
                         "src/images/favicon.ico")
        self.assertEqual(node6.text, "This is image text")
        self.assertEqual(node6.text_type.value, "image")
        self.assertEqual(node6.url, "src/images/favicon.ico")

    def test_text_node_init_plain_by_default(self):
        """
        Test TextNode init with no specified text type, default is plain
        """
        node7 = TextNode("Inferred plain text")
        self.assertEqual(node7.text, "Inferred plain text")
        self.assertEqual(node7.text_type.value, "plain")

    def test_text_node_init_none(self):
        """
        Test TextNode init with no text or text type
        """
        node8 = TextNode(None)
        self.assertEqual(node8.text, None)
        self.assertEqual(node8.text_type.value, "plain")

    def test_text_node_eq(self):
        """
        Test TextNode is __eq__ method
        """
        node = TextNode("This is a link node", TextType.LINK,
                        "https://localhost8888")
        node2 = TextNode("This is a link node", TextType.LINK,
                         "https://localhost8888")
        self.assertEqual(node, node2)

    def test_text_type_not_eq(self):
        """
        Test TextNode.text_type not __eq__ 
        """
        # Test TextType != TextType
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_text_node_not_eq(self):
        """
        Test TextNode.text not __eq__
        """
        node3 = TextNode("This is different text", TextType.PLAIN)
        node4 = TextNode("This text varies from above", TextType.PLAIN)
        self.assertNotEqual(node3, node4)

    def test_text_url_not_eq(self):
        """
        Test TextNode.url not __eq__
        """
        node5 = TextNode("This is an image node with a url",
                         TextType.IMAGE, "src/img/image1")
        node6 = TextNode("This is an image node with a url",
                         TextType.IMAGE, "src/img/image2")
        self.assertNotEqual(node5, node6)

    def test_text_node_to_html_node_plain(self):
        """
        Test text_node_to_html_node function with plain text
        """
        plain_html_node = text_node_to_html_node(
            TextNode("This is plain text", "plain", None))
        self.assertEqual(plain_html_node.tag, None)
        self.assertEqual(plain_html_node.value, "This is plain text")

    def test_text_node_to_html_node_bold(self):
        """
        Test text_node_to_html_node function with bold text
        """
        bold_html_node = text_node_to_html_node(
            TextNode("This is bold text", "bold", None))
        self.assertEqual(bold_html_node.tag, "b")
        self.assertEqual(bold_html_node.value, "This is bold text")

    def test_text_node_to_html_node_italic(self):
        """
        Test text_node_to_html_node function with italic text
        """
        italic_html_node = text_node_to_html_node(
            TextNode("This is italic text", "italic", None))
        self.assertEqual(italic_html_node.tag, "i")
        self.assertEqual(italic_html_node.value, "This is italic text")

    def test_text_node_to_html_node_code(self):
        """
        Test text_node_to_html_node function with code text
        """
        code_html_node = text_node_to_html_node(
            TextNode("This is code text", "code", None))
        self.assertEqual(code_html_node.tag, "code")
        self.assertEqual(code_html_node.value, "This is code text")

    def test_text_node_to_html_node_link(self):
        """
        Test text_node_to_html_node function with link text and url
        """
        link_html_node = text_node_to_html_node(
            TextNode("This is link text", "link", "https://localhost:8888"))
        self.assertEqual(link_html_node.tag, "a")
        self.assertEqual(link_html_node.value, "This is link text")
        self.assertEqual(link_html_node.props_to_html(),
                         "href=\"https://localhost:8888\"")

    def test_text_node_to_html_node_image(self):
        """
        Test text_node_to_html_node function with image text and url
        """
        img_html_node = text_node_to_html_node(
            TextNode("This is img alt text", "image", "src/img/favicon.jpg"))
        self.assertEqual(img_html_node.tag, "img")
        self.assertEqual(img_html_node.value, "")
        self.assertEqual(img_html_node.props_to_html(
        ), "src=\"src/img/favicon.jpg\" alt=\"This is img alt text\"")

    def test_text_node_to_html_node_no_type(self):
        """
        Test text node without text_type attribute; should raise ValueError
        """
        with self.assertRaises(ValueError):
            text_node_to_html_node(
                TextNode("This is untyped text", None, None))


if __name__ == "__main__":
    unittest.main()
