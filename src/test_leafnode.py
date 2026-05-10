"""
Unti tests for LeafNode class tests for to_html method.  
"""
import unittest


from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    """
    LeafNode class tests
    """

    def test_to_html(self):
        """
        test to_html method. 
        """
        # Test single prop
        node = LeafNode("a", "This is a link",{"href": "https://localhost:8888"})
        self.assertEqual(node.to_html(), "<a href=\"https://localhost:8888\">This is a link</a>")

        node2 = LeafNode("p", "Here is just some p text.")
        self.assertEqual(node2.to_html(), "<p>Here is just some p text.</p>")

        node3 = LeafNode("h1", "THIS IS A HEADING!", None)
        self.assertEqual(node3.to_html(), "<h1>THIS IS A HEADING!</h1>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is normal text")
        self.assertEqual(node.to_html(), "This is normal text")
        