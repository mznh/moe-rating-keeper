import models
import sql
import service.rating as rating


def add(data: models.Battle):
    battle = data.dict()
    battle["style"] = 1
    #sql.player.insert(player)
    validate_res_a = sql.validateNameAndToken( battle["side_a_name"], battle["side_a_token"] )
    validate_res_b = sql.validateNameAndToken( battle["side_b_name"], battle["side_b_token"] )
    if not validate_res_a or not validate_res_b:
        return "error"
    
    side_a_id = sql.getIdFromNameAndToken(battle["side_a_name"],battle["side_a_token"])
    side_b_id = sql.getIdFromNameAndToken(battle["side_b_name"],battle["side_b_token"])

    if battle["winner_token"] == battle["side_a_token"]:
        # A が勝った
        sql.battle.insert(side_a_id,side_b_id,side_a_id)
        rating.calculateRating(battle["style"],side_a_id,side_b_id)
    elif battle["winner_token"] == battle["side_b_token"]:
        # B が勝った
        sql.battle.insert(side_a_id,side_b_id,side_b_id)
        rating.calculateRating(battle["style"],side_b_id,side_a_id)
    return "ok"

def get(key:str):
    res = sql.battle.selectByKey(key)
    print(res)
    return {
        "battles": res
    }
