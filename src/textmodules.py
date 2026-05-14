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
        if node.text_type is not TextType.TEXT:
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


def split_nodes_images(old_nodes):
    if old_nodes is None or old_nodes == []:
        raise ValueError("no nodes to split images")
    new_nodes = []

    for node in old_nodes:
        # separate node text into text, image tag, text repeat
        # images info is a list of tuples of images. Will return all images in text
        images_info = extract_markdown_images(node.text)
        # if there are no images in the node, add the node to the new_nodes list as is.
        if images_info == []:
            new_nodes.append(node)
            continue

        working_text = node.text  # TEXT
        # TextNode(text, type, url) for image would be TextNode(alt=(img[0]), type.image, src=img[1])
        for image in images_info:
            img_removed = working_text.split(f"![{image[0]}]({image[1]})", 1)
            if img_removed[0] != "":
                new_nodes.append(TextNode(img_removed[0], node.text_type))
            new_nodes.append(TextNode(image[0], "image", image[1]))
            working_text = img_removed[-1]

        if working_text != "":
            new_nodes.append(TextNode(working_text, node.text_type))

    return new_nodes


def split_nodes_links(old_nodes):
    if old_nodes is None or old_nodes == []:
        raise ValueError("no nodes to split images")
    new_nodes = []

    for node in old_nodes:
        # separate node text into text, image tag, text repeat
        # images info is a list of tuples of images. Will return all images in text
        links_info = extract_markdown_links(node.text)
        # if there are no images in the node, add the node to the new_nodes list as is.
        if links_info == []:
            new_nodes.append(node)
            continue

        working_text = node.text  # TEXT
        # TextNode(text, type, url) for image would be TextNode(alt=(img[0]), type.image, src=img[1])
        for link in links_info:
            link_removed = working_text.split(f"[{link[0]}]({link[1]})", 1)
            if link_removed[0] != "":
                new_nodes.append(TextNode(link_removed[0], node.text_type))
            new_nodes.append(TextNode(link[0], "link", link[1]))
            working_text = link_removed[-1]

        if working_text != "":
            new_nodes.append(TextNode(working_text, node.text_type))

    return new_nodes
