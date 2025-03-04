from textnode import TextType 

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
        if self.tag is None:
            return str(self.value or "")  # Handle None values
    
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value or ''}</{self.tag}>"
        #prob should have used : f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return "<"+ self.tag + self.props_to_html()+">"+self.value+"</"+self.tag+">" 
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None , children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML : no tag")
        if self.children is None:
            raise ValueError("Invalid HTML : Missing child")
        
        html_string = ""
        for child in self.children:
            html_string = html_string + child.to_html()
        
        return f"<{self.tag}>{html_string}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

def text_node_to_html_node(text_node):
            
    if text_node.text_type is TextType.TEXT:
        return LeafNode(None,text_node.text,)
    elif text_node.text_type is TextType.BOLD:
        return LeafNode("b", text_node.text,)

    elif text_node.text_type is TextType.ITALIC:
        return LeafNode("i", text_node.text,)

    elif text_node.text_type is TextType.CODE:
        return LeafNode("code", text_node.text,)

    elif text_node.text_type is TextType.LINK:
        return LeafNode("a", text_node.text,{"href": text_node.url})

    elif text_node.text_type is TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url,"alt": text_node.text} )
    else:
        raise Exception(f"Invalid text type: {text_node.text_type}")