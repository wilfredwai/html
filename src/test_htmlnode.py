import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_1(self):
        self.props = {"href": "https://www.google.com","target": "_blank",}

    def test_2(self):
        self.props = {"href": "https://www.apple.com", "target": "_blank"}

    def test_3(self):
        self.props = {"href": "Error 404", "target": "not_blank"}

if __name__ == "__main__":
    unittest.main()