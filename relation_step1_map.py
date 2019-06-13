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
        score = item[idx+1:]

        for item2 in line:
            print("%s:%s\t%s:%s" % (vid, item2[:item2.find(":")], uid, score))
