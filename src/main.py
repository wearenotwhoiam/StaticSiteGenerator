from textnode import TextNode
from textnode import TextType
def main():
    test = TextNode("Test it up", TextType.BOLD , "www.yes.no")
    print(test.__repr__())

if __name__ == "__main__":
    main()