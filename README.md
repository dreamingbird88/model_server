Model server for HuggingFace models.

### Setup steps

1. Build docker image
```bash
docker_image_name=ml_model_server
user_name=some_user
docker build \
  -t ${docker_image_name} \
  --build-arg ML_USER_NAME=${user_name} \
  -f Dockerfile . 
```
2. Start docker container
```bash
port=7860
host_dir=/mnt/new_data/huggingface_models
container_dir=/models
docker run  -it --rm -e PORT=${port} \
  --volume "${host_dir}":$container_dir \
  ${docker_image_name}
```

Notes

  * The service is available in 'http://localhost:7860'.
  * Docs is available in 'http://localhost:7860/docs'.
  
### Additional Info
  * Install dependencies via pip.
    ```bash
    pip install --no-cache-dir --upgrade -r requirements.txt
    ```
  * Start server without docker. It can use for simple debug.
    ```bash
    export MODEL_PATH=/mnt/new_data/huggingface_models # directory stores models
    uvicorn main:app --host 0.0.0.0 --port 7860
    ```
  * Get universal link from "remote.moe". It can be used in demos.
    ```bash
    ssh -R 8000:localhost:7860 remote.moe
    ```    

