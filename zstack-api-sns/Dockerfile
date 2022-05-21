FROM python:3.7-slim
WORKDIR /code
COPY ./zstack_api_sns.py ./

RUN python -m pip install --upgrade pip
RUN pip install flask==2.0.1
RUN pip install requests

ENV FLASK_APP=zstack_api_sns.py
ENV FLASK_ENV=development

CMD flask run --host=0.0.0.0 
