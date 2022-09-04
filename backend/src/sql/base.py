import sqlite3

DB_FILE_PATH = "../db/rating.db"

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def executeQuery(baseQuery,args = None, commitable = False):
    connect = sqlite3.connect(DB_FILE_PATH)
    connect.set_trace_callback(print)
    connect.row_factory = dict_factory

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

def validateNameAndToken(name:str,token:str):
    base_query = "select * from players where name = ? and token = ? "
    res = executeQuery(base_query,(name,token))
    print("=== check player's token")
    print("= name  : " + name)
    print("= token : " + token)
    print("==--------------------==")
    if len(res) != 0:
        print("= result:  True")
        print("========================")
        return True
    else :
        print("= result:  False")
        print("========================")
        return False

def getKeyFromNameAndToken(name:str,token:str):
    base_query = "select key from players where name = ? and token = ? "
    res = executeQuery(base_query,(name,token))
    if len(res) != 0 :
        return res[0]["key"]
    else:
        return False

def getIdFromNameAndToken(name:str,token:str):
    base_query = "select id from players where name = ? and token = ? "
    res = executeQuery(base_query,(name,token))
    if len(res) != 0 :
        return res[0]["id"]
    else:
        return False

def getIdFromKey(key:str):
    base_query = "select id from players where key = ? "
    res = executeQuery(base_query,(key,))
    if len(res) != 0 :
        return res[0]["id"]
    else:
        return False




