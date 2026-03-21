import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode



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
    
    def test_leaf_to_html_p1(self):
        node = LeafNode("p", "This is a very very long test!!")
        self.assertEqual(node.to_html(), "<p>This is a very very long test!!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span><b>grandchild</b></span></div>",
            )
    def test_to_html_with_grandgrandchildren(self):
        grandgrandchild_node = LeafNode("b", "grandgrandchild")
        grandchild_node = ParentNode("p", [grandgrandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span><p><b>grandgrandchild</b></p></span></div>",
            )
    
if __name__ == "__main__":
    unittest.main()