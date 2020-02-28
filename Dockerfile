FROM python:3.6-slim-stretch

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /root/test_prediction

CMD cd /root/test_prediction && \
    python3 app.py