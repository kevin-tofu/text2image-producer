
import os
from dataclasses import dataclass
# from typing import NamedTuple

VERSION = os.getenv('VERSION', 'v0.0.1'),
AUTHOR = os.getenv('AUTHOR', 'kevin')
APP_PORT = int(os.getenv('APP_PORT', 80))

RABBITMQ_URL = os.getenv('RABBITMQ_URL', 'amqp://localhost:6380')
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
DATA_PATH = os.getenv('DATA_PATH', './temp')

@dataclass(slots=True)
class Config():
    version: str
    author: str
    app_port: int
    rabbitmq_url: str
    redis_url: str
    data_path: str
    

config_org = Config(
    VERSION,
    AUTHOR,
    APP_PORT,
    RABBITMQ_URL,
    REDIS_URL,
    DATA_PATH
)
