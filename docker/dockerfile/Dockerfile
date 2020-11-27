# Use an official CentOS 8 image
FROM centos:8

RUN yum update -y \
    && yum install -y python38 python38-devel gcc \
    && yum groupinstall -y "Development Tools"

RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
RUN dnf install -y langpacks-en langpacks-ko
RUN dnf install -y langpacks-en langpacks-ko

RUN mkdir /app
RUN mkdir /app/sock
RUN mkdir /app/logs
RUN mkdir /app/tmp

COPY requirements.txt /app/tmp
RUN pip3 install -r /app/tmp/requirements.txt

WORKDIR /app/animal