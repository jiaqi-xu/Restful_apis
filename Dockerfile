FROM python:3.6
MAINTAINER Jiaqi Xu <jxu930405@gmail.com>

COPY . /opt/restful_apis
WORKDIR /opt/restful_apis

RUN pip install -r requirements.txt

EXPOSE 8080

CMD python runner.py