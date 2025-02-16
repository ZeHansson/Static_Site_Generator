

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError("Not yet implemented")
    def props_to_html(self):
        if self.props is None:
            #print("it thinks it is none")
            return ""
        props_html = ""
        #print("it does not think it is none")
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value is None:
            raise ValueError("Leafnodes requires a value - None found")
        if self.tag is None:
            return str(self.value)
        return "<"+ self.tag + self.props_to_html()+">"+self.value+"</"+self.tag+">" 
    
    def __repr__(self):
        return "<"+ self.tag + self.props_to_html()+">"+self.value+"</"+self.tag+">" 