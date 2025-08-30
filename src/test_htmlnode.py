import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("This is a HTML node", "This is a value", [1, 2, 3], {"key": "value"})
        node2 = HTMLNode("This is a HTML node", "This is a value", [1, 2, 3], {"key": "value"})
        self.assertEqual(node, node2)

    def test_ineq_tag(self):
        node = HTMLNode(tag="This is a HTML node")
        node2 = HTMLNode(tag="This is another HTML node")
        self.assertNotEqual(node, node2)

    def test_ineq_value(self):
        node = HTMLNode(value="This is a HTML node")
        node2 = HTMLNode(value="This is another HTML node")

    def test_ineq_children(self):
        node = HTMLNode(children=[1, 2, 3])
        node2 = HTMLNode(children=[1, 2, 4])
        self.assertNotEqual(node, node2)

    def test_ineq_props(self):
        node = HTMLNode(props={"key": "value"})
        node2 = HTMLNode(props={"key": "value2"})

    def test_repr(self):
        node = HTMLNode("This is a HTML node", "This is a value", [1, 2, 3], {"key": "value"})
        self.assertEqual(repr(node), "HTMLNode(This is a HTML node, This is a value, [1, 2, 3], {'key': 'value'})")

    def test_props_to_html(self):
        node = HTMLNode("This is a HTML node", "This is a value", [1, 2, 3], {"key": "value"})
        self.assertEqual(node.props_to_html(), ' key="value"')


if __name__ == "__main__":
    unittest.main()
