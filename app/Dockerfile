FROM python:3.8-slim-buster

MAINTAINER Sean


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN apt-get update && apt-get -y install git cmake
RUN apt-get update && apt-get install build-essential -y
RUN python -m pip install \
        parse \
        realpython-reader
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt install libgl1-mesa-glx -y
RUN apt-get install libglib2.0-0 -y
COPY . /app
EXPOSE 5000

ENTRYPOINT [ "python3" ]
CMD [ "app.py"]