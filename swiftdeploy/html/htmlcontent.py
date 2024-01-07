import uuid 
from .config import BASE_DIR,HTML_FILE_PATH
from collections import OrderedDict

class HtmlShell(object):
    def __init__(self, doc_type: str = 'html', title: str = "Document", charset: str = "UTF-8", http_equiv: str = "X-UA-Compatible", content: str = "IE=edge", name__meta: str = "viewport", language: str = 'en', **kwargs) -> None:
        """
        Represents an HTML shell object.

        Args:
            doc_type (str, optional): The type of the document. Defaults to 'html'.
            title (str, optional): The title of the document. Defaults to "Document".
            charset (str, optional): The character encoding of the document. Defaults to "UTF-8".
            http_equiv (str, optional): The value for the http-equiv attribute. Defaults to "X-UA-Compatible".
            content (str, optional): The value for the content attribute. Defaults to "IE=edge".
            name__meta (str, optional): The value for the name attribute of the meta tag. Defaults to "viewport".
            language (str, optional): The language of the document. Defaults to 'en'.
            **kwargs: Additional keyword arguments.

        """
        self.title = title
        self.content_ = ''
        self.type = doc_type
        if doc_type == 'html':
            self.top = "<!DOCTYPE html>"
            self.html = f"<html lang='{language}'>"

            script: list = kwargs.get('script', [])  # capture direct script
            if script is not None:
                script_box = "".join(f"<script>{str(i)}</script>" for i in script)
            else:
                script_box = ''

            script_from_link: list = kwargs.get('script_from_link', []) or kwargs.get('sfl', [])  # capture scripts from external links
            if script_from_link is not None:
                script_box_from_link = "".join(f"<script src='{str(i)}'></script>" for i in script_from_link)
            else:
                script_box_from_link = ''

            other_links: list = kwargs.get('link_css', [])
            if other_links is not None:
                css = "".join(f"<link rel='stylesheet' href='{str(i)}'>" for i in other_links)  # capture css
            else:
                css = ''

            self.head = f"""
    <head>
        <meta charset="{charset}">
        <meta http-equiv="{http_equiv}" content="{content}">
        <meta name="{name__meta}" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        {script_box}{script_box_from_link}{css}
    </head>
                        """

    def __iter__(self):
        """
        Returns an iterator over the HTML shell object.

        Yields:
            str: The HTML shell components.

        """
        buck = [self.top, self.html, self.head, self.content_]
        for i in buck:
            yield i

    def __repr__(self) -> str:
        """
        Returns a string representation of the HTML shell object.

        Returns:
            str: The string representation of the HTML shell object.

        """
        return f"<HtmlShell object: {self.title}>"

    def __str__(self):
        """
        Returns a string representation of the HTML shell object.

        Returns:
            str: The string representation of the HTML shell object.

        """
        return f"<HtmlShell object: {self.title}>"

    def insert(self, obj):
        """
        Inserts content into the HTML shell object.

        Args:
            obj: The content to be inserted.

        Returns:
            HtmlShell: The updated HTML shell object.

        """
        self.content_ = "".join(str(obj))
        return self

    def to_file(self, filepath=HTML_FILE_PATH):
        """
        Writes the HTML shell object to a file.

        Args:
            filepath (str, optional): The path of the file to write to. Defaults to HTML_FILE_PATH.

        Raises:
            ValueError: If the value of 'type' is unknown.

        """
        if self.type == 'html':
            self.all = self.top + "\n" + self.html + "\n" + self.head + '\n' + self.content_ + "\n" + "</html>"
        elif self.type == 'xml':
            self.all = "<html xmlns='http://www.w3.org/1999/xhtml'>"
        else:
            raise ValueError(f"Unknown value '{self.type}' given for argument 'type', this argument receives either 'html' or 'xml' ")
        file_content = self.all
        with open(filepath, 'w') as html:
            html.write(file_content)
    
