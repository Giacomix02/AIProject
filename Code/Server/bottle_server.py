from bottle import route, run
from joblib import load
import sklearn.pipeline as Pipeline
from NLTKVectorizer import NLTKVectorizer

NLTKVectorizer = NLTKVectorizer()

model_Pipeline: Pipeline


@route("/load_server")
def load_server():
    # model_Pipeline = load('../dump/model.joblib') #official model
    model_Pipeline = load('../dump/test.joblib')  # test model
    if model_Pipeline is not None:
        return "model Loaded"


run(host='localhost', port=8080, debug=True)
