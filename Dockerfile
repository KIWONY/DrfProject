FROM python:3.9.0

# work directory 기본 설정
WORKDIR /home/Drfproject

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

