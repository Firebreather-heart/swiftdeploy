# Swiftdeploy

Swiftdeploy is a python package that allows you to add a flask web application as a wrapper to your machine learning models. It is most helpful for machine learing developers who don't know how to build web apps. All you need to do is to create your model and add a function that processes the data for your model. Swiftdeploy will take care of the rest.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install Swiftdeploy, run this command in your terminal:

```sh
$ pip install swiftdeploy
```

## Usage

Using swiftdeploy is quite easy and will be demonstrated with an example

```python
import sys 
from pathlib import Path

from swiftdeploy.settings import config
config.BASE_DIR = Path(__file__).resolve().parent #set the base directory of the project
config.APP_NAME = 'swiftdeploy'
config.APP_HEADER = 'SwiftDeploy'
config.APP_FOOTER = 'SwiftDeploy'


from swiftdeploy.model import MarkupModel #import the MarkupModel class
from swiftdeploy.app import webapp # import the webapp which is a flask app


#Create a fucntion that will process the data for your model, feed the model and return the result
def dummy(params:list)  -> list:
    return [str(i)+"processed" for i in params]

#Create a dictionary of the parameters you want to collect from the user, note that the values in the dict should match the html input types

param_dict = {
    "gender":"text",
    "age": "number",
    "height": "number",
    "weight": "number",
    "married": "text",
    "educated": "true",
    'picture': 'image',
    'cv':'file',
    'wealthy':'text'
}

my_model = MarkupModel(model_info = "A dummy model you will really like", model_func = dummy, 
                  form_fields = param_dict) #create an instance of the MarkupModel class
config.model = my_model  #set the model to the config object, this is important for the webapp to work

if __name__ == "__main__":
    webapp.run()    #run the webapp, this will start the flask server on port 5000, you can change the run parameters to suit your needs, e.g webapp.run(host="localhost", port=8080, debug=True)
```

You can visit the webapp at http://localhost:5000 in your browser

