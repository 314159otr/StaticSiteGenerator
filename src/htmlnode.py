
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        fstring = ""
        if self.props is None:
            return fstring
        for key, value in self.props.items():
            fstring += f" {key}=\"{value}\""
        return fstring

    def __repr__(self):
        return f"HTMLNode(\ntag = {self.tag}\nvalue = {self.value}\nchildren = {self.children}\nprops = {self.props}\n)"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(\ntag = {self.tag}\nvalue = {self.value}\nprops = {self.props}\n)"
