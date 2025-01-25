class HTMLNode:
    def __init__(self, tag = None , value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        string = ""
        if self.props is None:
            pass
        else:
            for key, value in self.props.items():
                string += (f' {key}="{value}"')
        return string
    
    def __repr__(self):
        return (f"HTMLNode(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})")


class LeafNode(HTMLNode):
    def __init__(self, tag = None , value = None, children = None, props = None):
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag == None:
            return self.value   
        else:
            props = self.props_to_html()
            return f"<{self.tag}{props}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        children_string = ""
        if self.tag is None:
            raise ValueError("no Tag was found")
        if self.children is None:
            raise ValueError("no Children is found")
        for i in self.children:
            tags = i.to_html()
            children_string += tags
        return f"<{self.tag}>{children_string}</{self.tag}>"