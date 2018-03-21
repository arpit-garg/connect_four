FROM python:2.7.13-wheezy
RUN pip install numpy

WORKDIR /srv/connect_four/

COPY . .

CMD python ./connect_four/connect_four.py