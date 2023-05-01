
import celery 
from src.config import config_org as cfg


app = celery.Celery(
    __name__,
    broker=cfg.rabbitmq_url,
    backend=cfg.redis_url
)
