"""
Create Enum class for the six different types of text for markup.
"""

from enum import Enum
from leafnode import LeafNode


class TextType(Enum):
    """
    TextType class extends Enum for types of text used in markup.
    """
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    """
    TextNode class for the actual objects containing the text
    """

    def __init__(self, text, text_type="plain", url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    """
    This method takes a TextNode object and returns 
    LeafNode based on the obj.text_type and text atts.
    """
    match text_node.text_type:
        case TextType.PLAIN:
            return LeafNode(None, text_node.text, None)
        case TextType.BOLD:
            return LeafNode("b", text_node.text, None)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text, None)
        case TextType.CODE:
            return LeafNode("code", text_node.text, None)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("Invalid or missing text type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Takes a list of TextNodes with in-line markdown text_type delimiters
    and breaks them into a list of TextNodes with proper text_types
    """
    if old_nodes is None or old_nodes == []:
        raise ValueError("no nodes to split on delimiter")
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.PLAIN:
            new_nodes.append(node)
            continue

        first_node_delimited = 0
        # check if first character of text is delimiter
        if node.text[0] == delimiter:
            first_node_delimited = 1

        split_nodes = node.text.split(delimiter)
        # check if split nodes is odd; if even, at least one delimiter did not close
        if len(split_nodes) % 2 == 0:
            raise ValueError("no closing delimiter found")
    # TODO: FIX THIS LOOP
        for idx in range(first_node_delimited, len(split_nodes), 2):
            print(idx)
            new_nodes.append(TextNode(split_nodes[idx]))
            new_nodes.append(TextNode(split_nodes[idx+1], text_type))
            new_nodes.append(TextNode(split_nodes[2]))

    return new_nodes
