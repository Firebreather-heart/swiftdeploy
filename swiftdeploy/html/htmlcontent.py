import uuid 
from .config import BASE_DIR,HTML_FILE_PATH
from collections import OrderedDict

class HtmlShell(object):
    def __init__(self,doc_type:str='html', title="Document",charset="UTF-8", http_equiv="X-UA-Compatible",content="IE=edge", name__meta="viewport", language='en',**kwargs) -> None:
        """
        
        """
        self.title = title
        self.content_ = ''
        self.type = doc_type
        if doc_type=='html':
            self.top = "<!DOCTYPE html>"
            self.html = f"<html lang='{language}'>"

            script:list = kwargs.get('script',[]) #capture direct script
            if script is not None:         
                script_box = "".join(f"<script>{str(i)}</script>" for i in script) 
            else:script_box=''

            script_from_link:list = kwargs.get('script_from_link',[]) or kwargs.get('sfl',[]) #capture scripts from external links  
            if script_from_link is not None:     
                script_box_from_link  = "".join(f"<script src='{str(i)}'></script>" for i in script_from_link) 
            else:script_box_from_link=''
            
            other_links:list = kwargs.get('link_css', [])
            if other_links is not None:
                css = "".join(f"<link rel='stylesheet' href='{str(i)}'>" for i in other_links) #capture css
            else: css=''
            
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
        buck = [self.top,self.html, self.head, self.content_]
        for i in buck:yield i
    
    def __repr__(self) -> str:
        return f"<HtmlShell object: {self.title}>"

    def __str__(self):
        return f"<HtmlShell object: {self.title}>"

    def insert(self,obj):
        self.content_ = "".join(str(obj))
        return self 
    
    def to_file(self, filepath=HTML_FILE_PATH):
        if self.type == 'html':
            self.all = self.top + "\n" + self.html + "\n"  + self.head + '\n' + self.content_  + "\n"+ "</html>"
        elif self.type == 'xml':
            self.all = "<html xmlns='http://www.w3.org/1999/xhtml'>"
        else:
            raise ValueError(f"Unknown value '{self.type}' given for argument 'type', this argument receives either 'html' or 'xml' ") 
        file_content = self.all 
        with open(filepath, 'w') as html:
            html.write(file_content)
    
class HtmlSkeleton(object):
    def __init__(self):
        #self.index = 1
        self.innards = OrderedDict()
    
    def __str__(self) -> str:
        return self.barebones

    def __repr__(self) -> str:
        return self.barebones

    def __iter__(self):
        for i in self.innards:
            yield i 

    def add(self, obj,name=None):
        if name is None:name = str(uuid.uuid4())
        marked_obj = Marker(obj,  name)
        self.innards[name] = marked_obj 
        #self.index += 1
        self.finalise()
        return self 
    
    def finalise(self):
        self.barebones = "".join(i[1].obj+"\n" for i in self.innards.items())
 
    def load_string(self, obj:str):
        str_obj = obj 
        self.add(str_obj)
    
    def load_file(self, path:str):
        with open(path, 'r') as file:
            doc = file.read(); container= ""
            for i in doc:
                container.join(i)
        self.add(container)
    
    def remove(self, name):
        del self.innards[name]
        pass 

    def wrap(self, wrapper:str,**kwargs):
        sb = ''
        for key,item in kwargs.items():
            sb += f"""{key}="{item}" """
        self.barebones = f"<{wrapper} {sb}> \n\t {self.barebones} \n\t </{wrapper}>"
        return self.barebones



    
class Marker(object):
    def __init__(self, object_to_mark, name=None) -> None:
        self.obj = object_to_mark
        self.name = name 
        if self.name is not None:
            self.name = name
        self.mark()
    
    def mark(self):
        if self.name is not None:
            self.id =  (self.obj, self.name)
        else:
            self.id =  (self.obj,)
        return self.id
    
    def __gt__(self, other):
        if type(self.name) == type(other.name):
            return self.name > other.name
        else:
            raise TypeError('Cannot compare values of different types')

    def __lt__(self, other):
        if type(self.name) == type(other.name):
            return self.name < other.name
        else:
            raise TypeError('Cannot compare values of different types')
    
    def __str__(self) -> str:
        return str(self.id) 
    
    def __repr__(self) -> str:
        return str(self.id )
    