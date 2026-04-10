import unittest

from blocktype import BlockType, block_to_block_type

class TestBlocktoblocktype(unittest.TestCase):
    def test_block_to_block_type_1(self):
        text = "#### This is a Headings"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.HEADING)
    def test_block_to_block_type_2(self):
        text = "```\nThis is a Code\nAnother line\n```"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.CODE)
    def test_block_to_block_type_3(self):
        text = "> This is a Quote"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.QUOTE)
    def test_block_to_block_type_4(self):
        text = "- This is a unordered"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.UNORDERED)
    def test_block_to_block_type_5(self):
        text = "1. This is an order"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.ORDERED)
    def test_block_to_block_type_6(self):
        text = "This is a paragraph"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)