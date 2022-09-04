from enum import Enum
import trueskill

import models
import sql

class RatingConstConfig(Enum):
    mu = 1500.
    sigma = mu / 5.
    beta = 200 
    # beta = sigma * 2. / 3.
    # 上手い人から見た勝率75%であるプレイヤーがどの程度下のmuにまで存在するか。
    # 運の要素が強い競技はここを大きな値にする必要がある。
    tau = sigma / 100. #sigmaの収束に影響 適当
    draw_probability = 0 # 引き分けになる確率


def generateRatingEnv():
    return trueskill.TrueSkill(
        mu=RatingConstConfig.mu.value,
        sigma=RatingConstConfig.sigma.value,
        beta=RatingConstConfig.beta.value,
        tau=RatingConstConfig.tau.value,
        draw_probability=RatingConstConfig.draw_probability.value, 
        backend=None)

def generateDefaultRating(initial_rate = None,):
    rate = RatingConstConfig.mu.value
    if initialRating != None:
        rate = initial_rate
    return self.env.create_rating(rate)

def addRating(player_id,style,new_rate,new_sigma):
    return sql.insertRating(player_id,style,new_rate,new_sigma)

def calculateRating(style_id,winner_id,loser_id):
    print("calculating ")
    ratingEnv = generateRatingEnv()
    tmp = sql.getRatingDataById(winner_id,style_id)
    print(tmp)
    winner_rating = ratingEnv.Rating(tmp["rating"],tmp["sigma"])
    tmp = sql.getRatingDataById(loser_id,style_id)
    loser_rating =  ratingEnv.Rating(tmp["rating"],tmp["sigma"])
    new_winner_rating, new_loser_rating = ratingEnv.rate_1vs1(winner_rating,loser_rating)

    sql.insertRating(winner_id,style_id, new_winner_rating.mu, new_winner_rating.sigma)
    sql.insertRating(loser_id ,style_id, new_loser_rating.mu,  new_loser_rating.sigma)


def getRatingByKey(key:str):
    return sql.getRatingByKey(key)

def getRatingByPlayerAndStyle(player_id:int,style_id:int):
    return sql.getRatingDataById(player_id,style_id)










