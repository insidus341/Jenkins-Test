FROM python:3.9

RUN apt-get update && apt-get install python3-pip -y 

COPY /deployment/requirements.txt /app/deployment/requirements.txt

RUN pip3 install -r /app/deployment/requirements.txt

WORKDIR /app

COPY /app .

WORKDIR /app

CMD ["python3", "app.py"]