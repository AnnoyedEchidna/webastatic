"""
This is the ParentNode class. This class will handle nesting HTML nodes inside one another.
"""

from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    """
    This is the ParentNode class.
    """
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode tag cannot be None")
        if self.children is None:
            raise ValueError("ParentNode cannot be childless")
        if self.props is not None:
            html_tag = f"<{self.tag} {self.props_to_html()}>"
            html_end_tag = f"</{self.tag}>"
        else:
            html_tag = f"<{self.tag}>"
            html_end_tag = f"</{self.tag}>"

        parent_to_html_str = f"{html_tag}"
        for child in self.children:
            parent_to_html_str += child.to_html()

        parent_to_html_str += html_end_tag
        return parent_to_html_str