FROM python:3.7-slim
WORKDIR /code
COPY ./app_server_api_flask.py ./

RUN python -m pip install --upgrade pip
RUN pip install flask==2.0.1
RUN pip install requests

ENV FLASK_APP=app_server_api_flask.py 
ENV FLASK_ENV=development

CMD flask run --host=0.0.0.0 
