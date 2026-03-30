import unittest

from textnode import TextType, TextNode
from split_node import split_nodes_delimiter, split_nodes_image

class TestSplitNode(unittest.TestCase):
    def test_split_nodes_delimiter_1(self):
        node = TextNode("This is a node with `code inside` the text node", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE),
                         [TextNode("This is a node with ", TextType.TEXT),
                          TextNode("code inside", TextType.CODE),
                          TextNode(" the text node", TextType.TEXT)]
                          )
    def test_split_nodes_delimiter_2(self):
        node = TextNode("This is a node with **bold inside** the text node", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD),
                         [TextNode("This is a node with ", TextType.TEXT),
                          TextNode("bold inside", TextType.BOLD),
                          TextNode(" the text node", TextType.TEXT)]
                          )
    def test_split_nodes_delimiter_3(self):
        node = TextNode("This is a node with _italic inside_ the text node", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "_", TextType.ITALIC),
                         [TextNode("This is a node with ", TextType.TEXT),
                          TextNode("italic inside", TextType.ITALIC),
                          TextNode(" the text node", TextType.TEXT)]
                          )
    def test_split_nodes_delimiter_4(self):
        node = TextNode("This is a node with **invalid** **the text node", TextType.TEXT)
        with self.assertRaises(Exception):
             split_nodes_delimiter([node], "**", TextType.BOLD)
                        
    def test_split_nodes_delimiter_5(self):
        node = TextNode("This is the text without any delimiter", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE),
                         [TextNode("This is the text without any delimiter", TextType.TEXT)]
                          )
        
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
            )