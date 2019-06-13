#!/usr/bin/python3
#-*-coding:utf8-*-

import sys
import numpy as np
import pandas as pd

from itertools import permutations


for line in sys.stdin:
    #uid,vid,score
    line = line.split(',')
    if (len(line) != 3):
        continue

    if not line[0].strip or not line[1].strip() or not line[2].strip():
        continue

    print("%s\t%s:%s" % (line[0].strip(), line[1].strip(), line[2].strip()))
