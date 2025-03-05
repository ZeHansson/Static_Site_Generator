from enum import Enum
from htmlnode import HTMLNode, text_node_to_html_node, ParentNode, LeafNode
from markdown import text_to_textnodes
from textnode import TextNode, TextType
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

# def extract_title(markdown):
#     if "#" in markdown:
#         return markdown.strip().split("\n")[0].strip('#').strip()
#     else:
#         raise Exception("missing header")

def markdown_to_blocks(markdown):
    lines = []
    for line in markdown.split("\n\n"):
        if any(c.isalpha() for c in line):
            temp = line
            if "\n" in line:
                temp = ""
                for new in line.split("\n"):
                    temp += f"{new.strip()}\n"

            lines.append(temp.strip())
    #returns ['# This is a heading', 'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.', '- This is the first list item in a list block', '- This is a list item', '- This is another list item']
    return lines

def block_to_block_type(markdown_block):
    if re.match(r"^#{1,6}\s", markdown_block):
        return BlockType.HEADING
    elif markdown_block.startswith("```") and markdown_block.endswith("```"):
        return BlockType.CODE
    elif all(re.match(r"^>", line) for line in markdown_block.splitlines()):
        return BlockType.QUOTE
    elif all(re.match(r"^-\s\S", line) for line in markdown_block.splitlines()):
        # "^-\s\S|^$" allows empty lines aswell
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(markdown_block):
        return BlockType.ORDERED_LIST
    else :
        return BlockType.PARAGRAPH

def is_ordered_list(markdown_block):
    lines = markdown_block.splitlines()  # Split block into individual lines
    for index, line in enumerate(lines):
        match = re.match(r"^(\d+)\.\s", line)  # Match number + ". " at the start of each line
        if not match:
            return False  # If a line doesn't match the "number. " pattern, it's invalid
        if int(match.group(1)) != index + 1:
            return False  # Validate that numbers count up sequentially
    return True

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return olist_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)