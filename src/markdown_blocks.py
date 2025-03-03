from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

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