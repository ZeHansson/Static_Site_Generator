from page_generator import generate_page

import os
import shutil

#print("hello world")

def main():
    #test_txt_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    #print(test_txt_node)
    #prop = {"href": "https://www.google.com","target": "_blank",}
    #htmlnode = HTMLNode( None,None ,None , prop )
    #print(htmlnode)
    #node = LeafNode("p", "This is a paragraph of text.")
    #node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    #print(node.to_html())
    #print(node2.to_html())
    #print(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"))
    #print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"))
    #node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT,)
    #print(split_nodes_link([node]))
    
    #nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
    #for node in nodes:
    #    print(node)
    #print(nodes)
    

    #copy_and_overwrite("static", "public")

    
    copy_and_overwrite("./static", "./public")
    from_dir = "./content"
    template_path = "./template.html"
    dest_dir = "./public"


    generate_page(os.path.join(from_dir, "index.md"), template_path, os.path.join(dest_dir, "index.html"))
    
def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

# def generate_page(from_path, template_path, dest_path):
#     print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
#     from_file = open(from_path)
#     text = from_file.read()
#     from_file.close()
#     tmp_file = open(template_path)
#     tmp = tmp_file.read()
#     tmp_file.close()

#     html_string = markdown_to_html_node(text).to_html()
#     extract_title(text)
#     tmp = tmp.replace("{{ Title }}", extract_title(text))
#     tmp = tmp.replace("{{ Content }}", html_string)

#     if os.path.exists(dest_path):
#         shutil.rmtree(dest_path)
    

#     open(dest_path, 'x').write(tmp)

    



        

main()