"""
TextNode Class tests for equality and disequality.  
"""
import unittest


from textnode import TextNode, TextType, text_node_to_html_node



class TestTextNode(unittest.TestCase):
    """
    TextNode class tests
    """

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
        #Test plain text 
        plain_html_node = text_node_to_html_node(TextNode("This is plain text", "plain", None))
        self.assertEqual(plain_html_node.tag, None)
        self.assertEqual(plain_html_node.value, "This is plain text")

        #Test bold text
        bold_html_node = text_node_to_html_node(TextNode("This is bold text", "bold", None))
        self.assertEqual(bold_html_node.tag, "b")
        self.assertEqual(bold_html_node.value, "This is bold text")

        #Test italit text
        italic_html_node = text_node_to_html_node(TextNode("This is italic text", "italic", None))
        self.assertEqual(italic_html_node.tag, "i")
        self.assertEqual(italic_html_node.value, "This is italic text")

        #Test code text
        code_html_node = text_node_to_html_node(TextNode("This is code text", "code", None))
        self.assertEqual(code_html_node.tag, "code")
        self.assertEqual(code_html_node.value, "This is code text")

        #Test link text
        link_html_node = text_node_to_html_node(TextNode("This is link text", "link", "https://localhost:8888"))
        self.assertEqual(link_html_node.tag, "a")
        self.assertEqual(link_html_node.value, "This is link text")
        self.assertEqual(link_html_node.props_to_html(), "href=\"https://localhost:8888\"")
        
        #Test img text
        img_html_node = text_node_to_html_node(TextNode("This is img alt text", "image", "src/img/favicon.jpg"))
        self.assertEqual(img_html_node.tag, "img")
        self.assertEqual(img_html_node.value, None)
        self.assertEqual(img_html_node.props_to_html(), "src=\"src/img/favicon.jpg\" alt=\"This is img alt text\"")    

    def test_text_node_to_html_node_no_type(self):
        with self.assertRaises(ValueError):
            untyped_html_node = text_node_to_html_node(TextNode("This is untyped text", None, None))

if __name__ == "__main__":
    unittest.main()
    