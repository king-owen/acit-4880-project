FROM python:3

RUN apt-get update
RUN apt install -y vim
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir flask requests pyftplib mysql-connector-python

CMD git clone https://github.com/king-owen/acit-4880-project.git && \
mkdir -p /acit-4880-project/acit_3495_project/video_streaming/static && \
sleep 1m && \
python acit-4880-project/acit_3495_project/video_streaming/app.py && \
tail -f /dev/null