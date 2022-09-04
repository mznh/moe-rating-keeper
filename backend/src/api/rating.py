from fastapi import APIRouter
import models
import service

api= APIRouter()


@api.post("/rating")
def recordBattleResult(battle :models.RecordBattle):
    None

        
@api.get("/rating")
def getRating(key:str):
    print(key)
    return service.rating.getRatingByKey(key)

@api.get("/rating-by-token")
def getRating(key:str):
    print(key)
    return service.rating.getRatingByKey(key)
