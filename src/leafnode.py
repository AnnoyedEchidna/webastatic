"""
This is the LeafNode class. This extends HTMLNode
does not allow for children
val and tag required.
"""

from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    """
    Leafnode class. Child of HTMLNode class, but does not allow for children
    """

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        """
        returns LeafNode in an HTML format
        """
        if self.value is None:
            raise ValueError("node must have value")
        if self.tag is None:
            return self.value
        if self.props is not None:
            html_tag = f"<{self.tag} {self.props_to_html()}>"
            html_end_tag = f"</{self.tag}>"
        else:
            html_tag = f"<{self.tag}>"
            html_end_tag = f"</{self.tag}>"
        return f"{html_tag}{self.value}{html_end_tag}"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props_to_html()})"
