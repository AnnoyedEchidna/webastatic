"""
Create Enum class for the six different types of text for markup.
"""

from enum import Enum


class TextType(Enum):
    """
    TextType class extends Enum for types of text used in markup.
    """
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
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
