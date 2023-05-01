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
