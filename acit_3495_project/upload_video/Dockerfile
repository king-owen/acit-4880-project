FROM python:3

RUN apt-get update
RUN apt install -y vim
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir flask requests pyftplib
#socket, tqdm
#RUN pip install --no-cache-dir os

#RUN mkdir -p upload_video

#ADD https://github.com/king-owen/acit-4880-project/tree/main/acit_3495_project/upload_video/app.py /upload_video/
#RUN git clone https://github.com/king-owen/acit-4880-project.git
#RUN git pull /acit-4880-project

#WORKDIR /acit-4880-project/acit_3495_project/upload_video

#CMD mkdir upload_foolder && \
#CMD python /acit-4880-project/acit_3495_project/upload_video/app.py && \ 
#tail -f /dev/null
CMD git clone https://github.com/king-owen/acit-4880-project.git && \
mkdir -p /acit-4880-project/acit_3495/upload_folder/upload_folder && \
python acit-4880-project/acit_3495_project/upload_video/app.py && \
tail -f /dev/null