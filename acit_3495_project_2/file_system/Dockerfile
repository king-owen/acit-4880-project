#FROM ubuntu:18.04
FROM python:3

RUN apt-get update
RUN apt install -y vim
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir flask
RUN pip install requests pyftplib
EXPOSE 21

CMD git clone https://github.com/king-owen/acit-4880-project.git && \
cd acit-4880-project/acit_3495_project_2/file_system/ && \
mkdir -p uploads && \
python ftpserver.py && \
tail -f /dev/null