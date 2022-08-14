#!/usr/bin/env python3

from fastapi import FastAPI
from pydantic import BaseModel

import models
import sql

app = FastAPI()

api_version = "/v1"

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get(api_version + "/items/{item_id}")
def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# Player

@app.get(api_version + "/players")
def get_players():
    res = sql.getPlayers()
    print(res)
    return res

@app.post(api_version + "/player")
def create_player(player :models.Player):
    print(player)
    res = sql.insertPlayer(player.dict())
    print(res)
    return {"status": "ok"}

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

