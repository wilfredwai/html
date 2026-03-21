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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()