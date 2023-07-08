# Dockerfile, Image, Container
FROM python:3.11-alpine3.15
WORKDIR /assign1
COPY . /assign1
RUN pip install -r requirements.txt
EXPOSE 8000
CMD  python ./main.py