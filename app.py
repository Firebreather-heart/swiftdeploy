from flask import Flask, render_template,request
import settings
from flask.views import View
from model import MarkupModel


class ModelApp(MarkupModel, View):
    """
    >>>  The `ModelApp` object subclasses the `MarkupModel`, it receives a number of 
         parameters which allows it to generate html template and views for the
         the app.
         To correctly use the class you should define a function which can run 
         your model and generate prediction based on the input data.
         
         `Parameters:`
    >>>  `model_info`:str - This will hold any information you will like to display about your model
    >>>  `model_func`:function - This is the function you have defined to
         run your model, it should contain all the neccessary preprocessing step and return the model prediction.
         Note that your model function will be given an array of values corresponding to the number of objects in
         the form field.
    >>> `func_params`:dict - This is a dictionary of the parameters your function expects
    >>> `form_fields`:dict - This is a dictionary of the input fields your model takes in the format 'field':'type'. Allowed values for the type include `text,number,date,image`

         `Usage:`
         ```python
         from swiftdeploy import ModelApp 
         modelapp = ModelApp() 
         ```
         
    """
    app = Flask(__name__)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model_func = kwargs.get("model_func") 
        self.func_params = kwargs.get("func_params")
        if self.model_func is None or self.func_params is None:
            raise ValueError(f"cannot initialize {self.__class__} without model_func and func_params")
    
    def get(self):
          return render_template('./templates/index.html')

    def post(self):
          model_input = [request.args.get(key) for key,_ in self.form_fields.items()]
          for i in model_input:
               if i is None:
                    raise ValueError(f"couldn't get appropriate value for {i}, got None instead")
          predictions = self.model_func(*model_input) #model output is got here
          return f"<h1>Prediction: {predictions}</h1>"
    
    def run(self):
         self.app.add_url_rule("/",view_func=self.as_view('home'))
         self.app.run('localhost', 8000, True)
