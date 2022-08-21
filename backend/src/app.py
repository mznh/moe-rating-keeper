#!/usr/bin/env python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import hashlib
import random



import models
import sql

app = FastAPI()
api_version = "/v1"
# for cors setting
origins = [
    "http://localhost:4200",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Players
@app.get(api_version + "/players")
def get_players():
    res = sql.getPlayers()
    print(res)
    return res

# Player
@app.get(api_version + "/player")
def get_player(key:str):
    print(key)
    res = sql.getPlayer(key)
    print(res)
    return res

@app.post(api_version + "/player")
def create_player(player :models.Player):
    data = player.dict()
    key_string = str(int(random.uniform(0,200)))+data["name"]+data["server"]
    data["key"] = hashlib.md5(key_string.encode()).hexdigest()
    res = sql.insertPlayer(data)
    print(key_string)
    #要エラー処理
    print(res)
    return {"status": "ok", "key": data["key"]}

@app.get(api_version + "/player_id")
def get_player_id(name:str, server:str):
    print(name,server)
    res = sql.getPlayerId(name,server)
    print(res)
    return res

@app.post(api_version + "/battle")
def create_battle(battle :models.Battle):
    print(battle)
    return {"hoge": "huga"}

@app.post(api_version + "/style")
def create_style(style :models.Style):
    print(style)
    return {"hoge": "huga"}

@app.post(api_version + "/format")
def create_format(format :models.Format):
    print(format)
    return {"hoge": "huga"}

