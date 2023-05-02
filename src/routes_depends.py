from dataclasses import dataclass
from typing import List, Optional
# from fastapi import FastAPI, Path, Query


@dataclass
class params_diffuser:
    prompt: str
    user: Optional[str] = None
    test: Optional[int] = None


