#!/usr/bin/python3
#-*-coding:utf8-*-

import sys
import numpy as np
import pandas as pd

from itertools import permutations


relation = ""
cnt = 0
score = ""

for line in sys.stdin:
    line = line.strip().split("\t")

    if not relation:
        relation = line[0]
        cnt = 1
        print(line)
        score = line[1]
        continue

    if relation == line[0]:
        cnt += 1
        score = "%s,%s" % (score, line[1])
    else:
        print("%s\t%d\t%s" % (relation, cnt, score))
        cnt = 1
        relation = line.strip()
        score = line[1]

print("%s\t%d\t%s" % (relation, cnt, score))
