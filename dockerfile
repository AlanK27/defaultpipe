FROM python:3.7.12-slim-buster

RUN apt-get update
RUN apt-get -y install vim unzip curl postgresql postgresql-contrib postgresql-client libpq-dev gcc default-libmysqlclient-dev redis-server nginx less
RUN apt-get -y install redis-server

# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# RUN unzip awscliv2.zip
# RUN ./aws/install

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /data
RUN mkdir /tmp/supervisor_logs

COPY supervisor/supervisord.conf /etc/supervisord.conf

# COPY .aws /root/.aws
ENV PYTHONPATH="/${PYTHONPATH}"

COPY src /src

COPY start.sh ./start.sh
RUN chmod +x start.sh

CMD bash start.sh && supervisord -n
