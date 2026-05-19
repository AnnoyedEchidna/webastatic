"""
Main! You should know what main is.
"""

import os
import shutil
import sys

from page_modules import copy_directory, generate_page_recursive


def main():

    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_directory("static", "public")

    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(sys.argv)
    # generate_page_recursive(basepath, "template.html", "public")


if __name__ == "__main__":
    main()
