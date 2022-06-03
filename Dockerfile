FROM python:3.9.0

# work directory 기본 설정
WORKDIR /home/

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "stock.wsgi:application"]
