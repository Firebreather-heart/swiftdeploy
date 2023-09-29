from settings import settings
from html.htmlcontent import HtmlSkeleton, HtmlShell
from html.tags import Division, Header, Tag , Form, FormElement

class MarkupModel:
    def __init__(self,**kwargs):
        self.app_name  =  settings.APP_NAME # type: ignore
        self.model_info = kwargs.get("model_info", "")
        self.form_fields:dict = kwargs.get('form_fields') # type: ignore (field, input_type)
        self.pagebody = []

    def addHeader(self, header_value = settings.APP_HEADER,  ): # type: ignore
         self.header = Header(id = f"header_{self.app_name}", classname=f'header_{self.app_name}', body = header_value ).create()
    
    def addContent(self, *args):
        self.content = HtmlSkeleton()
        # if not isinstance(str, tuple(*args)):
        #     raise ValueError(f"The items to be added to the content object should be string objects")
        for item in args:
            self.content.add(item)
        self.content.wrap('div')
        return self
    
    def addFooter(self, footer_value = settings.APP_FOOTER): #type: ignore
        self.footer = Tag(name='footer', id = f'footer_{self.app_name}', classname=f'footer_{self.app_name}', body=footer_value).create()
        return self

    def createform(self):
        if self.form_fields is None:
            raise ValueError("form_fields have not been set")
        else:
            form = Form()
            for key, item in self.form_fields.items():
                form.add(FormElement(name = f'{key}', id = f"id_{key}", classname = f'class_{key}', input_type = item, label = key).make())
            return form.set_()
        
    def compile(self):
        self.addHeader()
        self.addContent(*self.pagebody)
        self.addFooter()
    
            


    def makePage(self):
        self.pageObj = HtmlShell(title=settings.APP_HEADER, sfl = [], link_css = ['./static/index.css']) # type: ignore
        self.body = HtmlSkeleton() 
        self.pagebody = [self.createform()]
        self.compile()
        self.body.add(self.header)
        self.body.add(self.content.barebones)
        self.body.add(self.footer)
        self.body.wrap('body')
        self.pageObj.insert(self.body)
        self.pageObj.to_file('./templates/index.html')
        
