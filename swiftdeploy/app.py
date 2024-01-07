import os
from flask import Flask, render_template,request
from flask.views import MethodView
from swiftdeploy.settings import config
from flask import abort

template = os.path.join(config.BASE_DIR, 'templates')
static = os.path.join(config.BASE_DIR, 'static')
webapp = Flask(__name__, template_folder=template, static_folder=static)



         
class WebViews(MethodView):
     """
     Class representing the web views for the application.

     Methods:
     - get: Handles the GET request and renders the 'index.html' template.
     - post: Handles the POST request, validates the input, and returns the model predictions.
     """

     def get(self):
          """
          Handles the GET request and renders the 'index.html' template.

          Returns:
          - The rendered 'index.html' template.
          """
          return render_template('index.html')

     def post(self):
          """
          Handles the POST request, validates the input, and returns the model predictions.

          Returns:
          - The prediction result as an HTML string.
          """
          model_input = [request.form.get(key) for key,_ in config.model.form_fields.items()]
          for i in model_input:
               if i is None:
                    abort(403)  # Return a 403 Forbidden error if any input is missing
               predictions = config.model.model_func(model_input) # Model output is obtained here
          return f"<h1>Prediction: {predictions}</h1>"


webapp.add_url_rule("/",view_func=WebViews.as_view('home'))