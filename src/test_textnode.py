"""
TextNode Class tests for equality and disequality.  
"""
import unittest


from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
