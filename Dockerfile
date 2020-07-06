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

ENV PORT 80

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 myproject.wsgi:application