# Base class representing an HTML element
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # The HTML tag name (e.g., 'div', 'p')
        self.tag = tag
        # The textual content of the HTML element
        self.value = value
        # A list of child HTMLNode elements (used in ParentNode)
        self.children = children
        # A dictionary of HTML attributes (e.g., {'class': 'container'})
        self.props = props

    # Method that must be implemented in subclasses to convert the node to HTML
    def to_html(self):
        raise NotImplementedError

    # Helper method to convert properties (attributes) to an HTML-compatible string
    def props_to_html(self):
        string = ""
        if self.props is None:
            pass  # No properties, do nothing
        else:
            for key, value in self.props.items():
                # Convert key-value pairs to HTML attribute syntax
                string += (f' {key}="{value}"')
        return string

    # String representation of the HTMLNode object for debugging purposes
    def __repr__(self):
        return (f"HTMLNode(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})")


# Class representing an HTML element without children (e.g., <p>text</p>)
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        # Call the base class constructor
        super().__init__(tag, value, children, props)

    # Convert the LeafNode to an HTML string
    def to_html(self):
        if self.value is None:
            raise ValueError  # Ensure a value is provided
        if self.tag is None:
            return self.value  # If no tag, return the value as plain text
        else:
            props = self.props_to_html()  # Get the properties as HTML attributes
            return f"<{self.tag}{props}>{self.value}</{self.tag}>"


# Class representing an HTML element that contains child elements (e.g., <div><p>...</p></div>)
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        # Call the base class constructor with no value, since ParentNode holds children
        super().__init__(tag, None, children, props)

    # Convert the ParentNode and its children to an HTML string
    def to_html(self):
        children_string = ""
        if self.tag is None or self.tag == "":
            raise ValueError("no Tag was found")  # Ensure a tag is provided
        if self.children is None:
            raise ValueError("no Children was found")  # Ensure children are provided
        for i in self.children:
            # Convert each child node to HTML recursively
            tags = i.to_html()
            children_string += tags
        # Wrap children in the parent HTML tag
        return f"<{self.tag}>{children_string}</{self.tag}>"
