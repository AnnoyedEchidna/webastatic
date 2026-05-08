"""
HTMLNode Class tests for equality and disequality.  
"""
import unittest


from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    """
    HTMLNode class tests
    """

    def test_props_to_html(self):
        """
        test props_to_html method. 
        """
        # Test single prop
        node = HTMLNode("a", "This is a link", None, {
                        "href": "https://localhost:8888"})
        node_solution = "href=\"https://localhost:8888\""
        self.assertEqual(node.props_to_html(), node_solution)

        # Test dual props
        node2 = HTMLNode("a", "This is a link", None, {
            "href": "https://localhost:8888", "target": "_blank"})
        node2_solution = "href=\"https://localhost:8888\" target=\"_blank\""
        self.assertEqual(node2.props_to_html(), node2_solution)

        # Test props = None
        node3 = HTMLNode("p", "This is a paragraph", None, None)
        node3_solution = ""
        self.assertEqual(node3.props_to_html(), node3_solution)
