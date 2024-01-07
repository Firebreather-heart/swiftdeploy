from swiftdeploy.html.htmlcontent import HtmlSkeleton


class Tag:
    """
    Base class for html tags
    """
    def __init__(self,body=None,**kwargs) -> None:
        self.name = kwargs.get('name')
        self._class = kwargs.get('classname', '')
        self.id = kwargs.get('id','')
        self.style = kwargs.get('style', '')
        self.body = body #if you want to create an empty tag, then assign empty to body
        self.misc = kwargs.get('misc','') # this is a list containing all other tag variable such as required etc in string format
        self.href = kwargs.get('href', '')
        if self.misc is not None:
            self.misclist = "".join(i+" " for i in self.misc)
        
    def create(self):
        if self.body is None:
            return f'<{self.name} href="{self.href}" class="{self._class}" id="{self.id}" {self.misclist}/>'
        elif self.body == 'empty':
            return f'<{self.name} href="{self.href}" class="{self._class}" id="{self.id}" {self.misclist}></{self.name}>'
        else:
            return f'<{self.name} href="{self.href}" class="{self._class}" id="{self.id}" {self.misclist}>{self.body}</{self.name}>'
    
    def __str__(self) -> str:
        return self.create()
    
    def __repr__(self) -> str:
        return self.create()

class FormElement():
    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get('name','')
        self.id = kwargs.get('id', '')
        self.class_ = kwargs.get('classname', '')
        self.input_type = kwargs.get('input_type', '')
        self.label = kwargs.get('label', '')
        self.accept = kwargs.get('accept', '')  # New attribute for file types
    
    def make(self):
        if self.input_type == 'file' or self.input_type == 'image':
            self.tag = f"""    <p>
                <label for="{self.name}">{self.label}</label>
                <input name="{self.name}"  class="{self.class_}" type="file" id="{self.id}" accept="{self.accept}"></input>    
            </p>\n"""
        else:
            self.tag = f"""    <p>
                <label for="{self.name}">{self.label}</label>
                <input name="{self.name}"  class="{self.class_}" type="{self.input_type}" id="{self.id}"></input>    
            </p>\n"""
        return self.tag


class Form(HtmlSkeleton):
    def __init__(self):
        super().__init__()
    
    def set_(self):
        self.add("""<button type="submit">Submit</button>""")
        return self.wrap("form", enctype="multipart/form-data", method="post")
    
    def __str__(self) -> str:
        return super().__str__()
    
    def __repr__(self) -> str:
        return super().__repr__()

class Header(Tag):
    """
    Base class for header tags
    """
    def __init__(self,type_=None  , body=None, **kwargs) -> None:
        super().__init__( body, **kwargs)
        self.type_ = type_ 
        if isinstance(self.type_, int):
            self.name = f"h{self.type_}"
        else:
            self.name = 'header'
        self.create()

def h_tag(type_=None, body=None, **kwargs):
    param_dict = kwargs
    tag_obj = Header(type_, body, **param_dict).create()
    return tag_obj

class H1(Header):
    """
    sub class for h1 tag
    """
    def __init__(self,body=None, **kwargs) -> None:
        super().__init__(type_=1,  body=body, **kwargs)
        self.type_ = 1 
        self.name = 'h1'
        self.create()

class H2(Header):
    """
    sub class for h2 tag
    """
    def __init__(self,body=None, **kwargs) -> None:
        super().__init__(type_=2,  body=body, **kwargs)
        self.type_ = 2 
        self.name = 'h2'
        self.create()

class H3(Header):
    """
    sub class for h3 tag
    """
    def __init__(self,body=None, **kwargs) -> None:
        super().__init__(type_=3,  body=body, **kwargs)
        self.type_ = 3 
        self.name = 'h3'
        self.create()

class H4(Header):
    """
    sub class for h4 tag
    """
    def __init__(self,body=None, **kwargs) -> None:
        super().__init__(type_=4,  body=body, **kwargs)
        self.type_ = 4 
        self.name = 'h4'
        self.create()

class H5(Header):
    """
    sub class for h5 tag
    """
    def __init__(self,body=None, **kwargs) -> None:
        super().__init__(type_=5,  body=body, **kwargs)
        self.type_ = 5 
        self.name = 'h5'
        self.create()

class H6(Header):
    """
    sub class for h6 tag
    """
    def __init__(self,body=None, **kwargs) -> None:
        super().__init__(type_=6,  body=body, **kwargs)
        self.type_ = 6 
        self.name = 'h6'
        self.create()


        
class Paragraph(Tag):
    def __init__(self, body=None, **kwargs) -> None:
        super().__init__(body, **kwargs)
        self.name = 'p'
        self.create()

def p_tag(body=None, **kwargs):
    param_dict = kwargs 
    tag_obj = Paragraph(body,**param_dict).create()
    return tag_obj

class Division(Tag):
    def __init__(self, body=None, **kwargs) -> None:
        super().__init__(body, **kwargs)
        self.name = 'div'
        self.create()
    
def div(body=None, **kwargs):
    param_dict = kwargs
    tag_obj = Division(body, **param_dict).create()
    return tag_obj

def make_tag(name:str,**kwargs):
    if not isinstance(name, str):
        raise ValueError(f'expected string object got {type(name)}')
    param_dict = kwargs
    new_tag = Tag(name=name, **param_dict).create()
    return new_tag

