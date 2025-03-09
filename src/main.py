from page_generator import generate_pages_recursive, generate_page

from textnode import *
from markdown import *
from htmlnode import *

import os
import shutil
import sys

def setup():
    if len(sys.argv) == 1 :
        basepath = "/"
    else : 
        basepath = sys.argv[1]
    return basepath


def main():
    basepath = setup()
    print(basepath)
    copy_and_overwrite("./static", "./docs")
    from_dir = "./content"
    template_path = "./template.html"
    dest_dir = "./docs"
    generate_pages_recursive(basepath, from_dir,template_path,dest_dir)

def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

main()