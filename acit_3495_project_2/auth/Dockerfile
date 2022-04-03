FROM python:3

RUN apt-get update
RUN pip install flask

CMD git clone https://github.com/king-owen/acit-4880-project.git && \
sleep 1m && \
python acit-4880-project/acit_3495_project_2/auth/login_files/main.py && \
tail -f /dev/null