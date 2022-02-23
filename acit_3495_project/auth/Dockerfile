FROM python:3

RUN apt-get update
RUN pip install flask flask-sqlalchemy flask-login json

CMD git clone https://github.com/king-owen/acit-4880-project.git && \
cd ./acit_3495_project/auth/login_files && \
python main.py && \
tail -f /dev/null