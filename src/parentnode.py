from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, value=None, props=None):
        super().__init__(children=children, props=props, tag=tag, value=None)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent Node must have a tag")
        if self.children is None:
            raise ValueError("Parent Node must have a children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
