FROM python:3.9

RUN apt-get update && apt-get install python3-pip -y 

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

WORKDIR /app

COPY /app .

WORKDIR /app

CMD ["python3", "app.py"]