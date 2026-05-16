"""
Series of functions to handle markdown formatting for HTML conversion
"""

from enum import Enum

from parentnode import ParentNode
from textmodules import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


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
    Takes multiline markdown text and returns a list of individual blocks
    """
    blocks = []
    lines = markdown_text.split("\n\n")
    for line in lines:
        stripped = line.strip()
        no_spaces = stripped.replace("    ", "")
        if no_spaces != "":
            blocks.append(no_spaces)
    return blocks


def block_to_block_type(block):

    match block[0]:
        case "#":
            if block[1] == "#" or block[1] == " ":
                return BlockType.HEADING
            else:
                return BlockType.PARAGRAPH
        case "`":
            if block[1:4] == "``\n" and block.endswith("\n```"):
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


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children


def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for md_block in markdown_blocks:
        block_type = block_to_block_type(md_block)
        match block_type:
            case BlockType.HEADING:
                heading_num = md_block[0:6].count("#")
                html_node = ParentNode(
                    f"h{heading_num}", text_to_children(md_block[heading_num + 1 :])
                )
            case BlockType.QUOTE:
                if md_block[1] == " ":
                    html_node = ParentNode(
                        "blockquote", text_to_children(md_block[2:].replace("\n", " "))
                    )
                else:
                    html_node = ParentNode(
                        "blockquote", text_to_children(md_block[1:].replace("\n", " "))
                    )
            case BlockType.UNORDERED_LIST:
                list_items = md_block.split("\n")
                li_parent_nodes = []
                for item in list_items:
                    li_parent_nodes.append(ParentNode("li", text_to_children(item[2:])))
                html_node = ParentNode("ul", li_parent_nodes)
            case BlockType.ORDERED_LIST:
                list_items = md_block.split("\n")
                li_parent_nodes = []
                for item in list_items:
                    li_parent_nodes.append(ParentNode("li", text_to_children(item[3:])))
                html_node = ParentNode("ol", li_parent_nodes)
            case BlockType.PARAGRAPH:
                html_node = ParentNode(
                    "p", text_to_children(md_block.replace("\n", " "))
                )
            case BlockType.CODE:
                code_node = TextNode(md_block.replace("```", "")[1:], TextType.CODE)
                html_node = ParentNode("pre", [text_node_to_html_node(code_node)])

        html_nodes.append(html_node)
    return ParentNode("div", html_nodes)
