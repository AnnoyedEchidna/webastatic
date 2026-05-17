"""
Main! You should know what main is.
"""

import os
import shutil

from markdownmodules import extract_title, markdown_to_html_node


def main():

    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_directory("static", "public")

    generate_page("content/index.md", "template.html", "public/index.html")


def generate_page(from_path, template_path, to_path):
    """
    Takes a path of .md file to generate page content,
    the template file of the .html,
    and the path to where to save the new .html file
    then saves the new HTML file to that path.
    """
    print(f"Generating page from {from_path} to {to_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as t:
        html = t.read()

    index_html = html.replace(
        "{{ Content }}", markdown_to_html_node(markdown).to_html()
    ).replace("{{ Title }}", extract_title(markdown))

    if not os.path.exists(to_path.split("/")[0]):
        os.mkdir(to_path)
    with open(to_path, "w") as i:
        i.write(index_html)


def copy_directory(src_path, to_path):
    if os.path.isdir(src_path):
        if not os.path.exists(to_path):
            os.mkdir(to_path)
        paths = os.listdir(src_path)
        for r_path in paths:
            joined_path = os.path.join(src_path, r_path)
            path_root = src_path.split("/")[0]
            dest_path = joined_path.replace(path_root, to_path)
            if os.path.isdir(joined_path):
                print(f"creating {dest_path}")
                if not os.path.exists(dest_path):
                    os.mkdir(dest_path)
                copy_directory(joined_path, to_path)
            elif os.path.isfile(joined_path):
                print(f"copying {joined_path} to {dest_path}")
                shutil.copy(joined_path, dest_path)

        return
    print(f"{src_path} is not a directory")


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
