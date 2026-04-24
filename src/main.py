import os
from textnode import TextType, TextNode

def main():
    if os.path.exists("./public") and os.path.exists("./src/static"):
        
    else:
        print("Error, path not exists!")
main()