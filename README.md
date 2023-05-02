# text2image-producer

## SetUp

### Build using Docker

```bash

docker build . -t text2image-producer

```

### Build using Poetry

```bash

poetry install

```

### How to Run using Docker

```bash
docker run -it -d --rm \
   -e RABBITMQ_URL=amqp://localhost:6380 \
   -e REDIS_URL=redis://localhost:6379/0 \
   --name producer \
   text2image-producer
```

### How to run using Poetry

```bash

poetry run python server.py --port 3333

```

## Environment Variables

| Name | type | Example | Description |
| --- | --- | --- | --- |
| APP_VERSION | str | {CI_COMMIT_SHORT_SHA} |  |
| APP_MANAGER | str | 'myname' |  |
| APP_PORT | int | 8080 |  |
| RABBITMQ_URL | str | 'amqp://localhost:6380' |  |
| REDIS_URL | str | 'redis://localhost:6379/0' |  |
| DATA_PATH | str | './temp' |  |
| FIREBASE_URL | str | '' |  |
