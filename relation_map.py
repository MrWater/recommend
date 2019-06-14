#!/usr/bin/python3
#-*-coding:utf8-*-

import sys
import numpy as np
import pandas as pd

from itertools import permutations


for line in sys.stdin:
    line = line.split('\t')
    if (len(line) != 2):
        continue

    uid = line[0].strip()
    line = line[1].strip().split(",")

    for item in line:
        item = item.strip()
        idx = item.find(":")
        vid = item[:idx]
        temp = item[idx+1:]

        for item2 in line:
            idx = item2.find(":")
            score = item2[idx+1:]
           
            # 0:both 1:cal no add 2:both no
            _type = 0
            if temp != "NAN" and score != "NAN":
                _type = 0
            elif temp == "NAN":
                _type = 1
            else:
                _type = 2
            print("%s:%s\t%s:%s\t%d" % (vid, item2[:item2.find(":")], uid, score, _type))
