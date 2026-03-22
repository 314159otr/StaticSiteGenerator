import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_default_constructor(self):
        htmlNode = HTMLNode()
        self.assertEqual(htmlNode.tag, None)
        self.assertEqual(htmlNode.value, None)
        self.assertEqual(htmlNode.children, None)
        self.assertEqual(htmlNode.props, None)

    def test_props_to_html(self):
        propsDict = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        htmlNode = HTMLNode(props=propsDict)
        self.assertEqual(htmlNode.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_empty_props_to_html(self):
        htmlNode = HTMLNode()
        self.assertEqual(htmlNode.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "some text with no tag")
        self.assertEqual(node.to_html(), "some text with no tag")

if __name__ == "__main__":
    unittest.main() 
