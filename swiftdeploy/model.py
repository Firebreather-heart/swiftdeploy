import os
from swiftdeploy.settings import config
from swiftdeploy.html.htmlcontent import HtmlSkeleton, HtmlShell
from swiftdeploy.html.tags import Division, Header, Tag , Form, FormElement



class MarkupModel:
    """
    This class represents a markup model for a web application.

    Parameters:
    - `model_info` (str): Information to display about the model.
    - `model_func` (function): The function that runs the model and returns the prediction.
    - `form_fields` (dict): A dictionary of input fields the model takes, in the format 'field':'type'.
                            Allowed types include 'text', 'number', 'date', and 'image'.

    Usage:
    1. Import the `ModelApp` class from the `swiftdeploy` module.
    2. Create an instance of `ModelApp`.
    3. Use the instance to interact with the markup model.

    Example:
    ```python
    from swiftdeploy import ModelApp

    modelapp = ModelApp()
    ```

    """

    def __init__(self, **kwargs):
        self.app_name = config.APP_NAME
        self.model_info = kwargs.get("model_info", "")
        self.form_fields: dict = kwargs.get('form_fields')
        self.pagebody = []
        self.model_func = kwargs.get("model_func")
        if self.model_func is None:
            raise ValueError(f"Cannot initialize {self.__class__} without model_func")
        self.makePage()

    def addHeader(self, header_value=config.APP_HEADER):
        """
        Add a header to the markup model.

        Parameters:
        - `header_value` (str): The value of the header.

        """
        header = Header(id=f"app-header", classname=f'app-header', body=header_value).create()
        topdiv = Division(body=self.model_info, classname=f"app-info", id=f"app-info").create()
        self.topdiv_container = HtmlSkeleton()
        self.topdiv_container.add(header)
        self.topdiv_container.add(topdiv)

    def addContent(self, *args):
        """
        Add content to the markup model.

        Parameters:
        - `args` (str): The content to be added.

        Returns:
        - `self`: The instance of the markup model.

        """
        self.content = HtmlSkeleton()
        for item in args:
            self.content.add(item)
        self.content.wrap('div')
        return self

    def addFooter(self, footer_value=config.APP_FOOTER):
        """
        Add a footer to the markup model.

        Parameters:
        - `footer_value` (str): The value of the footer.

        Returns:
        - `self`: The instance of the markup model.

        """
        self.footer = Tag(name='footer', id=f'app-footer', classname=f'app-footer', body=footer_value).create()
        return self

    def createform(self):
        """
        Create a form for the markup model.

        Returns:
        - `form`: The created form.

        Raises:
        - `ValueError`: If form_fields have not been set.

        """
        if self.form_fields is None:
            raise ValueError("form_fields have not been set")
        else:
            form = Form()
            for key, item in self.form_fields.items():
                if item == 'file' or item == 'image':
                    form.add(FormElement(name=f'{key}', id=f"id_{key}", classname=f'class_{key}', input_type=item, label=key, accept='image/*').make())
                else:
                    form.add(FormElement(name=f'{key}', id=f"id_{key}", classname=f'class_{key}', input_type=item, label=key).make())
            return form.set_()

    def compile(self):
        """
        Compile the markup model.

        This method adds the header, content, and footer to the markup model.

        """
        self.addHeader()
        self.addContent(*self.pagebody)
        self.addFooter()

    def makePage(self):
        """
        Create the markup model page.

        This method creates the HTML structure of the markup model page and saves it to a file.

        """
        self.pageObj = HtmlShell(title=config.APP_HEADER, sfl=[], link_css=['./static/index.css'])
        self.body = HtmlSkeleton()
        self.pagebody = [self.createform()]
        self.compile()
        self.body.add(self.topdiv_container.barebones)
        self.body.add(self.content.barebones)
        self.body.add(self.footer)
        self.body.wrap('body')
        self.pageObj.insert(self.body)
        if os.path.exists(os.path.join(config.BASE_DIR, 'templates')):
            self.pageObj.to_file(os.path.join(config.BASE_DIR, 'templates/index.html'))
        else:
            os.makedirs(os.path.join(config.BASE_DIR, 'templates'), exist_ok=True)
            self.pageObj.to_file(os.path.join(config.BASE_DIR, 'templates/index.html'))
        if os.path.exists(os.path.join(config.BASE_DIR, 'static')):
            with open(os.path.join(config.BASE_DIR, 'static/index.css'), 'w') as f:
                f.write(config.CSS)
        else:
            os.makedirs(os.path.join(config.BASE_DIR, 'static'), exist_ok=True)
            with open(os.path.join(config.BASE_DIR, 'static/index.css'), 'w') as f:
                f.write(config.CSS)
        
