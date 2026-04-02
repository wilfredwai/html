import unittest

from markdown_to_blocks import markdown_to_blocks

class TestMakdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_1(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,
                         [
                             "This is **bolded** paragraph",
                             "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                             "- This is a list\n- with items",
                             ],
                             )
    
    def test_markdown_to_blocks_2(self):
        md = """
This is `code` paragraph

This is another paragraph with **bolded** text and `code` here
This is also another paragraph with $#@#!%!@%@!#@!$!# with 5 spaces...     
This is the same paragraph on a new line

- This is a list
- with items
- also an apple
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks,
                         [
                             "This is `code` paragraph",
                             "This is another paragraph with **bolded** text and `code` here\nThis is also another paragraph with $#@#!%!@%@!#@!$!# with 5 spaces...\nThis is the same paragraph on a new line",
                             "- This is a list\n- with items\n- also an apple",
                             ],
                             )
