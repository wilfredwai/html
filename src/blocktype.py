import re

from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"

def block_to_block_type(text):
    for line in text:
        


"""
    #heading_check = re.findall(r"#{1,6} ", text)
    if re.findall(r"#{1,6} ", text) != []:
        return BlockType.HEADING
    elif re.findall(r"\\\\n", text) != []:
        return BlockType.CODE
    elif re.findall(r"> ?", text) != []:
        return BlockType.QUOTE
    elif re.findall(r"- ", text) != []:
        return BlockType.UNORDERED
    elif re.findall(r"\d. +", text) != []:
        return BlockType.ORDERED
    else:
        return BlockType.PARAGRAPH
        """
