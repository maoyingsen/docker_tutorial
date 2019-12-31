from alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip \
    && pip3 install --no-cache-dir pipenv 

WORKDIR /app

COPY . /app

#pipenv lock --requirements > requirements.txt
RUN pip3 --no-cache-dir install -r requirements.txt                                                                          

EXPOSE 8000

ENTRYPOINT  ["python3"]

CMD ["app.py"]