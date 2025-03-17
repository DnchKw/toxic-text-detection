from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import joblib
from fastapi.responses import FileResponse, HTMLResponse
from tokenizer import tokenize




model = joblib.load('model/model_pipeline.joblib')

def test():
    return model.predict(['I love you'])

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get('/static/{file_name}')
def serve_static(file_name: str):
    return FileResponse(f'frontend/{file_name}')

@app.get('/')
def read_index():
    with open('frontend/index.html', 'r') as f:
        return HTMLResponse(content=f.read())

@app.get('/predict/{text}')
def model_predict(text: str):

    return model.predict([text])[0]