from swiftdeploy.html.htmlcontent import HtmlSkeleton,iwrap


class Tag:
    """
    Base class for html tags
    
    Attributes:
        name (str): The name of the HTML tag.
        _class (str): The class attribute of the HTML tag.
        id (str): The id attribute of the HTML tag.
        style (str): The style attribute of the HTML tag.
        body (str): The content of the HTML tag.
        misc (str): Additional tag variables in string format.
        href (str): The href attribute of the HTML tag.
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
        """
        Create an HTML tag based on the provided attributes.

        Returns:
            str: The generated HTML tag.

        Raises:
            None
        """
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
        """
        Initialize a FormElement object.

        Args:
            **kwargs: Additional keyword arguments to customize the FormElement.

        Keyword Args:
            name (str): The name attribute of the form element.
            id (str): The id attribute of the form element.
            classname (str): The class attribute of the form element.
            input_type (str): The type attribute of the input element.
            label (str): The label text for the form element.
            accept (str): The accept attribute for file types.

        Returns:
            None
        """
        self.name = kwargs.get('name','')
        self.id = kwargs.get('id', '')
        self.class_ = kwargs.get('classname', '')
        self.input_type = kwargs.get('input_type', '')
        self.label = kwargs.get('label', '')
        self.accept = kwargs.get('accept', '')  # New attribute for file types
    
    def make(self):
        """
        Generate the HTML tag for the form element.

        Returns:
            str: The HTML tag for the form element.
        """
        if self.input_type == 'file' or self.input_type == 'image':
            self.tag = f""" 
                <label for="{self.name}">{self.label}</label>
                <input name="{self.name}"  class="{self.class_}" type="file" id="{self.id}" accept="{self.accept}"></input>    
            \n"""
        else:
            self.tag = f"""
                <label for="{self.name}">{self.label}</label>
                <input name="{self.name}"  class="{self.class_}" type="{self.input_type}" id="{self.id}"></input>    
            \n"""
        self.tag = iwrap('div', self.tag, class_='form-group')
        return self.tag


class Form(HtmlSkeleton):
    def __init__(self):
        """
        Represents an HTML form element.

        This class provides methods to set attributes and add content to the form element.
        """
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
    
    Args:
        type_ (int): The header type. If provided, the tag name will be set to 'h{type_}'.
        body (str): The content of the header tag.
        **kwargs: Additional attributes to be added to the header tag.
    """
    def __init__(self, type_=None, body=None, **kwargs) -> None:
        super().__init__(body, **kwargs)
        self.type_ = type_ 
        if isinstance(self.type_, int):
            self.name = f"h{self.type_}"
        else:
            self.name = 'header'
        self.create()

def h_tag(type_=None, body=None, **kwargs):
    """
    Create an HTML header tag with the specified type, body, and additional attributes.

    Args:
        type_ (str): The type of the header tag (e.g., 'h1', 'h2', 'h3', etc.).
        body (str): The content of the header tag.
        **kwargs: Additional attributes to be added to the header tag.

    Returns:
        str: The HTML representation of the header tag.
    """
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
    """
    Represents an HTML paragraph tag.

    Args:
        body (str): The content of the paragraph.
        **kwargs: Additional attributes to be added to the paragraph tag.

    Attributes:
        name (str): The name of the tag ('p').

    Methods:
        create: Creates the paragraph tag.
    """

    def __init__(self, body=None, **kwargs) -> None:
        super().__init__(body, **kwargs)
        self.name = 'p'
        self.create()

def p_tag(body=None, **kwargs):
    """
    Create a paragraph HTML tag with the given body and optional attributes.

    Args:
        body (str): The content of the paragraph tag.
        **kwargs: Optional attributes to be added to the paragraph tag.

    Returns:
        str: The HTML representation of the paragraph tag.
    """
    param_dict = kwargs 
    tag_obj = Paragraph(body, **param_dict).create()
    return tag_obj

class Division(Tag):
    """
    Represents an HTML <div> tag.

    Args:
        body (str): The content of the <div> tag.
        **kwargs: Additional attributes to be added to the <div> tag.

    Attributes:
        name (str): The name of the tag ('div').

    Methods:
        create: Creates the <div> tag with the specified attributes and content.
    """

    def __init__(self, body=None, **kwargs) -> None:
        super().__init__(body, **kwargs)
        self.name = 'div'
        self.create()
    
def div(body=None, **kwargs):
    param_dict = kwargs
    tag_obj = Division(body, **param_dict).create()
    return tag_obj

def make_tag(name:str,**kwargs):
    """
    Create an HTML tag with the given name and optional attributes.

    Args:
        name (str): The name of the HTML tag.
        **kwargs: Optional attributes for the HTML tag.

    Returns:
        str: The created HTML tag.

    Raises:
        ValueError: If the name parameter is not a string.

    Example:
        >>> make_tag('div', id='myDiv', class_='container')
        '<div id="myDiv" class="container"></div>'
    """
    if not isinstance(name, str):
        raise ValueError(f'expected string object got {type(name)}')
    param_dict = kwargs
    new_tag = Tag(name=name, **param_dict).create()
    return new_tag

