FROM alpine
MAINTAINER bergpb
RUN mkdir /home/lisapi
ENV FLASK_ENV=production
ENV FLASK_APP=app
COPY . /home/lisapi
WORKDIR /home/lisapi
RUN apk add --no-cache alpine-sdk python3 python3-dev libevent-dev openssl-dev libffi-dev && \
    pip3 install --upgrade pip setuptools && pip3 install -r requirements.txt
RUN flask db-drop && flask db-seed
CMD gunicorn -b 0.0.0.0:5000 --worker-class eventlet -w 1 run:app
