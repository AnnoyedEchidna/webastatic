"""
Main! You should know what main is.
"""
from textnode import TextNode


def main():
    """
    main.py definition
    """
    dummy_text_node = TextNode(
        "Here is some anchor text", "link", "https://localhost:8000")
    print(dummy_text_node)


if __name__ == "__main__":
    main()
