import typing as type
from enum import Enum

class tokenType(Enum):
    INT  = b'i'
    LIST = b'l'
    DICT = b'd'
    END  = b'e'
    DELIMITOR = b':'

#---------------------------------

def tokenize(data: bytes) -> type.List:
    print("hello tokenizer")
    return []
