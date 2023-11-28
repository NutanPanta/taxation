FROM python:3.10-buster

RUN apt-get update && apt-get install  postgresql-client gettext gnupg2 wget -y

RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get -y update

RUN apt-get install postgresql-14 -y

# Add a work directory
WORKDIR /opt/taxation

RUN mkdir -p /var/log/taxation

RUN apt-get update && apt-get install -y postgresql-client

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD /bin/sh -c ./start.sh
