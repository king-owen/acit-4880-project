#FROM ubuntu:18.04
FROM python:3

RUN apt-get update
RUN apt install -y vim
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir flask
RUN pip install requests pyftplib
EXPOSE 21
#socket, tqdm
#RUN echo "root:password" | chpasswd
#RUN git clone https://github.com/king-owen/acit-4880-project.git
#WORKDIR /acit-4880-project/acit_3495_project/file_system/
#RUN mkdir -p uploads
#RUN chmod 777 uploads

#EXPOSE 22 80

CMD git clone https://github.com/king-owen/acit-4880-project.git && \
cd acit-4880-project/acit_3495_project/file_system/ && \
mkdir -p uploads && \
python ftpserver.py && \
#python acit-4880-project/acit_3495_project/file_system/ftpserver.py && \
#mkdir -p uploads && \
#chmod 777 uploads && \
tail -f /dev/null