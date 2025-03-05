import os
import shutil

from markdown_blocks import markdown_to_html_node




def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    markdown_content = get_text_from_file(from_path)
    template = get_text_from_file(template_path)

    # from_file = open(from_path)
    # text = from_file.read()
    # from_file.close()
    # tmp_file = open(template_path)
    # tmp = tmp_file.read()
    # tmp_file.close()

    # html_string = markdown_to_html_node(text).to_html()
    # extract_title(text)
    # tmp = tmp.replace("{{ Title }}", extract_title(text))
    # tmp = tmp.replace("{{ Content }}", html_string)

    html_content = use_template(template, markdown_content)

    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    

    open(dest_path, 'x').write(html_content)

def extract_title(markdown):
    if "#" in markdown:
        return markdown.strip().split("\n")[0].strip('#').strip()
    else:
        raise Exception("missing header")

def get_text_from_file(path):
    file = open(path)
    text = file.read()
    file.close()
    return text

def use_template(template, content):
    html_content = markdown_to_html_node(content).to_html()
    useable_template = template.replace("{{ Title }}", extract_title(content))
    useable_template = useable_template.replace("{{ Content }}", html_content) 
    return useable_template


