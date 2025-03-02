import unittest

from textnode import TextNode, TextType
from markdown import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a FAT text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_texttype(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_texttype_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_text_url(self):
        node = TextNode("This is a FAT text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_text_texttype(self):
        node = TextNode("This is a FAT text node", TextType.BOLD)
        node2 = TextNode("This is a LEANING text node", TextType.ITALIC)

    def test_not_eq_ALL(self):
        node = TextNode("This is a FAT text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")


#class Test_Markdown_To_TextNode(unittest.TestCase):
#    def test_detect_code(self):
#        self.assertEqual(split_nodes_delimiter([TextNode("This is text with a `code block` word", TextType.TEXT)],"`", TextType.CODE)[1].text,"code block" )

#    def test_detect_bold(self):
#        self.assertEqual(split_nodes_delimiter([TextNode("This is text with a **bold** word", TextType.TEXT)],"**", TextType.BOLD)[1].text,"bold" )

#    def test_detect_italic(self):
#        self.assertEqual(split_nodes_delimiter([TextNode("This is text with an _Italic_ word", TextType.TEXT)],"_", TextType.ITALIC)[1].text,"Italic" )


if __name__ == "__main__":
    unittest.main()
