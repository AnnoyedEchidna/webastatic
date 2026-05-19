"""
Main! You should know what main is.
"""

import os
import shutil

from page_modules import copy_directory, generate_page, generate_page_recursive


def main():

    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_directory("static", "public")

    generate_page_recursive("content", "template.html", "public")

    #
    # generate_page("content/index.md", "template.html", "public/index.html")
    # generate_page(
    #     "content/blog/glorfindel/index.md",
    #     "template.html",
    #     "public/blog/glorfindel/index.html",
    # )
    # generate_page(
    #     "content/blog/majesty/index.md",
    #     "template.html",
    #     "public/blog/majesty/index.html",
    # )
    # generate_page(
    #     "content/blog/tom/index.md", "template.html", "public/blog/tom/index.html"
    # )
    # generate_page(
    #     "content/contact/index.md",
    #     "template.html",
    #     "public/contact/index.html",
    # )


def test():
    # """
    #     main.py definition
    #     """
    #     dummy_text_node = markdown_to_html_node(
    #         """ # Lost on the Interwebs

    # Oh **look**! We have found a link!
    # I wonder where it goes...
    # [Here is some anchor text](https://localhost:8000)

    # ## In a weird place never before seen

    # _Somewhere between webpages on localhost_ Where are we? This doesn't feel like the **internet**.
    # What are you talking about? You have to review the field manual.

    # > To access previously visited webpages, please click the back button on your mouse.
    # > If this has no affect, consider the following:

    # - Ctrl+W
    # - Alt+F4
    # - Pressing the power button on the front of your computer

    # 1. Restarting the system
    # 2. Try entering a command with sudo
    # 3. Finding inner peace and remaining where you are until rescue arrives

    # ```
    # Press(Ctrl+W)
    # rerun
    # ```

    # #### Back on the desktop

    # _Back upon a hill somewhere much like this:_
    # ![grassy knoll with wildflowers](src/link/to/hill.png)
    # _Our adventurers find themselves confused but relieved_
    # I'm so glad we're back on this hill! It's been too long on the internet
    # """
    #     ).to_html()
    #     print(dummy_text_node)
    pass


if __name__ == "__main__":
    main()
