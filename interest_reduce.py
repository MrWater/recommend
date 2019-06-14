#!/usr/bin/python3
#-*-coding:utf8-*-

import sys
import numpy as np
import pandas as pd

from itertools import permutations


uid_vid = ""
interest = 0

for line in sys.stdin:
    line = line.split("\t")

    if not uid_vid:
        uid_vid = line[0].strip()
        interest = float(line[2].strip()) * float(line[3].strip())
        continue

    if uid_vid == line[0].strip():
        interest += float(line[2].strip()) * float(line[3].strip())
    else:
        print("%s\t%f" % (uid_vid, interest))
        uid_vid = line[0].strip()
        interest = float(line[2].strip()) * float(line[3].strip())

print("%s\t%f" % (uid_vid, interest))
