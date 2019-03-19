FROM alpine
MAINTAINER bergpb
RUN mkdir /home/lisapi
RUN FLASK_ENV=production
COPY . /home/lisapi
WORKDIR /home/lisapi
RUN apk add --no-cache alpine-sdk python3 python3-dev libevent-dev openssl-dev libffi-dev && \
    pip3 install --upgrade pip setuptools pipenv && \
    pipenv install --system --deploy
ENTRYPOINT gunicorn -w 4 -b 0.0.0.0:5000 app:app
