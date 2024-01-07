import os
from swiftdeploy.settings import config
from swiftdeploy.html.htmlcontent import HtmlSkeleton, HtmlShell
from swiftdeploy.html.tags import Division, Header, Tag , Form, FormElement



class MarkupModel:
    """
         `Parameters:`
    >>>  `model_info`:str - This will hold any information you will like to display about your model
    >>>  `model_func`:function - This is the function you have defined to
         run your model, it should contain all the neccessary preprocessing step and return the model prediction.
         Note that your model function will be given an array of values corresponding to the number of objects in
         the form field.
    >>> `form_fields`:dict - This is a dictionary of the input fields your model takes in the format 'field':'type'. Allowed values for the type include `text,number,date,image`

         `Usage:`
         ```python
         from swiftdeploy import ModelApp 
         modelapp = ModelApp() 
         ```
         
    """
    def __init__(self,**kwargs):
        self.app_name  =  config.APP_NAME # type: ignore
        self.model_info = kwargs.get("model_info", "")
        self.form_fields:dict = kwargs.get('form_fields') # type: ignore (field, input_type)
        self.pagebody = []
        self.model_func = kwargs.get("model_func") 
        if self.model_func is None:
            raise ValueError(f"cannot initialize {self.__class__} without model_func")
        self.makePage()

    def addHeader(self, header_value = config.APP_HEADER,  ): # type: ignore
         header = Header(id = f"app-header", classname=f'app-header', body = header_value ).create()
         topdiv = Division(body=self.model_info,classname=f"app-info",id=f"app-info").create()
         self.topdiv_container = HtmlSkeleton()
         self.topdiv_container.add(header)
         self.topdiv_container.add(topdiv)

    
    def addContent(self, *args):
        self.content = HtmlSkeleton()
        # if not isinstance(str, tuple(*args)):
        #     raise ValueError(f"The items to be added to the content object should be string objects")
        for item in args:
            self.content.add(item)
        self.content.wrap('div')
        return self
    
    def addFooter(self, footer_value = config.APP_FOOTER): #type: ignore
        self.footer = Tag(name='footer', id = f'app-footer', classname=f'app-footer', body=footer_value).create()
        return self

    def createform(self):
        if self.form_fields is None:
            raise ValueError("form_fields have not been set")
        else:
            form = Form()
            for key, item in self.form_fields.items():
                if item == 'file' or item == 'image':
                    form.add(FormElement(name = f'{key}', id = f"id_{key}", classname = f'class_{key}', input_type = item, label = key, accept = 'image/*').make())
                else:
                    form.add(FormElement(name = f'{key}', id = f"id_{key}", classname = f'class_{key}', input_type = item, label = key).make())
            return form.set_()
        
    def compile(self):
        self.addHeader()
        self.addContent(*self.pagebody)
        self.addFooter()
    
            


    def makePage(self):
        self.pageObj = HtmlShell(title=config.APP_HEADER, sfl = [], link_css = ['./static/index.css']) # type: ignore
        self.body = HtmlSkeleton() 
        self.pagebody = [self.createform()]
        self.compile()
        self.body.add(self.topdiv_container.barebones)
        self.body.add(self.content.barebones)
        self.body.add(self.footer)
        self.body.wrap('body')
        self.pageObj.insert(self.body)
        if os.path.exists(os.path.join(config.BASE_DIR,'templates')):
            self.pageObj.to_file(os.path.join(config.BASE_DIR,'templates/index.html'))
        else:
            os.makedirs(os.path.join(config.BASE_DIR,'templates'), exist_ok=True)
            self.pageObj.to_file(os.path.join(config.BASE_DIR,'templates/index.html'))
        if os.path.exists(os.path.join(config.BASE_DIR,'static')):
            with open(os.path.join(config.BASE_DIR,'static/index.css'), 'w') as f:
                f.write(config.CSS)
        else:
            os.makedirs(os.path.join(config.BASE_DIR,'static'), exist_ok=True)
            with open(os.path.join(config.BASE_DIR,'static/index.css'), 'w') as f:
                f.write(config.CSS)
        
