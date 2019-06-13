import numpy as np
import pandas as pd

from itertools import permutations


temp = pd.read_csv("test.csv", header=None, names=["uid", "vid", "score"])

all_vid = set(temp["vid"].values)
all_vid_len = len(all_vid)
vid_matrix = pd.DataFrame(np.zeros((all_vid_len, all_vid_len), dtype=np.int), columns=all_vid, index=all_vid)

all_uid = set(temp["uid"].values)

score_matrix = pd.DataFrame(np.zeros((all_vid_len, len(all_uid)), dtype=np.int), columns=all_uid, index=all_vid)

def all_vid_group(uid):
	a = temp[temp["uid"]==uid]["vid"].values
	lst = list(permutations(a, 2))
	lst.extend([(i, i) for i in a])
	return lst

def fill_vid_matrix():
	global vid_matrix

	for uid in all_uid:
		vid_groups = all_vid_group(uid)

		for group in vid_groups:
			vid_matrix.loc[group] +=1

def fill_score():
	global score_matrix

	for index, row in temp.loc[1:].iterrows():
		score_matrix.loc[row["vid"],row["uid"]] = row["score"]

def last_score():
	return pd.DataFrame(np.array(vid_matrix.values).dot(np.array(score_matrix.values)), index=all_vid, columns=all_uid)


fill_score()
fill_vid_matrix()
print(last_score())




