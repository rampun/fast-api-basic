FROM python:3.8

WORKDIR /fast-api-basic

COPY requirements.txt .
COPY ./src ./src

RUN pip install -r requirements.txt

CMD ["python","./src/main.py"]