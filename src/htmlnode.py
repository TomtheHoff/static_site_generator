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
        if self.props == None:
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
        if self.value == None or self.value == "":
            raise ValueError
        if self.tag == None:
            return self.value   
        else:
            props = self.props_to_html()
            return f"<{self.tag}{props}>{self.value}</{self.tag}>"



