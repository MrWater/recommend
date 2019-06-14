#!/usr/bin/python3
#-*-coding:utf8-*-

import sys
import numpy as np
import pandas as pd

from itertools import permutations


relation = ""
cnt = 0
score = []

for line in sys.stdin:
    line = line.strip().split("\t")
    _type = line[2]

    if not relation:
        relation = line[0]
        
        idx = line[1].find(":")

        if _type == "0":
            cnt = 1
            score = [(line[1][:idx], line[1][idx+1:])]
        elif _type == "1":
            cnt = 0
            score = [(line[1][:idx], line[1][idx+1:])]
        else:
            cnt = 0
            score = []
        continue

    if relation == line[0]:
        idx = line[1].find(":")

        if _type == "0":
            cnt += 1
            score.append((line[1][:idx], line[1][idx+1:]))
        elif _type == "1":
            score.append((line[1][:idx], line[1][idx+1:]))
    else:
        for item in score:
            idx = relation.find(":")
            print("%s:%s\t%s\t%d\t%s" % (item[0], relation[:idx], relation[idx+1:], cnt, item[1]))
        relation = line[0]
        idx = line[1].find(":")

        if _type == "0":
            cnt = 1
            score = [(line[1][:idx], line[1][idx+1:])]
        elif _type == "1":
            cnt = 0
            score = [(line[1][:idx], line[1][idx+1:])]
        else:
            cnt = 0
            score = []

for item in score:
    idx = relation.find(":")
    print("%s:%s\t%s\t%d\t%s" % (item[0], relation[:idx], relation[idx+1:], cnt, item[1]))
