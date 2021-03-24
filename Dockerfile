FROM python:3
ENV CUSTOM_ENV="this is my env, hi :)"

WORKDIR /usr/src/app
COPY . .
CMD ["test.py"]
ENTRYPOINT ["python3"]
