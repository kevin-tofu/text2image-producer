
from src.config import config_org as config
from src.publisher import app


if __name__ == '__main__':
    
    params = {
        'prompt': 'yahoo',
        'user': None,
        'test': 1,
    }

    task = app.send_task(
        'main.prompting', [params]
    )
