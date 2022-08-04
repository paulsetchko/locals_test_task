FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./src /src
WORKDIR /src
RUN pip install -r requirements.txt
