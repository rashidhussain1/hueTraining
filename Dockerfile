FROM python:3.8
ENV PYTHONUNBUFFERED=1
COPY . /django
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt