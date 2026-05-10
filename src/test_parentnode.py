"""
Unit tests for ParentNode class
"""

import unittest


from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    """
    ParentNode class tests
    """

    def test_to_html_with_multi_children(self):
        """
        test ParentNode to_html method. 
        """
        
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

        node2 = ParentNode(
            "div",
            [
                LeafNode("div", "This is div"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode("p", "paragraph text"),
                LeafNode("p", "paragraph text"),
                LeafNode("div", "Another div"),
            ],
        )
        self.assertEqual(node2.to_html(), "<div><div>This is div</div>Normal text<i>italic text</i><p>paragraph text</p><p>paragraph text</p><div>Another div</div></div>")

        def test_to_html_with_children(self):
            child_node = LeafNode("span", "child")
            parent_node = ParentNode("div", [child_node])
            self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

        def test_to_html_with_grandchildren(self):
            grandchild_node = LeafNode("b", "grandchild")
            child_node = ParentNode("span", [grandchild_node])
            parent_node = ParentNode("div", [child_node])
            self.assertEqual(
                parent_node.to_html(),
                "<div><span><b>grandchild</b></span></div>",
            )

        