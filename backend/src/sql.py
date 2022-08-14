import sqlite3
import models

DB_FILE_PATH = "../db/rating.db"


def executeQuery(baseQuery,args = None, commitable = False):
    print(__file__)
    connect = sqlite3.connect(DB_FILE_PATH)
    cursor = connect.cursor()
    result = None
    if args == None:
        cursor.execute(baseQuery)
    else:
        cursor.execute(baseQuery,args)
    if commitable:
        connect.commit()

    result = cursor.fetchall()
    connect.close()
    return result


#Player
# KeyError か SQLError
def insertPlayer(data):
    # 値チェック
    print(data["server"])
    if not models.SERVER.has_value(data["server"]):
        raise models.InvalidServerNameError

    name   = data["name"]
    server = data["server"]
    info   = data.get("info","")
    query  = "insert into players(name, server, info) values(?, ?, ?);"
    res = executeQuery(query,(name,server,info), True)
    return res

def getPlayers():
    query  = "select * from players"
    return executeQuery(query)

def getPlayerId(chara_name, server):
    query  = "select id from players where name = ? and server = ? ;"
    res = executeQuery(query,(chara_name,server))
    print(res[0][0])
    return res[0][0]

def insertBattle(data):
    # 値チェック
    print(data["server"])
    if not models.SERVER.has_value(data["server"]):
        raise models.InvalidServerNameError

    name   = data["name"]
    server = data["server"]
    info   = data.get("info","")
    side_a = data["side_a"]
    side_b = data["side_b"]
    winner = data["winner"]
    style = data["style"]
    format = data["format"]

    query  = """
        insert into battles(name, server, info, side_a, side_b, winner, style, format) 
        values(?, ?, ?, ?, ?, ?, ?, ?)
    """
    res = executeQuery(query, (name,server,info,side_a,side_b,winner,style,format), True)
    return res
