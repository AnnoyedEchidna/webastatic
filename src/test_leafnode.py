"""
Unit tests for LeafNode class tests for to_html method.  
"""

import unittest


from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    """
    LeafNode class tests
    """

    # TEST LeafNode init method
    def test_leafnode_init_p(self):
        """
        Test LeafNode init with p tag and plain text
        """
        node = LeafNode("p", "This is a p text")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a p text")

    def test_leafnode_init_h1(self):
        """
        Test LeafNode init with h1 tag and plain text
        """
        node = LeafNode("h1", "This is a heading text")
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "This is a heading text")

    # TEST LeafNode.to_html() method
    def test_to_html(self):
        """
        Test to_html method with a link and one prop 
        """
        node = LeafNode("a", "This is a link", {
                        "href": "https://localhost:8888"})
        self.assertEqual(
            node.to_html(), "<a href=\"https://localhost:8888\">This is a link</a>")

    def test_to_html_p(self):
        """
        Test to_html with p tag no props
        """
        node2 = LeafNode("p", "Here is just some p text.")
        self.assertEqual(node2.to_html(), "<p>Here is just some p text.</p>")

    def test_to_html_h1(self):
        """
        Test to_html with h1 tag no props
        """
        node3 = LeafNode("h1", "THIS IS A HEADING!", None)
        self.assertEqual(node3.to_html(), "<h1>THIS IS A HEADING!</h1>")

    def test_to_html_img(self):
        """
        Test to_html with imgage tag two props
        """
        node3 = LeafNode(
            "img", "", {"src": "src/images/favicon.ico", "alt": "This is img alt text"})
        self.assertEqual(node3.to_html(
        ), "<img src=\"src/images/favicon.ico\" alt=\"This is img alt text\"></img>")

    def test_to_html_no_tag(self):
        """
        Test to_html method without explicit tag expecting no tag on return
        """
        node = LeafNode(None, "This is normal text")
        self.assertEqual(node.to_html(), "This is normal text")


if __name__ == "__main__":
    unittest.main()
