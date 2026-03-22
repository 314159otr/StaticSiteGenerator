import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main() 
