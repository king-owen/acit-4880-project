FROM python:3

RUN apt-get update
RUN apt install -y vim
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir flask
#RUN pip install --no-cache-dir os

RUN mkdir -p upload_video

#ADD https://github.com/king-owen/acit-4880-project/tree/main/acit_3495_project/upload_video/app.py /upload_video/
RUN git clone https://github.com/king-owen/acit-4880-project.git

#CMD mkdir upload_foolder && \
CMD tail -f /dev/null