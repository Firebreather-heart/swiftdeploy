import sys 
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from swiftdeploy.settings import config
config.BASE_DIR = Path(__file__).resolve().parent
config.APP_NAME = 'swiftdeploy'
config.APP_HEADER = 'SwiftDeploy'
config.APP_FOOTER = 'SwiftDeploy'
from swiftdeploy.model import MarkupModel
from swiftdeploy.app import webapp



def dummy(params:list)  -> list:
    return [str(i)+"processed" for i in params]

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
                  form_fields = param_dict)
config.model = my_model

if __name__ == "__main__":
    webapp.run()