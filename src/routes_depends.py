from typing import List, Optional
# from fastapi import FastAPI, Path, Query
from dataclasses import dataclass

@dataclass
class params_diffuser:
    prompt: str
    user: Optional[str] = None
    test: Optional[int] = None
