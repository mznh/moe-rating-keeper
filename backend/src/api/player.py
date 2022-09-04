from fastapi import APIRouter
import hashlib
import random

import models
import service

api= APIRouter()

# Player
# name,server,infoをもとにプレイヤー新規登録
@api.post("/player")
def create_player(player :models.Player):
    print("プレイヤーを新規登録")
    print(player)
    # プレイヤー新規登録
    return service.player.add(player)

# keyをもとにプレイヤーの詳細な情報を取得
@api.get("/player")
def get_player(key:str):
    # プレイヤーの詳細を取得して返す    
    print("プレイヤーの詳細を取得")
    return service.player.get(key)

@api.delete("/player")
def delete_player(key:str):
    # プレイヤーの詳細を取得して返す    
    print("プレイヤーを削除")
    return ""


