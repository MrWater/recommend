#!/usr/bin/python3
#-*-coding:utf8-*-

import sys
import numpy as np
import pandas as pd


uid = ""
score = ""
need_print = False

for line in sys.stdin:
    temp = line.strip()
    line = line.strip().split("\t")
    if (len(line) != 2):
        continue
    
    try:
        if not uid:
            uid = line[0].strip()
            score = line[1]
            need_print = True
            continue
        
        if uid == line[0].strip():
            score = "%s,%s" % (score, line[1].strip())
        else:
            need_print = False
            print("%s\t%s" % (uid, score))
            uid = line[0].strip()
            score = line[1].strip()
            need_print = True
    except:
        continue

if need_print:
    print("%s\t%s" % (uid, score))
