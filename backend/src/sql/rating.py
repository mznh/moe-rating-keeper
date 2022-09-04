import sqlite3
import models

import sql.base as base

def insertRating(player_id,style,new_rate,new_sigma):
    print(player_id,style,new_rate,new_sigma)
    query  = """
        insert into 
        rating_logs(player_id, style, rating, sigma) 
        values(?, ?, ?, ?)
    """
    res = base.executeQuery(query, (player_id,style,new_rate,new_sigma), True)
    return res


def getRatingDataById(player_id:int,style_id:int):
    query = """
        select 
          player_id,
          style,
          rating,
          sigma
        from rating_logs
        where 
            player_id = ?  and style = ?
        order by created_at desc
        limit 1
    """
    res = base.executeQuery(query,(player_id, style_id))
    print(res)
    return res[0]

def getRatingByKey(key:str):
    player_id = base.getIdFromKey(key)
    query = """
	select 
	  player_id,
	  style,
	  rating,
	  sigma
	from(
	select 
	  * ,
	  rank() over (partition by style order by id desc) as recently
	from rating_logs 
	where player_id = ?
	) 
	where recently = 1;
    """
    res = base.executeQuery(query,(player_id,))
    print(res)
    return res

