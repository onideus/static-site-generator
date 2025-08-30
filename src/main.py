from textnode import TextNode, TextType

if __name__ == '__main__':
    node = TextNode("Hello World", TextType.LINK, "URL")
    print(node)
