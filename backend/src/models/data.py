from typing import Union
from pydantic import BaseModel
from enum import Enum


class Player(BaseModel): 
    name:  str
    server:  str
    info:  Union[str, None]

class Battle(BaseModel): 
    name:  str
    server:  str
    info:  Union[str, None]
    side_a: int
    side_b: int
    winner: int
    style: int
    format: Union[str, None]

class Style(BaseModel): 
    name:  str
    info:  Union[str, None]

class Format(BaseModel): 
    name:  str
    info:  Union[str, None]

class RatingLog(BaseModel): 
    player_id:  int
    style: int 
    rating:  float 
    sigma: float

class SERVER(Enum):
    DIAMOND = "DIAMOND"
    PEARL = "PEARL"
    EMERALD = "EMERALD"
    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

class InvalidServerNameError(Exception):
    pass