class HtmlSkeleton(object):
    def __init__(self):
        """
        Initializes an instance of HtmlSkeleton class.
        """
        self.innards = OrderedDict()
    
    def __str__(self) -> str:
        """
        Returns the string representation of the HtmlSkeleton object.
        """
        return self.barebones

    def __repr__(self) -> str:
        """
        Returns the string representation of the HtmlSkeleton object.
        """
        return self.barebones

    def __iter__(self):
        """
        Iterates over the innards of the HtmlSkeleton object.
        """
        for i in self.innards:
            yield i 

    def add(self, obj, name=None):
        """
        Adds an object to the HtmlSkeleton object.

        Args:
            obj: The object to be added.
            name: The name of the object (optional).

        Returns:
            The HtmlSkeleton object.
        """
        if name is None:
            name = str(uuid.uuid4())
        marked_obj = Marker(obj, name)
        self.innards[name] = marked_obj 
        self.finalise()
        return self 
    
    def finalise(self):
        """
        Finalizes the HtmlSkeleton object by joining the innards.
        """
        self.barebones = "".join(i[1].obj+"\n" for i in self.innards.items())
 
    def load_string(self, obj:str):
        """
        Loads a string into the HtmlSkeleton object.

        Args:
            obj: The string to be loaded.
        """
        str_obj = obj 
        self.add(str_obj)
    
    def load_file(self, path:str):
        """
        Loads a file into the HtmlSkeleton object.

        Args:
            path: The path of the file to be loaded.
        """
        with open(path, 'r') as file:
            doc = file.read()
            container = ""
            for i in doc:
                container.join(i)
        self.add(container)
    
    def remove(self, name):
        """
        Removes an object from the HtmlSkeleton object.

        Args:
            name: The name of the object to be removed.
        """
        del self.innards[name]
    
    def wrap(self, wrapper:str, **kwargs):
        """
        Wraps the HtmlSkeleton object with a wrapper tag.

        Args:
            wrapper: The wrapper tag.
            kwargs: Additional attributes for the wrapper tag.

        Returns:
            The wrapped HtmlSkeleton object.
        """
        sb = ''
        for key, item in kwargs.items():
            sb += f"""{key}="{item}" """
        self.barebones = f"<{wrapper} {sb}> \n\t {self.barebones} \n\t </{wrapper}>"
        return self.barebones



    
class Marker(object):
    def __init__(self, object_to_mark, name=None) -> None:
        """
        Initializes a Marker object.

        Args:
            object_to_mark: The object to be marked.
            name: Optional name for the marker.

        Returns:
            None
        """
        self.obj = object_to_mark
        self.name = name 
        if self.name is not None:
            self.name = name
        self.mark()
    
    def mark(self):
        """
        Marks the object with a unique identifier.

        Returns:
            The unique identifier of the marked object.
        """
        if self.name is not None:
            self.id =  (self.obj, self.name)
        else:
            self.id =  (self.obj,)
        return self.id
    
    def __gt__(self, other):
        """
        Compares two Marker objects based on their names.

        Args:
            other: The other Marker object to compare with.

        Returns:
            True if the name of this Marker is greater than the name of the other Marker, False otherwise.

        Raises:
            TypeError: If the names of the two Marker objects are of different types.
        """
        if type(self.name) == type(other.name):
            return self.name > other.name
        else:
            raise TypeError('Cannot compare values of different types')

    def __lt__(self, other):
        """
        Compares two Marker objects based on their names.

        Args:
            other: The other Marker object to compare with.

        Returns:
            True if the name of this Marker is less than the name of the other Marker, False otherwise.

        Raises:
            TypeError: If the names of the two Marker objects are of different types.
        """
        if type(self.name) == type(other.name):
            return self.name < other.name
        else:
            raise TypeError('Cannot compare values of different types')
    
    def __str__(self) -> str:
        """
        Returns a string representation of the Marker object.

        Returns:
            A string representation of the unique identifier of the Marker object.
        """
        return str(self.id) 
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the Marker object.

        Returns:
            A string representation of the unique identifier of the Marker object.
        """
        return str(self.id)

def iwrap(wrapper:str,obj:str, class_:str,**kwargs):
    """
    Wraps the given object with an HTML wrapper element.

    Args:
        wrapper (str): The HTML wrapper element to use.
        obj (str): The object to wrap.
        class_ (str): The CSS class to apply to the wrapper element.
        **kwargs: Additional attributes to add to the wrapper element.

    Returns:
        str: The wrapped object as an HTML string.
    """
    sb = ''
    for key,item in kwargs.items():
        sb += f"""{key}='{item}'"""
    barebones = f"<{wrapper} class='{class_}' {sb}> \n\t {obj} \n\t </{wrapper}>"
    return barebones
