from transformers import pipeline
import os
MODEL_PATH = os.environ['MODEL_PATH']

TASK_TO_KEY = {
  'text2text-generation': 'generated_text',
  'translation_en_to_zh': 'translation_text',
}

def loadModelPipeline(task: str, name: str):
  model_path = '/'.join([MODEL_PATH, name.replace('/', '--')])
  if os.path.isdir(model_path):
    model_pipeline = pipeline(task, model=model_path)
  else:
    model_pipeline = pipeline(task, model=name)
    model_pipeline.save_pretrained(model_path)
  return model_pipeline, TASK_TO_KEY[task]
