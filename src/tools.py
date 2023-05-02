import os
import time
from src.logconf import mylogger
logger = mylogger(__name__)

def get_file_extension(fname: str):
    # fname_without_ext = os.path.splitext(fname)[0]
    extension = os.path.splitext(fname)[-1][1::]
    return extension


def remove_file(path_file: str, sleep_sec: int=60) -> None:

    # logger.info('timer')
    time.sleep(sleep_sec)
    if os.path.exists(path_file) == True:
        os.unlink(path_file)
        logger.info(f'removed : {path_file}')
