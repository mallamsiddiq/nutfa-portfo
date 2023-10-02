

FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /nutfa


WORKDIR /nutfa


ADD . /nutfa/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# CMD gunicorn seedtest.wsgi:application --bind 0.0.0.0:$PORT


