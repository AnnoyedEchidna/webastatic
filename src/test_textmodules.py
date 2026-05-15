"""
TextNode Class tests for equality and disequality.
"""

import unittest

from textmodules import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_images,
    split_nodes_links,
    text_to_textnodes,
)
from textnode import TextNode, TextType


class TestTextModule(unittest.TestCase):
    """
    TextModules functions tests
    """

    # Test split_node_delimiter function

    def test_split_nodes_delimiter_bold(self):
        """
        Test split_nodes_delimiter method with bold delimiters
        """
        old_node = TextNode("This will be **bold** text")
        new_nodes = split_nodes_delimiter([old_node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text, "This will be ")
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[2].text, " text")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_first_node_italic(self):
        """
        Test split_nodes_delimiter method with italic delimiters with first node delimited
        """
        another_node = TextNode("_All_ together now!")
        more_new_nodes = split_nodes_delimiter([another_node], "_", TextType.ITALIC)
        self.assertEqual(more_new_nodes[0].text, "All")
        self.assertEqual(more_new_nodes[1].text, " together now!")
        self.assertEqual(more_new_nodes[0].text_type, TextType.ITALIC)
        self.assertEqual(more_new_nodes[1].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_last_node_italic(self):
        """
        Test split_nodes_delimiter method with italic delimiters with last node delimited
        """
        another_node = TextNode("All together _now!_")
        more_new_nodes = split_nodes_delimiter([another_node], "_", TextType.ITALIC)
        self.assertEqual(more_new_nodes[0].text, "All together ")
        self.assertEqual(more_new_nodes[1].text, "now!")
        self.assertEqual(more_new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(more_new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(len(more_new_nodes), 2)

    def test_split_nodes_delimiter_not_text_input(self):
        """
        Test split_nodes_delimiter method with italic delimiters but bold text_type
        """
        non_text_text_node = TextNode("This is already _bold_", TextType.BOLD)
        one_new_node = split_nodes_delimiter([non_text_text_node], "_", TextType.ITALIC)
        self.assertEqual(one_new_node[0].text, "This is already _bold_")
        self.assertEqual(one_new_node[0].text_type, TextType.BOLD)
        self.assertEqual(len(one_new_node), 1)

    def test_split_nodes_delimiter_double_bold(self):
        """
        Test split_nodes_delimiter method with two bold delimiters
        """
        double_delimiter = TextNode("This text is **bold** but this is **bolder**")
        double_delim_split = split_nodes_delimiter(
            [double_delimiter], "**", TextType.BOLD
        )
        self.assertEqual(double_delim_split[0].text, "This text is ")
        self.assertEqual(double_delim_split[1].text, "bold")
        self.assertEqual(double_delim_split[2].text, " but this is ")
        self.assertEqual(double_delim_split[3].text, "bolder")
        self.assertEqual(double_delim_split[0].text_type, TextType.TEXT)
        self.assertEqual(double_delim_split[1].text_type, TextType.BOLD)
        self.assertEqual(double_delim_split[2].text_type, TextType.TEXT)
        self.assertEqual(double_delim_split[3].text_type, TextType.BOLD)

    def test_split_nodes_delimiter_unmatched_delimiter(self):
        """
        Test split_nodes_delimiter method with one missing bold delimiter
        """
        broken_delimiter = TextNode("There is only one **delimeter for this one")
        with self.assertRaises(ValueError):
            split_nodes_delimiter([broken_delimiter], "**", TextType.BOLD)

    def test_split_nodes_delimiter_no_delimiter(self):
        """
        Test split_nodes_delimiter without passing any delimiters in the input string.
        """
        text_to_text = TextNode("This is entirely text text", TextType.TEXT)
        text_no_split = split_nodes_delimiter([text_to_text], "**", TextType.BOLD)
        self.assertEqual(text_no_split[0].text, "This is entirely text text")
        self.assertEqual(text_no_split[0].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_empty_list(self):
        """
        Test split_nodes_delimiter method with empty input list
        """
        with self.assertRaises(ValueError):
            split_nodes_delimiter([], "**", TextType.BOLD)

    # Test extract_markdown_images
    def test_extract_single_markdown_image(self):
        """
        Test extract_markdown_images function using inital example given in lesson
        """
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(
            extract_markdown_images(text),
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif")],
        )

    def test_extract_dual_markdown_images(self):
        """
        Test extract_markdown_images function using dual example given in lesson
        """
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
        )

    def test_extract_no_markdown_images(self):
        """
        Test extract_markdown_images function passing no valid images
        """
        text = "This is just some boring ole text"
        self.assertEqual(extract_markdown_images(text), [])

    def test_extract_markdown_images_with_lnk(self):
        """
        Test extract_markdown_images function passing link instead of image
        """
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(extract_markdown_images(text), [])

    # Test extract_markdown_links
    def test_extract_single_markdown_link(self):
        """
        Test extract_markdown_links function using inital example given in lesson
        """
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(
            extract_markdown_links(text),
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif")],
        )

    def test_extract_dual_markdown_links(self):
        """
        Test extract_markdown_links function using inital example given in lesson
        """
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) along with some [hockey goals](this/path/to/hockey)"
        self.assertEqual(
            extract_markdown_links(text),
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("hockey goals", "this/path/to/hockey"),
            ],
        )

    def test_extract_no_markdown_links(self):
        """
        Test extract_markdown_links function using inital example given in lesson
        """
        text = "This is text with no links or images"
        self.assertEqual(extract_markdown_links(text), [])

    def test_extract_markdown_link_with_img(self):
        """
        Test extract_markdown_links function passing image instead of link
        """
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(extract_markdown_links(text), [])

    # TEST split_nodes_images method
    def test_split_nodes_images_no_input(self):
        """
        Test split_nodes_images while passing nothing intot the old nodes; expecting exception
        """
        with self.assertRaises(ValueError):
            split_nodes_images([])

    def test_split_nodes_images_no_text(self):
        """
        Test the split_nodes_images function passing single node with image and no surround text
        """
        text = "![no text img text](src/images/notext.png)"
        new_nodes = split_nodes_images([TextNode(text, TextType.TEXT)])
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "no text img text")
            self.assertEqual(new_nodes[0].text_type, TextType.IMAGE)
            self.assertEqual(new_nodes[0].url, "src/images/notext.png")
            with self.assertRaises(IndexError):
                new_nodes[1]

    def test_split_nodes_images_no_image(self):
        """
        Test the split_nodes_images function passing single node with image and no surround text
        """
        text = "This is just text with no pretty pictures"
        new_nodes = split_nodes_images([TextNode(text, TextType.TEXT)])
        if new_nodes is not None:
            self.assertEqual(
                new_nodes[0].text, "This is just text with no pretty pictures"
            )
            self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
            with self.assertRaises(IndexError):
                new_nodes[1]

    def test_split_nodes_images_with_text(self):
        """
        Test the split_nodes_images function passing single node with image and surrounding text
        """
        text = "This image shown includes things ![single img text](src/images/img1.png) and stuff around the image"
        new_nodes = split_nodes_images([TextNode(text, TextType.TEXT)])
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "This image shown includes things ")
            self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[1].text, "single img text")
            self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
            self.assertEqual(new_nodes[1].url, "src/images/img1.png")
            self.assertEqual(new_nodes[2].text, " and stuff around the image")
            self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
            with self.assertRaises(IndexError):
                new_nodes[3]

    def test_split_nodes_images_with_only_middle_text(self):
        """
        Test the split_nodes_images function passing single node with image and surrounding text
        """
        text = "![single img text](src/images/img1.png) and stuff between the images ![second image](src/image/numbertwo.ico)"
        new_nodes = split_nodes_images([TextNode(text, TextType.TEXT)])
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "single img text")
            self.assertEqual(new_nodes[0].text_type, TextType.IMAGE)
            self.assertEqual(new_nodes[0].url, "src/images/img1.png")
            self.assertEqual(new_nodes[1].text, " and stuff between the images ")
            self.assertEqual(new_nodes[1].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[2].text, "second image")
            self.assertEqual(new_nodes[2].text_type, TextType.IMAGE)
            self.assertEqual(new_nodes[2].url, "src/image/numbertwo.ico")
            with self.assertRaises(IndexError):
                new_nodes[3]

    def test_split_nodes_images_multi_image(self):
        """
        Test the split_nodes_images function passing single node with two images and surrounding text
        """
        text = "This image shown includes things ![multi img text](src/images/allthepics.png) and stuff around the image. This also includes ![more picture](src/images/other.png)"
        new_nodes = split_nodes_images([TextNode(text, TextType.TEXT)])
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "This image shown includes things ")
            self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[1].text, "multi img text")
            self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
            self.assertEqual(new_nodes[1].url, "src/images/allthepics.png")
            self.assertEqual(
                new_nodes[2].text, " and stuff around the image. This also includes "
            )
            self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[3].text, "more picture")
            self.assertEqual(new_nodes[3].text_type, TextType.IMAGE)
            self.assertEqual(new_nodes[3].url, "src/images/other.png")
            with self.assertRaises(IndexError):
                new_nodes[4]

    def test_split_nodes_images_multi_image_ending_text(self):
        """
        Test the split_nodes_images function passing single node with two images and surrounding text including ending text
        """
        text = "This image shown includes things ![multi img text](src/images/allthepics.png) and stuff around the image. This also includes ![more picture](src/images/other.png) and a closing to the statement"
        new_nodes = split_nodes_images([TextNode(text, TextType.TEXT)])
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "This image shown includes things ")
            self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[1].text, "multi img text")
            self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
            self.assertEqual(new_nodes[1].url, "src/images/allthepics.png")
            self.assertEqual(
                new_nodes[2].text, " and stuff around the image. This also includes "
            )
            self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[3].text, "more picture")
            self.assertEqual(new_nodes[3].text_type, TextType.IMAGE)
            self.assertEqual(new_nodes[3].url, "src/images/other.png")
            self.assertEqual(new_nodes[4].text, " and a closing to the statement")
            self.assertEqual(new_nodes[4].text_type, TextType.TEXT)
            with self.assertRaises(IndexError):
                new_nodes[5]

    def test_split_nodes_images_multi_text_node(self):
        """
        Test split_nodes_images function passing multiple TextNode objects
        """
        text1 = "Text text ![image desc](src/images/icons.ico)"
        text2 = "Other text ![image text](src/images/other.ico) finish text"
        text3 = "This is just text."
        new_nodes = split_nodes_images(
            [
                TextNode(text1, TextType.TEXT),
                TextNode(text2, TextType.TEXT),
                TextNode(text3, TextType.TEXT),
            ]
        )
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "Text text ")
            self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[1].text, "image desc")
            self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
            self.assertEqual(new_nodes[1].url, "src/images/icons.ico")
            self.assertEqual(new_nodes[2].text, "Other text ")
            self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[3].text, "image text")
            self.assertEqual(new_nodes[3].text_type, TextType.IMAGE)
            self.assertEqual(new_nodes[3].url, "src/images/other.ico")
            self.assertEqual(new_nodes[4].text, " finish text")
            self.assertEqual(new_nodes[4].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[5].text, "This is just text.")
            self.assertEqual(new_nodes[5].text_type, TextType.TEXT)
            with self.assertRaises(IndexError):
                new_nodes[6]

    def test_split_nodes_images_multi_just_text_node(self):
        """
        Test split_nodes_images function passing multiple TextNode objects but no images
        """
        text1 = "Text text"
        text2 = "Other text"
        text3 = "This is just text"
        new_nodes = split_nodes_images(
            [
                TextNode(text1, TextType.TEXT),
                TextNode(text2, TextType.TEXT),
                TextNode(text3, TextType.TEXT),
            ]
        )
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "Text text")
            self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[1].text, "Other text")
            self.assertEqual(new_nodes[1].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[2].text, "This is just text")
            self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
            with self.assertRaises(IndexError):
                new_nodes[3]

    def test_split_nodes_images_with_mixed_multi_text_node(self):
        """
        Test split_nodes_images function passing multiple TextNode objects
        """
        text1 = "Text text ![image desc](src/images/icons.ico)"
        text2 = "Other text [this is a link](link/path/to/target) finish text"
        text3 = "This is just text."
        new_nodes = split_nodes_images(
            [
                TextNode(text1, TextType.TEXT),
                TextNode(text2, TextType.TEXT),
                TextNode(text3, TextType.TEXT),
            ]
        )
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "Text text ")
            self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[1].text, "image desc")
            self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
            self.assertEqual(new_nodes[1].url, "src/images/icons.ico")
            self.assertEqual(
                new_nodes[2].text,
                "Other text [this is a link](link/path/to/target) finish text",
            )
            self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[3].text, "This is just text.")
            self.assertEqual(new_nodes[3].text_type, TextType.TEXT)
            with self.assertRaises(IndexError):
                new_nodes[4]

    # TEST split_nodes_links function
    def test_split_nodes_links_no_input(self):
        """
        Test split_nodes_links while passing nothing into the old nodes; expecting exception
        """
        with self.assertRaises(ValueError):
            split_nodes_links([])

    def test_split_nodes_links_no_text(self):
        """
        Test the split_nodes_links function passing single node with link and no surround text
        """
        text = "[no text link text](path/to/link/target)"
        new_nodes = split_nodes_links([TextNode(text, TextType.TEXT)])
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "no text link text")
            self.assertEqual(new_nodes[0].text_type, TextType.LINK)
            self.assertEqual(new_nodes[0].url, "path/to/link/target")
            with self.assertRaises(IndexError):
                new_nodes[1]

    def test_split_nodes_links_no_image(self):
        """
        Test the split_nodes_links function passing single node with link and no surround text
        """
        text = "This is just text with no fancy links"
        new_nodes = split_nodes_links([TextNode(text, TextType.TEXT)])
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "This is just text with no fancy links")
            self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
            with self.assertRaises(IndexError):
                new_nodes[1]

    def test_split_nodes_links_with_text(self):
        """
        Test the split_nodes_links function passing single node with link and surrounding text
        """
        text = "This link shown includes things [single link text](src/images/target) and stuff around the link"
        new_nodes = split_nodes_links([TextNode(text, TextType.TEXT)])
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "This link shown includes things ")
            self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[1].text, "single link text")
            self.assertEqual(new_nodes[1].text_type, TextType.LINK)
            self.assertEqual(new_nodes[1].url, "src/images/target")
            self.assertEqual(new_nodes[2].text, " and stuff around the link")
            self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
            with self.assertRaises(IndexError):
                new_nodes[3]

    def test_split_nodes_links_with_only_middle_text(self):
        """
        Test the split_nodes_links function passing single node with image and surrounding text
        """
        text = "[single link text](src/images/target) and stuff between the links [second link](src/image/target2)"
        new_nodes = split_nodes_links([TextNode(text, TextType.TEXT)])
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "single link text")
            self.assertEqual(new_nodes[0].text_type, TextType.LINK)
            self.assertEqual(new_nodes[0].url, "src/images/target")
            self.assertEqual(new_nodes[1].text, " and stuff between the links ")
            self.assertEqual(new_nodes[1].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[2].text, "second link")
            self.assertEqual(new_nodes[2].text_type, TextType.LINK)
            self.assertEqual(new_nodes[2].url, "src/image/target2")
            with self.assertRaises(IndexError):
                new_nodes[3]

    def test_split_nodes_links_multi_link(self):
        """
        Test the split_nodes_links function passing single node with two links and surrounding text
        """
        text = "This link shown includes things [multi link text](src/images/allthepics.png) and stuff around the link. This also includes [more link](src/images/other.png)"
        new_nodes = split_nodes_links([TextNode(text, TextType.TEXT)])
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "This link shown includes things ")
            self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[1].text, "multi link text")
            self.assertEqual(new_nodes[1].text_type, TextType.LINK)
            self.assertEqual(new_nodes[1].url, "src/images/allthepics.png")
            self.assertEqual(
                new_nodes[2].text, " and stuff around the link. This also includes "
            )
            self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[3].text, "more link")
            self.assertEqual(new_nodes[3].text_type, TextType.LINK)
            self.assertEqual(new_nodes[3].url, "src/images/other.png")
            with self.assertRaises(IndexError):
                new_nodes[4]

    def test_split_nodes_links_multi_image_ending_text(self):
        """
        Test the split_nodes_links function passing single node with two links and surrounding text including ending text
        """
        text = "This link shown includes things [multi link text](src/images/allthepics.png) and stuff around the link. This also includes [more link](src/images/other.png) and a closing to the statement"
        new_nodes = split_nodes_links([TextNode(text, TextType.TEXT)])
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "This link shown includes things ")
            self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[1].text, "multi link text")
            self.assertEqual(new_nodes[1].text_type, TextType.LINK)
            self.assertEqual(new_nodes[1].url, "src/images/allthepics.png")
            self.assertEqual(
                new_nodes[2].text, " and stuff around the link. This also includes "
            )
            self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[3].text, "more link")
            self.assertEqual(new_nodes[3].text_type, TextType.LINK)
            self.assertEqual(new_nodes[3].url, "src/images/other.png")
            self.assertEqual(new_nodes[4].text, " and a closing to the statement")
            self.assertEqual(new_nodes[4].text_type, TextType.TEXT)
            with self.assertRaises(IndexError):
                new_nodes[5]

    def test_split_nodes_links_multi_text_node(self):
        """
        Test split_nodes_links function passing multiple TextNode objects
        """
        text1 = "Text text [link desc](src/images/icons.ico)"
        text2 = "Other text [link text](src/images/other.ico) finish text"
        text3 = "This is just text."
        new_nodes = split_nodes_links(
            [
                TextNode(text1, TextType.TEXT),
                TextNode(text2, TextType.TEXT),
                TextNode(text3, TextType.TEXT),
            ]
        )
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "Text text ")
            self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[1].text, "link desc")
            self.assertEqual(new_nodes[1].text_type, TextType.LINK)
            self.assertEqual(new_nodes[1].url, "src/images/icons.ico")
            self.assertEqual(new_nodes[2].text, "Other text ")
            self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[3].text, "link text")
            self.assertEqual(new_nodes[3].text_type, TextType.LINK)
            self.assertEqual(new_nodes[3].url, "src/images/other.ico")
            self.assertEqual(new_nodes[4].text, " finish text")
            self.assertEqual(new_nodes[4].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[5].text, "This is just text.")
            self.assertEqual(new_nodes[5].text_type, TextType.TEXT)
            with self.assertRaises(IndexError):
                new_nodes[6]

    def test_split_nodes_links_multi_just_text_node(self):
        """
        Test split_nodes_links function passing multiple TextNode objects but no links
        """
        text1 = "Text text"
        text2 = "Other text"
        text3 = "This is just text"
        new_nodes = split_nodes_links(
            [
                TextNode(text1, TextType.TEXT),
                TextNode(text2, TextType.TEXT),
                TextNode(text3, TextType.TEXT),
            ]
        )
        if new_nodes is not None:
            self.assertEqual(new_nodes[0].text, "Text text")
            self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[1].text, "Other text")
            self.assertEqual(new_nodes[1].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[2].text, "This is just text")
            self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
            with self.assertRaises(IndexError):
                new_nodes[3]

    def test_split_nodes_links_with_mixed_multi_text_node(self):
        """
        Test split_nodes_links function passing multiple TextNode objects
        """
        text1 = "Text text ![image desc](src/images/icons.ico)"
        text2 = "Other text [this is a link](link/path/to/target) finish text"
        text3 = "This is just text."
        new_nodes = split_nodes_links(
            [
                TextNode(text1, TextType.TEXT),
                TextNode(text2, TextType.TEXT),
                TextNode(text3, TextType.TEXT),
            ]
        )
        if new_nodes is not None:
            self.assertEqual(
                new_nodes[0].text, "Text text ![image desc](src/images/icons.ico)"
            )
            self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[1].text, "Other text ")
            self.assertEqual(new_nodes[1].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[2].text, "this is a link")
            self.assertEqual(new_nodes[2].text_type, TextType.LINK)
            self.assertEqual(new_nodes[2].url, "link/path/to/target")
            self.assertEqual(new_nodes[3].text, " finish text")
            self.assertEqual(new_nodes[3].text_type, TextType.TEXT)
            self.assertEqual(new_nodes[4].text, "This is just text.")
            self.assertEqual(new_nodes[4].text_type, TextType.TEXT)
            with self.assertRaises(IndexError):
                new_nodes[5]

    def test_split_images_provided_test(self):
        """
        Test for split_nodes_images function provided by lesson
        """
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    # TEST text_to_textnodes function
    def test_text_to_textnodes(self):
        """
        Test text_to_textnodes function passing in given string from lesson.
        """
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes_list = text_to_textnodes(text)
        self.assertListEqual(
            nodes_list,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )

    def test_text_to_textnodes_all_link(self):
        """
        Test text_to_textnodes function passing in given string with only links. Including _ delimiter to test file_names.
        """
        text = "This is [a link](link/target/path) with [another link](link/other/target)[link three](more_links/link) and [link four](link/four/links)"
        nodes_list = text_to_textnodes(text)
        self.assertListEqual(
            nodes_list,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("a link", TextType.LINK, "link/target/path"),
                TextNode(" with ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "link/other/target"),
                TextNode("link three", TextType.LINK, "more_links/link"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link four", TextType.LINK, "link/four/links"),
            ],
        )

    def test_text_to_textnodes_all_text(self):
        """
        Test text_to_textnodes function passing in given string with only links. Including _ delimiter to test file_names.
        """
        text = "This is text with just more text and only text the whole way"
        nodes_list = text_to_textnodes(text)
        self.assertListEqual(
            nodes_list,
            [
                TextNode(
                    "This is text with just more text and only text the whole way",
                    TextType.TEXT,
                ),
            ],
        )

    def test_text_to_textnodes_links_and_images(self):
        """
        Test text_to_textnodes function passing given string of a link and images
        """
        text = "![image to start](src/starts/image.png)![image to follow](src/followers/follow.png)![just a picture](something/else)[link to everywhere](all/of/the/web)"
        nodes_list = text_to_textnodes(text)
        self.assertListEqual(
            nodes_list,
            [
                TextNode("image to start", TextType.IMAGE, "src/starts/image.png"),
                TextNode("image to follow", TextType.IMAGE, "src/followers/follow.png"),
                TextNode("just a picture", TextType.IMAGE, "something/else"),
                TextNode("link to everywhere", TextType.LINK, "all/of/the/web"),
            ],
        )

    def test_text_to_textnodes_italic_code_bold(self):
        """
        Test text_to_textnodes function with a string of italic, bold, and code text snippets
        """
        text = "**this text bolded** _and this is italics_ with just a `space` inbetween some."
        nodes_list = text_to_textnodes(text)
        self.assertListEqual(
            nodes_list,
            [
                TextNode("this text bolded", TextType.BOLD),
                TextNode(" ", TextType.TEXT),
                TextNode("and this is italics", TextType.ITALIC),
                TextNode(" with just a ", TextType.TEXT),
                TextNode("space", TextType.CODE),
                TextNode(" inbetween some.", TextType.TEXT),
            ],
        )

    def test_text_to_textnodes_blank(self):
        text = ""
        nodes_list = text_to_textnodes(text)
        self.assertEqual(nodes_list, [TextNode("", TextType.TEXT)])


if __name__ == "__main__":
    unittest.main()
