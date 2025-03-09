from page_generator import generate_pages_recursive, generate_page

from textnode import *
from markdown import *
from htmlnode import *

import os
import shutil



def main():
    copy_and_overwrite("./static", "./public")
    from_dir = "./content"
    template_path = "./template.html"
    dest_dir = "./public"
    generate_pages_recursive(from_dir,template_path,dest_dir)

def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

main()