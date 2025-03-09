import os
import shutil

from markdown_blocks import markdown_to_html_node




def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    markdown_content = get_text_from_file(from_path)
    template = get_text_from_file(template_path)
    html_content = use_template(template, markdown_content)

    ensure_dir_exists(os.path.dirname(dest_path))
    with open(dest_path, 'w') as f:
        f.write(html_content)

def ensure_dir_exists(dest_dir_path):
    os.makedirs(dest_dir_path, exist_ok=True)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isfile(dir_path_content)and dir_path_content.endswith('.md'):
        dest_path_html = os.path.splitext(dest_dir_path)[0] + '.html'
        generate_page(dir_path_content, template_path, dest_path_html)

    elif os.path.isdir(dir_path_content):
        ensure_dir_exists(dest_dir_path)
        for dir in os.listdir(dir_path_content):
            child_path = os.path.join(dir_path_content, dir)
            generate_pages_recursive(child_path, template_path, os.path.join(dest_dir_path, dir))
    else:
        raise Exception(f"Invalid path: {dir_path_content}")

def extract_title(markdown):
    if "#" in markdown:
        return markdown.strip().split("\n")[0].strip('#').strip()
    else:
        raise Exception("missing header")

def get_text_from_file(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text

def use_template(template, content):
    html_content = markdown_to_html_node(content).to_html()
    useable_template = template.replace("{{ Title }}", extract_title(content))
    useable_template = useable_template.replace("{{ Content }}", html_content) 
    return useable_template


