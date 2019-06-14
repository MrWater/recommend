#!/usr/bin/python3
#-*-coding:utf8-*-

import sys


all_vid = set()


with open(sys.argv[1]) as f:
    for line in f:
        line = line.split(",")
        all_vid.add(line[1].strip())

fs_input = open("input.txt", "w+");

uid = ""
with open(sys.argv[1]) as f:
    if not uid:
        line = f.readline()
        line = line.split(",")
        uid = line[1].strip()

fs_input.close()
