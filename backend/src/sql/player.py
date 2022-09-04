import sqlite3
import models

import sql.base as base

#Player
# KeyError か SQLError
def insert(data,key,token):
    # 値チェック
    print(data["server"])
    if not models.SERVER.has_value(data["server"]):
        raise models.InvalidServerNameError
    name   = data["name"]
    server = data["server"]
    info   = data.get("info","")
    query  = """
    insert into players(name, key,token, server, info) values(?, ?, ?, ?, ?);"""

    print(name,key,token,server,info)
    res = base.executeQuery(query,(name,key,token,server,info), True)
    return res

def get(key:str):
    player_id = base.getIdFromKey(key)

    query  = """
    select 
      *
    from  players 
    where key = ?
    """
    print(query)
    print(key)
    res =  base.executeQuery(query,(key,))
    print(res[0])
    return res[0]

def getPlayerId(chara_name, server):
    query  = "select id from players where name = ? and server = ? ;"
    res = base.executeQuery(query,(chara_name,server))
    print(res[0]["id"])
    return res[0]["id"]

def getPlayers():
    query  = "select * from players"
    return base.executeQuery(query)

