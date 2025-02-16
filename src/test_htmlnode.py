import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )


if __name__ == "__main__":
    unittest.main()









#first try Was not sure abaout values. have taken test from course, assume those are future proof.:
#class TestHTMLNode(unittest.TestCase):
#    def test_repr(self):
#        prop = {"href": "https://www.google.com","target": "_blank",}
        
#        htmlnode = HTMLNode( None,None ,None , prop )
#        res_str = "Tag: "+ "None" + " Value: " + "None" + " Children: " + "None" + " Props: " + htmlnode.props_to_html()
#        print("test final string: \n"+res_str +"| <-- Ends here")
#        print("test final string: \n" + htmlnode.__repr__() +"| <-- Ends here")
#        self.assertEqual(htmlnode.__repr__(), res_str )
    
    
#if __name__ == "__main__":
#    unittest.main()