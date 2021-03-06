# Start with a Python image.
FROM python:latest

# Install some necessary things.
RUN apt-get update
RUN apt-get install -y libssl-dev redis-server

# Copy all our files into the image.
RUN mkdir /code
WORKDIR /code
COPY . /code/

# Install our requirements.
RUN pip install -U pip
RUN pip install -Ur requirements.txt
RUN pip install uwsgi

RUN python /code/manage.py migrate
RUN python /code/manage.py collectstatic --noinput

EXPOSE 8000

# Specify the command to run when the image is run.
# CMD python /code/manage.py runserver 0.0.0.0:8000
CMD redis-server --daemonize yes && celery worker -A capsoul -E --detach && uwsgi --http=0.0.0.0:8000 --chdir /code --wsgi-file capsoul/wsgi.py --master --processes 4 --threads 2
