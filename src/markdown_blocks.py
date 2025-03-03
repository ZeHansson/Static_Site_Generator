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