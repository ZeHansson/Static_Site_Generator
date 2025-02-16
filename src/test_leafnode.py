import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_tohtml_no_link(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_tohtml_with_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(node.to_html())
        print("<a href=\"https://www.google.com\">Click me!</a>")
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")



if __name__ == "__main__":
    unittest.main()
