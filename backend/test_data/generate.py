#!/usr/bin/env python3

import random



players = ["a","b","c","d","e","f"]



for sideA in players:
    for sideB in [ p for p in players if p != sideA ] :
        winner = random.choice([sideA,sideB])
        s = ",".join([sideA,sideB,winner])
        print(s)


