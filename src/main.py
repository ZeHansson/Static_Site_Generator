from textnode import TextType, TextNode

print("hello world")

def main():
    test_txt_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(test_txt_node)

main()