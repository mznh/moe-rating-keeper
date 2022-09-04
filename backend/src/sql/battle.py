import sqlite3
import models

import sql.base as base

def insert(side_a_id,side_b_id,winner_id):
    style = ""
    format = ""

    query  = """
        insert into battles(name, server, info, side_a, side_b, winner, style, format) 
        values(?, ?, ?, ?, ?, ?, ?, ?)
    """
    res = base.executeQuery(query, ("","","",side_a_id,side_b_id,winner_id,style,format), True)
    return res

def selectByKey(key:str):
    query = """
        select 
          (select name from players where id = side_a) as side_a_name,
          (select name from players where id = side_b) as side_b_name,
          (select name from players where id = winner) as winner_name
        from battles as btl
        inner join (
          select 
            *
          from players
          where key = ?
        ) as pls
        on btl.side_a = pls.id or btl.side_b = pls.id
    """
    res = base.executeQuery(query,(key,))
    print(res)
    return res


