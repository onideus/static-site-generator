from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        if self.tag is None:
            return self.value

        if self.tag == "b" or self.tag == "p":
            return f"<{self.tag}>{self.value}</{self.tag}>"

        if self.tag == "a" and self.props is not None and "href" in self.props:
            for k, v in self.props.items():
                if k == "href":
                    return f'<a href="{v}">{self.value}</a>'

        if self.tag == "img" and self.props is not None and "src" in self.props:
            for k, v in self.props.items():
                if k == "src":
                    return f'<img src="{v}" alt="{self.value}"/>'

        return None
