import unittest

from textnode import TextType, TextNode
from split_nodes_image_and_link import split_nodes_image, split_nodes_link

class TestSplitNode(unittest.TestCase):

    def test_split_link_1(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT,)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
                ],
                new_nodes,
                )

    def test_split_link_2(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)" \
            " also [3th image](https://www.kdfhusadfhjskd.org)", TextType.TEXT,)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" also ", TextType.TEXT),
                TextNode("3th image", TextType.LINK, "https://www.kdfhusadfhjskd.org"),
                ],
                new_nodes,
                )
def test_split_images_1(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT,)
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),                ],
            new_nodes,
            )
def test_split_images_2(self):
    node = TextNode("This is text with a link ![Boot.dev](https://www.boot.dev/img/bootdev-logo-full-150.png) and ![Boot face](https://www.boot.dev/_nuxt/new_boots_profile.DriFHGho.webp)",TextType.TEXT,)
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("Boot.dev", TextType.IMAGE, "https://www.boot.dev/img/bootdev-logo-full-150.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("Boot face", TextType.IMAGE, "https://www.boot.dev/_nuxt/new_boots_profile.DriFHGho.webp"),
            ],
            new_nodes,
            )
