"""
Series of functions to handle markdown formatting for HTML conversion
"""

from enum import Enum


class BlockType(Enum):
    """
    BlockType extends Enum to standardize block_types
    """

    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unorderd_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown_text):
    """
    Takes multiline markdown text and returns a list of individual lines
    """
    block = []
    lines = markdown_text.split("\n\n")
    for line in lines:
        stripped = line.strip()
        no_spaces = stripped.replace("    ", "")
        if no_spaces != "":
            block.append(no_spaces)
    return block


def block_to_block_type(block):

    match block[0]:
        case "#":
            if block[1] == "#" or block[1] == " ":
                return BlockType.HEADING
            else:
                return BlockType.PARAGRAPH
        case "`":
            if block[1:4] == "``\n" and block.endswith("```"):
                return BlockType.CODE
            else:
                return BlockType.PARAGRAPH
        case ">":
            return BlockType.QUOTE
        case "-":
            if block[1] == " ":
                return BlockType.UNORDERED_LIST
            else:
                return BlockType.PARAGRAPH
        case "1":
            if block[1] == ".":
                return BlockType.ORDERED_LIST
            else:
                return BlockType.PARAGRAPH
        case _:
            return BlockType.PARAGRAPH
