"""
Main! You should know what main is.
"""

import os
import shutil
import sys

from page_modules import copy_directory, generate_page_recursive


def main():

    if os.path.exists("docs"):
        shutil.rmtree("docs")
    copy_directory("static", "docs")

    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(sys.argv)
    generate_page_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()
