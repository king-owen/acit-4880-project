FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y mysql-server

EXPOSE 3306

CMD apt-get update && \
apt install -y sudo vim && \
awk '!/bind-address/' /etc/mysql/mysql.conf.d/mysqld.cnf > temp && mv temp /etc/mysql/mysql.conf.d/mysqld.cnf && \
service mysql start && \
echo "root:root" | chpasswd && \
mysql -e "create database video CHARACTER SET utf8 COLLATE utf8_bin;" && \
mysql video -e "create table videos (ID int not null auto_increment, name varchar(255) not null, path varchar(255) not null, primary key (id));" && \
mysql video -e "GRANT ALL ON video.* TO 'root'@'%' IDENTIFIED BY 'root';" && \
mysql video -e "GRANT ALL ON video.* TO 'root'@'%' IDENTIFIED BY 'root';" && \
mysql video -e "FLUSH PRIVILEGES;" && \ 
tail -f /dev/null