"""
Various functions for manipulating text inputs
"""

import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Takes a list of TextNodes with in-line markdown text_type delimiters
    and breaks them into a list of TextNodes with proper text_types
    """
    if old_nodes is None or old_nodes == []:
        raise ValueError("no nodes to split on delimiter")
    new_nodes = []
    for node in old_nodes:
        # Only want to check for delimiters on plain text. If not plain text, skip node and continue
        if node.text_type is not TextType.PLAIN:
            new_nodes.append(node)
            continue

        split_nodes = node.text.split(delimiter)
        # If splitting yeilds no additional strings, no change needed
        if len(split_nodes) == 1:
            new_nodes.append(node)
            continue

        # check if split nodes is odd; if even, at least one delimiter did not close
        if len(split_nodes) % 2 == 0:
            raise ValueError("no closing delimiter found")

        # Split nodes always gives an odd number of nodes, even when starts with delimiter.
        for idx, node_text in enumerate(split_nodes):
            # If the old_node starts or ends with delimited string, gives an empty string to skip
            if len(node_text) == 0:
                continue
            # Only odd nodes should be set to different text_type; append originals as is if even
            if idx % 2 == 0:
                new_nodes.append(TextNode(node_text))
            else:
                new_nodes.append(TextNode(node_text, text_type))

    return new_nodes


def extract_markdown_images(text):
    """
    Takes a string of text and uses regex to extract the src and alt attributes and returns tuple (src, alt)
    """
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    """
    Takes a string of text and uses regex to extract the href and link text attributes and returns tuple (href, link)
    """
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches


# TODO: Fix this mess
def split_nodes_images(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # separate node text into text, image tag, text repeat
        non_image_text = []
        # images info is a list of tuples of images. Will return all images in text
        images_info = extract_markdown_images(node.text)
        # if there are no images in the node, add the node to the new_nodes list as is.
        if images_info == []:
            new_nodes.append(node)
            continue

        # TextNode(text, type, url) for image would be TextNode(alt=(img[0]), type.image, src=img[1])
        # Do we want two lists that come back and we iterate over both? HMMMM
        for image in images_info:
            img_removed_split = node.text.split(f"![{image[0]}]({image[1]})", 1)
            print(non_image_text)
            # print(
            #     f"{img_removed_split}, len post split: {len(img_removed_split)} len images:{len(images_info)}"
            # )
            # new_nodes.append(broken_nodes)
    pass


def split_nodes_links(old_nodes):
    pass
