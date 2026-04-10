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
    lines = text.split("\n")

    if text.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if text.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if text.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED
    if text.startswith("1. "):
        for i in range(0, len(lines)):
            if not lines[i].startswith(f"{i+1}. "):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED
    else:
        return BlockType.PARAGRAPH


"""
    heading_check = re.findall(r"#{1,6} ", text)
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
