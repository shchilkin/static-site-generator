import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p_with_props(self):
        node = LeafNode("p", "Hello, world!", {"href": "https://example.com"})
        self.assertEqual(
            node.to_html(), '<p href="https://example.com">Hello, world!</p>'
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), "Hello, world!")
