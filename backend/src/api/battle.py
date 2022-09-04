from fastapi import APIRouter
import models
import service

api= APIRouter()


# name_a,token_a,name_b,token_b,winner_token を受け取り新しい対戦結果を記録し、レイティングを更新
@api.post("/battle")
def recordBattleResult(data :models.RecordBattle):
    print(data)
    # バトル登録
    return service.battle.add(data)
        
@api.get("/battle")
def getBattleResult(key:str):
    # バトル結果取得
    return service.battle.get(key)


@api.delete("/battle")
def deleteBattleResult(key:str):
    # バトル結果削除
    return ""
