from textnode import TextType, TextNode
from htmlnode import HTMLNode

print("hello world")

def main():
    test_txt_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    #print(test_txt_node)
    prop = {"href": "https://www.google.com","target": "_blank",}
    htmlnode = HTMLNode( None,None ,None , prop )
    print(htmlnode)
        

main()