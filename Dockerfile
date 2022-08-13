FROM python:3.10
ENV BASEDIRECTORY=/home/app/weather_app_demo
RUN adduser user
RUN mkdir -p $BASEDIRECTORY
RUN mkdir -p /home/app/static
RUN mkdir -p /home/app/media
WORKDIR $BASEDIRECTORY
ENV PYTHONUNBUFFERED 1
COPY . .
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt