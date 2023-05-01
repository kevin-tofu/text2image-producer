
from typing import List, Optional
# from fastapi import FastAPI, Path, Query

def params_diffusion(
    prompt: str,
    user: Optional[str] = None,
    test: Optional[int] = None
):
    '''
    '''

    ret = {
        'prompt': prompt,
        'user': user,
        'test': test,
    }
    return ret

