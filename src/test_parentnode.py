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
    # Test ParentNode init

    def test_parentnode_p_none_none(self):
        """
        Test ParentNode init with p tag and no children nor props
        """
        parent_node_p = ParentNode("p", None, None)
        self.assertEqual(parent_node_p.tag, "p")
        self.assertEqual(parent_node_p.children, None)
        self.assertEqual(parent_node_p.props, None)

    def test_parentnode_a_none_url(self):
        """
        Test ParentNode init with <a> tag and no children but href prop
        """
        parent_node_a = ParentNode("a", None, {"href": "justalink"})
        self.assertEqual(parent_node_a.tag, "a")
        self.assertEqual(parent_node_a.children, None)
        self.assertEqual(parent_node_a.props_to_html(), "href=\"justalink\"")

    def test_parentnode_div_p_none(self):
        """
        Test ParentNode init with div tag and a p child node without props
        """
        inner_node = LeafNode("p", "this goes in the div")
        parent_node_p = ParentNode("div", [inner_node], None)
        self.assertEqual(parent_node_p.tag, "div")
        self.assertIsNotNone(parent_node_p.children)
        self.assertEqual(parent_node_p.props, None)

    # Test ParentNode to_html method
    def test_to_html_p(self):
        pass

    def test_to_html_a(self):
        pass

    def test_to_html_with_multi_children(self):
        """
        test ParentNode to_html method with four children. 
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
        self.assertEqual(node.to_html(
        ), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_six_children(self):
        """
        Test ParentNode to_html method with six children and duplicate <div> tags at start and end
        """
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
        self.assertEqual(node2.to_html(
        ), "<div><div>This is div</div>Normal text<i>italic text</i><p>paragraph text</p><p>paragraph text</p><div>Another div</div></div>")

    def test_to_html_with_children(self):
        """
        Test ParentNode to_html with assigned child_node
        """
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        """
        Test ParentNode to_html with assigned child and grandchild nodes
        """
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_deep_tree(self):
        "Test to_html method for Parentnode with four levels of ParentNode children and LeafNode as the innermost"
        deepest_child = LeafNode("p", "the innermost child")
        middling_child = ParentNode("b", [deepest_child])
        penultimate_child = ParentNode("span", [middling_child])
        eldest_child = ParentNode("div", [penultimate_child])
        deep_parent = ParentNode("div", [eldest_child])
        self.assertEqual(deep_parent.to_html(
        ), "<div><div><span><b><p>the innermost child</p></b></span></div></div>")

    def test_to_html_deep_wide_tree(self):
        """
        Test to_html method for ParentNode with ParentNode children and LeafNodes as their children
        """
        deep_child01 = LeafNode("p", "family 1 child")
        deep_child11 = LeafNode("b", "Bolder family 1 child")
        deep_child21 = LeafNode("code", "Family 1 coder")
        family1_parent = ParentNode(
            "div", [deep_child01, deep_child11, deep_child21])
        deep_child02 = LeafNode("h1", "family 2 header")
        deep_child12 = LeafNode("a", "Family 2 linker", {
                                "href": "family/2/tree"})
        family2_parent = ParentNode("span", [deep_child02, deep_child12])
        grandpa = ParentNode("div", [family1_parent, family2_parent])
        self.assertEqual(grandpa.to_html(
        ), "<div><div><p>family 1 child</p><b>Bolder family 1 child</b><code>Family 1 coder</code></div><span><h1>family 2 header</h1><a href=\"family/2/tree\">Family 2 linker</a></span></div>")

    # Test excepction expectations for ParentNode to_html method
    def test_childless_parentnode_to_html(self):
        """
        Test ParentNode to_html with children=None
        """
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_tagless_parentnode_to_html(self):
        """
        Test ParentNode to_html with tag=None
        """

        with self.assertRaises(ValueError):
            child_node = LeafNode("p", "family child")
            ParentNode(None, [child_node]).to_html()


if __name__ == "__main__":
    unittest.main()
