FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
    openssh-server \
    python3 \
    python3-pip \
    && pip3 install --upgrade pip

RUN mkdir /var/run/sshd

# for flask web server
EXPOSE 8080

ADD . /app
WORKDIR /app

# This is the runtime command
RUN pip3 install --user -r requirements.txt

CMD python3 app.py



