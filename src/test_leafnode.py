import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_value_none_raises(self):
        node = LeafNode("p", None, {})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_tag_none_returns_value(self):
        node = LeafNode(None, "hello", {})
        self.assertEqual("hello", node.to_html())

    def test_b_tag_renders(self):
        node = LeafNode("b", "bold text", {})
        self.assertEqual("<b>bold text</b>", node.to_html())

    def test_p_tag_renders(self):
        node = LeafNode("p", "paragraph", {})
        self.assertEqual("<p>paragraph</p>", node.to_html())

    def test_a_tag_with_href_renders(self):
        node = LeafNode("a", "Click here", {"href": "https://example.com"})
        self.assertEqual('<a href="https://example.com">Click here</a>', node.to_html())

    def test_a_tag_without_href_returns_none(self):
        node = LeafNode("a", "Click here", {})
        self.assertIsNone(node.to_html())

    def test_img_tag_with_src_renders(self):
        node = LeafNode("img", "An image", {"src": "image.png"})
        self.assertEqual('<img src="image.png" alt="An image"/>', node.to_html())

    def test_img_tag_without_src_returns_none(self):
        node = LeafNode("img", "An image", {})
        self.assertIsNone(node.to_html())

    def test_unknown_tag_returns_none(self):
        node = LeafNode("div", "content", {})
        self.assertIsNone(node.to_html())


if __name__ == "__main__":
    unittest.main()
