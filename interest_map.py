#!/usr/bin/python3
#-*-coding:utf8-*-

import sys
import numpy as np
import pandas as pd

from itertools import permutations


for line in sys.stdin:
    if "NAN" not in line:
        print(line.strip())
