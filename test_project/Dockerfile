FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python python-pip

RUN pip intall flask

COPY main.py /opt/

ENTRYPOINT FLASK_APP=/opt/main.py flask run --host:0.0.0.0 --port=8080