import hashlib
import random
import models
import sql
import service.rating as rating


def add(data: models.Player):
    print("player insert")
    player = data.dict()
    # key,token を生成
    key = generatePlayerKey(player)
    token = generatePlayerToken(player)

    # Playerを登録
    sql.player.insert(player,key,token)
    # PlayerIdを取得
    playerId = sql.player.base.getIdFromKey(key)
    defMu = rating.RatingConstConfig.mu.value
    defSigma = rating.RatingConstConfig.sigma.value

    for style in sql.style.getStyles():
        sql.rating.insertRating( playerId,style["id"],defMu,defSigma)
        sql.rating.getRatingDataById(playerId,style["id"])

    return {
        "status": "ok", 
        "player":{
            "name":player["name"],
            "key": key,
            "token": token,
            "server": player["server"]
        }
    }
        

def get(key:str):
    print("get")
    print( sql.player.get(key))
    return sql.player.get(key)

def generatePlayerKey(player):
    row_str = str(int(random.uniform(0,200)))+player["name"]+player["server"]
    return  hashlib.md5(row_str.encode()).hexdigest()

def generatePlayerToken(player):
    row_str = str(int(random.uniform(0,200)))+player["name"]+player["server"]
    return hashlib.md5(row_str.encode()).hexdigest()[0:4]

