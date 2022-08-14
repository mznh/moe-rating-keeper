#!/usr/bin/env python3

import trueskill
import csv 


mu = 25.
sigma = mu / 3.

# 上手い人から見た勝率75%であるプレイヤーがどの程度下のmuにまで存在するか。運の要素が強い競技はここを大きな値にする必要がある。
beta = sigma / 2.

tau = sigma / 100.
draw_probability = 0
backend = None


players = ["a","b","c","d","e","f"]


# trueskill env 生成
env = trueskill.TrueSkill(
    mu=mu, sigma=sigma, beta=beta, tau=tau,
    draw_probability=draw_probability, backend=backend)


# 全プレイヤーの rate object 生成
rate_objects = { p: env.create_rating() for p in players }

#with open('test_data/data.csv') as f:
with open('test_data/shuf.csv') as f:
    reader = csv.reader(f)
    for [a,b,w] in reader:
        print(a,b,w)
        side_a = rate_objects[a]
        side_b = rate_objects[b]
        winner = rate_objects[w]
        if a == w:
            rate_objects[w], rate_objects[b] = env.rate_1vs1(winner,side_b)
        else:
            rate_objects[w], rate_objects[a] = env.rate_1vs1(winner,side_a)



print(rate_objects)









