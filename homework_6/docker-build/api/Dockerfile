FROM tiangolo/uwsgi-nginx-flask:python3.9

ENV PYTHONBUFFERED=1

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .