import sys 
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from swiftdeploy.settings import config
config.BASE_DIR = Path(__file__).resolve().parent.parent

from swiftdeploy.model import MarkupModel

from pathlib import Path
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
    'cv':'file'
}

my_app = MarkupModel(model_info = "A dummy model you will really like", model_func = dummy, 
                  form_fields = param_dict)
config.model = my_app

if __name__ == "__main__":
    webapp.run()