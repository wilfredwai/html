import unittest

from htmlnode import HTMLNode, LeafNode


class TestHtmlNode(unittest.TestCase):

    def test_1(self):
        node = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_2(self):
        node = HTMLNode(props={"href": "https://www.apple.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.apple.com" target="_blank"')

    def test_3(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()