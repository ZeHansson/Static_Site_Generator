from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode
from markdown import *
from markdown_blocks import markdown_to_blocks

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

    print(markdown_to_blocks("   \n\n# This is a heading \n\nThis is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n - This is the first list item in a list block\n- This is a list item\n- This is another list item     "))

        

main()