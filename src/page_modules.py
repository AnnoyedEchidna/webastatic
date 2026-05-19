"""
This is a series of modules for filehandling and page generation
"""

import os
import shutil

from markdownmodules import extract_title, markdown_to_html_node


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    for inner_path in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, inner_path)
        print(f"inner path: {content_path}")
        if os.path.isdir(content_path):
            deeper_dest_path = os.path.join(dest_dir_path, inner_path)
            if not os.path.exists(deeper_dest_path):
                print(f"making dir: {deeper_dest_path}")
                os.mkdir(deeper_dest_path)
            generate_page_recursive(content_path, template_path, deeper_dest_path)
        elif os.path.isfile(content_path):
            if content_path[-3:] == ".md":
                print(f"is file: {content_path}")
                with open(content_path, "r") as f:
                    markdown = f.read()
                with open(template_path, "r") as t:
                    html = t.read()

                index_html = html.replace(
                    "{{ Content }}", markdown_to_html_node(markdown).to_html()
                ).replace("{{ Title }}", extract_title(markdown))

                print(f"writing file: {dest_dir_path + 'index.html'}")
                with open(dest_dir_path + "/index.html", "w") as i:
                    i.write(index_html)


def generate_page(from_path, template_path, to_path):
    """
    Takes a path of .md file to generate page content,
    the template file of the .html,
    and the path to where to save the new .html file
    then saves the new HTML file to that path.
    """
    print("=================================")
    print(f"Generating page from {from_path} to {to_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as t:
        html = t.read()

    index_html = html.replace(
        "{{ Content }}", markdown_to_html_node(markdown).to_html()
    ).replace("{{ Title }}", extract_title(markdown))

    split_to_path = to_path.split("/")
    combo_to_path = ""
    for idx, dir in enumerate(split_to_path):
        combo_to_path = os.path.join(combo_to_path, dir)
        print(f"combo dir: {combo_to_path}")
        if idx == len(split_to_path) - 1:
            print(f"End of the filename: {dir}")
            continue
        if not os.path.exists(combo_to_path):
            os.mkdir(combo_to_path)
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
