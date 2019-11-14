FROM httpd:2.4
RUN apt-get update
RUN apt-get install -y python3 python3-pip vim
RUN pip3 install htpasswd


COPY addUsers.py /usr/local/bin/
COPY removeUser.py /usr/local/bin/