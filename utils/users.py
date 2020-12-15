from dataclasses import dataclass
from typing import Union


@dataclass
class User:
    name: str
    age: int
    id: Union[str, None] = None
