FROM debian
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt update
RUN apt upgrade
RUN  apt install -y python2.7 python-pip
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py runserver 0.0.0.0:80
