FROM mysql

ENV MYSQL_ROOT_PASSWORD video
ENV MYSQL_DATABASE video
ENV MYSQL_USER video
ENV MYSQL_PASSWORD video

#-p${MYSQL_ROOT_PASSWORD}
RUN sudo systemctl start mysql
RUN mysql -u root -e "create database video CHARACTER SET utf8 COLLATE utf8_bin"
RUN mysql -u root video -e "create table [if not exists] videos (ID int not null auto_increment, name varchar(255) not null, path varchar(255) not null, primary key (id));"
