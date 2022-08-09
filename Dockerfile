FROM python:3.9.0

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# work directory 기본 설정
WORKDIR /home/DrfProject

COPY requirements.txt  /home/DrfProject

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /home/DrfProject


