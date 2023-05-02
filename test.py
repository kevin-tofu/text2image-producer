
from src.config import config_org as config
from src.publisher import app
from celery.result import AsyncResult


if __name__ == '__main__':
    
    params = {
        'prompt': 'yahoo',
        'user': None,
        'test': 1,
    }

    res = app.send_task(
        'prompt', 
        args=[],
        kwargs=params
    )

    print('res:', res, type(res))
    # tasks = app.control.inspect()
    # print("res.get():", res.get())
    # print("tasks:", tasks)
    # print("tasks.active():", tasks.active())
    
    import time
    for loop in range(100):
        result = AsyncResult(res.id)
        time.sleep(3)
        print("res.id:", res.id)
        print('status:', result.status, result.ready())  # PENDING/FAILURE/SUCCESS
        print('info:', result.info)
        if result.ready():
            break

        
