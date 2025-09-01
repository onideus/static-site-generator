from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")

        if self.children is None:
            raise ValueError("All parent nodes must have children")

        str_to_return = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            str_to_return += child.to_html()

        str_to_return += f"</{self.tag}>"

        return str_to_return