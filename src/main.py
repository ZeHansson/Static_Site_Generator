from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode
from markdown import *

#print("hello world")

def main():
    #test_txt_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    #print(test_txt_node)
    #prop = {"href": "https://www.google.com","target": "_blank",}
    #htmlnode = HTMLNode( None,None ,None , prop )
    #print(htmlnode)
    node = LeafNode("p", "This is a paragraph of text.")
    #node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    #print(node.to_html())
    #print(node2.to_html())
    #print(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"))
    print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"))
        

main()