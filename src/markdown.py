import re
from textnode import TextNode, TextType


def extract_markdown_images(text):
    return use_regex(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_markdown_links(text):
    return use_regex(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def use_regex(pattern, text):
    return re.findall(pattern,text)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return split_nodes(old_nodes, delimiter,text_type)

def split_nodes(nodes, delimiter, text_type):
    new_nodes = []
    for old_node in nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_link_nodes(nodes, text_type):
    is_image = text_type is TextType.IMAGE
    is_link = text_type is TextType.LINK
    new_nodes = []
    for old_node in nodes:
        # Skip non-text nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        matches = []
        if is_image:
            matches = extract_markdown_images(old_node.text)
        elif is_link: 
            matches = extract_markdown_links(old_node.text)

        if not matches:
            new_nodes.append(old_node)
            continue

        current_text = old_node.text
        for alt_text, url in matches:
            if is_image:
                markdown = f"![{alt_text}]({url})"
            else:
                markdown = f"[{alt_text}]({url})"

            parts = current_text.split(markdown, 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
                
            new_nodes.append(TextNode(alt_text, text_type, url))

            if len(parts) > 1:
                current_text = parts[1]
            else:
                current_text = ""
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
            
    return new_nodes


def split_nodes_image(old_nodes):
    return split_link_nodes(old_nodes, TextType.IMAGE)
    

def split_nodes_link(old_nodes):
    return split_link_nodes(old_nodes, TextType.LINK)

def text_to_textnodes(text):
    nodes = split_nodes_delimiter([TextNode(text,TextType.TEXT)],"**",TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes


#def split_nodes_delimiter(old_nodes, delimiter, text_type):
#    newnodes = []
#    for node in old_nodes:
#        if node.text_type is not TextType.TEXT:
#            newnodes.append(node)
#        else:
#            if delimiter in node.text:
#                texts = node.text.split(delimiter)
#                for i in range(len(texts)):
#                    if (i+2)%2 == 1:
#                        newnodes.append(TextNode(texts[i],text_type))
#                    else: 
#                        newnodes.append(TextNode(texts[i], TextType.TEXT))

#    return newnodes
               
            