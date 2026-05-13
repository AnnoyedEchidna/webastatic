"""
HTMLNode Class tests for equality and disequality.  
"""

import unittest


from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    """
    TEST HTMLNode class and methods
    """

    # TEST HTMLNode init method
    def test_html_node_init_p(self):
        """
        Test HTMLNode init with p tag
        """
        node = HTMLNode("p", "This is a p text", None, None)
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a p text")

    def test_html_node_init_h1(self):
        """
        Test HTMLNode init with h1 tag
        """
        node = HTMLNode("h1", "This is a big boy heading", None, None)
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "This is a big boy heading")

    def test_html_node_init_link_w_props(self):
        """
        Test HTMLNode init with link tag
        """
        node = HTMLNode("a", "This is a link with props",
                        None, {"href": "someplace.com"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "This is a link with props")
        self.assertEqual(node.props_to_html(), "href=\"someplace.com\"")

    def test_html_node_init_image_w_props(self):
        """
        Test HTMLNode init with image tag
        """
        node = HTMLNode("img", "This is an image with props",
                        None, {"src": "src/images/favicon.ico"})
        self.assertEqual(node.tag, "img")
        self.assertEqual(node.value, "This is an image with props")
        self.assertEqual(node.props_to_html(),
                         "src=\"src/images/favicon.ico\"")

    # TEST props_to_html method

    def test_props_to_html_link_single_prop(self):
        """
        test props_to_html method with link node and one prop value. 
        """
        # Test single prop
        node = HTMLNode("a", "This is a link", None, {
                        "href": "https://localhost:8888"})
        node_solution = "href=\"https://localhost:8888\""
        self.assertEqual(node.props_to_html(), node_solution)

    def test_props_to_html_link_double_props(self):
        """
        test props_to_html method with link node with two props values. 
        """
        node2 = HTMLNode("a", "This is a link", None, {
            "href": "https://localhost:8888", "target": "_blank"})
        self.assertEqual(node2.props_to_html(),
                         "href=\"https://localhost:8888\" target=\"_blank\"")

    def test_props_to_html_link_no_props(self):
        """
        test props_to_html method with paragraph node and no prop values. 
        """
        node3 = HTMLNode("p", "This is a paragraph", None, None)
        self.assertEqual(node3.props_to_html(), "")

    # TEST to_html method

    def test_to_html_raises_implerror(self):
        """
        test HTMLNode.to_html() method raises error when not overwritten by child class
        """
        node = HTMLNode("h1", "This is a big boy heading", None, None)
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
