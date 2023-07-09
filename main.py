'''

source activate huggingface
export MODEL_PATH=/mnt/new_data/huggingface_models
uvicorn main:app --host 0.0.0.0 --port 7860

'''
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import Union

app = FastAPI()

from pipeline_io import loadModelPipeline, TASK_TO_KEY
current_model_name = 'google/flan-t5-small'
model_pipeline, predict_key = loadModelPipeline('text2text-generation', 'google/flan-t5-small')

@app.get("/infer/")
async def get_infer(input: str):
  return {'output': model_pipeline(input)[0][predict_key]}

@app.get("/model/")
async def change_model(task: str = "text2text-generation", name: str = "google/flan-t5-small"):
  global current_model_name, model_pipeline, predict_key
  if not task in TASK_TO_KEY:
    raise HTTPException(status_code=404, detail=f'Not support {task}.')
  if current_model_name == name:
    return {'output': f'Current model is {name}.'}
  try:
    model_pipeline, predict_key = loadModelPipeline(task, name)
  except OSError:
    return {'output': f'Invalid model {name}. Current model {current_model_name}.'}
  current_model_name = name
  return {'output': f'Change model to {name}.'}

app.mount("/", StaticFiles(directory="static", html=True), name="static")
@app.get("/")
def index() -> FileResponse:  # cannot use async 
  return FileResponse(path='/app/static/index.html', media_type="text/html")
