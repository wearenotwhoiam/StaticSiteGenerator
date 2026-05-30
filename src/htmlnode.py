class HTMLNode:
    def __init__(
            self,
            tag: str | None = None, 
            value: str | None = None, 
            children: list["HTMLNode"] | None = None, 
            props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):

        if self.props is None or self.props == "":
            return ""
        html_props = ""
        for attribute in self.props:
            html_props += f' {attribute}="{self.props[attribute]}"'
        return html_props
    
    def __repr__(self):
        return f"\nHTMLNode (Tag:{self.tag}\nValue:{self.value}\nChildren:{self.children}\nProps:{self.props})"
       
class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None) -> None:
        super().__init__(tag=tag, value=value, children=None, props=props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if not self.value:
            raise ValueError("No Value")
        if not self.tag:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"\nLeafNode (Tag:{self.tag}\nValue:{self.value}\nProps:{self.props})" 
    
class ParentNode(HTMLNode):
        def __init__(self, tag: str, children: list["HTMLNode"], props: dict[str, str] | None = None) -> None:
            super().__init__(tag=tag, value=None, children=children, props=props)
            self.tag = tag
            self.children = children
            self.props = props
        def to_html(self):
            if not self.tag:
                raise ValueError("No Tag on Parent")
            if not self.children:
                raise ValueError("No Children on Parent")
            html_string = ""
            for child in self.children:
                html_string += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>"