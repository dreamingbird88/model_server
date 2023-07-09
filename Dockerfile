# Use the official Python 3.9 image
FROM python:3.9
VOLUME /models

ARG ML_USER_NAME

RUN useradd -m -u 1000 $ML_USER_NAME
USER $ML_USER_NAME

ENV HOME=/home/$ML_USER_NAME \
  PATH=/home/$ML_USER_NAME/.local/bin:$PATH \
  MODEL_PATH=/models \
  PORT=7860
COPY --chown=$ML_USER_NAME . $HOME/app
RUN pip install --no-cache-dir --upgrade -r $HOME/app/requirements.txt

WORKDIR $HOME/app
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
EXPOSE $PORT
