
import os
from dataclasses import dataclass
from typing import Optional

APP_VERSION = os.getenv('APP_VERSION', 'v0.0.1'),
APP_MANAGER = os.getenv('APP_MANAGER', 'kevin')
APP_PORT = int(os.getenv('APP_PORT', 80))

RABBITMQ_URL = os.getenv('RABBITMQ_URL', 'amqp://localhost:6380')
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
DATA_PATH = os.getenv('DATA_PATH', './temp')
FIREBASE_URL = os.getenv('FIREBASE_URL', None)


@dataclass(slots=True)
class Config():
    app_version: str
    app_manager: str
    app_port: int
    rabbitmq_url: str
    redis_url: str
    data_path: str
    firebase_url: Optional[str]=None

config_org = Config(
    APP_VERSION,
    APP_MANAGER,
    APP_PORT,
    RABBITMQ_URL,
    REDIS_URL,
    DATA_PATH,
    FIREBASE_URL
)
