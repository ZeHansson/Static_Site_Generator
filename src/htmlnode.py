

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
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        tmp_tag = self.tag
        tmp_val = self.value
        tmp_chil = self.children
        tmp_props = self.props_to_html()

        if self.tag == None:
            tmp_tag = "None"
        if self.value == None:
            tmp_val = "None"
        if self.children == None:
            tmp_chil = "None"
        if self.props == None:
            tmp_props = "None"

        return "Tag: "+ tmp_tag + " Value: " + tmp_val + " Children: " + tmp_chil + " Props: " + tmp_props


    
