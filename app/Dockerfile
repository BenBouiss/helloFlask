FROM python:3.8-slim-buster

LABEL Maintainer="Ben"


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev &&\
    apt-get install -y libpq-dev
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app
EXPOSE 8000
 
ENTRYPOINT [ "python" ]

CMD [ "src/app.py" ]