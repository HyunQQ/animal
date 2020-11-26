# Use an official CentOS 8 image
FROM centos:8

RUN yum update -y \
    && yum install -y python38 python38-devel gcc \
    && yum groupinstall -y "Development Tools"


RUN localedef -f UTF-8 -i ko_KR ko_KR.utf8 && ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
ENV LC_ALL ko_KR.UTF-8
ENV LANG ko_KR.UTF-8

RUN mkdir /app/sock