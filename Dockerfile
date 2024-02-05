FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /fampay-youtube
COPY requirements.txt /fampay-youtube/
RUN pip install -r requirements.txt
COPY . /fampay-youtube/