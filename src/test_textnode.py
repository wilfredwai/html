import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is the first node", TextType.CODE)
        node2 = TextNode("This is the sec node", TextType.CODE)
        self.assertNotEqual(node, node2)
    
    def test_not_eq2(self):
        node = TextNode("This is a node", TextType.TEXT)
        node2 = TextNode("This is a node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_not_eq3(self):
        node = TextNode("This is a node", TextType.CODE, None)
        node2 = TextNode("This is a node", TextType.CODE, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a node", TextType.CODE, "www.google.com")
        node2 = TextNode("This is a node", TextType.CODE, "www.google.com")
        self.assertEqual(node, node2)

# class TextNode:
    # def __init__(self, text, text_type, url=None):
        # self.text = text
        # self.text_type = text_type
        # self.url = url

    def extnode_to_htmlnode_test_1(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_textnode_to_htmlnode_2(self):
        node = TextNode("This is a Link node", TextType.LINK, "www.apple.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a Link node")
        self.assertEqual(html_node.props, {"href": "www.apple.com"})

    def test_textnode_to_htmlnode_3(self):
        node = TextNode("This is a Image node", TextType.IMAGE, "www.imagetest.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "www.imagetest.com", "alt": "This is a Image node"})

if __name__ == "__main__":
    unittest.main()