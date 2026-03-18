class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None or self.props == {}:
            return ""
        prop = ""
        for key in self.props:
            prop = prop + f' {key}="{self.props[key]}"'
        return prop

    def __repr__(self):
        return f"HTMLnode({self.tag}, {self.value}, children: {self.children}, {self.props})"
