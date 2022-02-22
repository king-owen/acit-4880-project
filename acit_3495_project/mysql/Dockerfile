FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y mysql-server

EXPOSE 3306
#RUN
CMD apt install -y sudo && \
service mysql start && \
echo "root:root" | chpasswd && \
mysql -e "create database video CHARACTER SET utf8 COLLATE utf8_bin;" && \
mysql video -e "create table videos (ID int not null auto_increment, name varchar(255) not null, path varchar(255) not null, primary key (id));" && \
tail -f /dev/null
#ENV MYSQL_ROOT_PASSWORD video
#ENV MYSQL_DATABASE video
#ENV MYSQL_USER video
#ENV MYSQL_PASSWORD video

#-p${MYSQL_ROOT_PASSWORD}