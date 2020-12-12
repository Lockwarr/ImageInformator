FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /Scaleflex
COPY requirements.txt /Scaleflex/
RUN apt-get update
RUN pip install -r requirements.txt
COPY . /Scaleflex/