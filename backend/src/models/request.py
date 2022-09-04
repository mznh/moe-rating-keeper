from typing import Union
from pydantic import BaseModel
from enum import Enum

class CreatePlayer(BaseModel):
    name: str
    server: str

class RecordBattle(BaseModel): 
    side_a_name:  str
    side_a_token:  str
    side_b_name:  str
    side_b_token:  str
    winner_token: str

class GetBattle(BaseModel):
    name:str
    key:str

