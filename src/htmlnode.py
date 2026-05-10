"""
HTML Class for nodes to create HTML tags 
"""


class HTMLNode:
    """
    Class of HTMLNodes. 
    """

    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        init method for HTMLNodes. Has all optional attributes:
        tag: HTML tag type (<p>, <h1>, <a>, etc.)
        value: Content to be placed within the HTML tag
        children: A list of children HTMLNodes to this node
        props: A dictionary of key-value pairs representing the attributes for the HTML tag. {"href":"some/link/url"}
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """
        Method to be overwritten by extended classes 
        """
        raise NotImplementedError("The 'to_html' method is not implemented. Must be used with extended LeafNode class")

    def props_to_html(self):
        """
        format HTMLNode.props into standard string. 
        """
        formatted_props = ""
        if self.props is None or self.props == {}:
            return ""
        for key, value in self.props.items():
            formatted_props += f"{key}=\"{value}\" "

        return formatted_props[:-1]

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
