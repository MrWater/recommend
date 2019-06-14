#!/bin/bash

workdir=/root/test/reconmend
cd $workdir


#===========用户评分============
input=/test/test.csv
output="/test/score_output"
streaming=/soft/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.7.jar
	
hadoop fs -rm -r -skipTrash $output 2>/dev/null
hadoop jar $streaming -Dmapred.job.map=2 -Dmapred.job.reduces=2 -Dmapreduce.map.memory.mb=8192 -Dmapreduce.reduce.memory.mb=8192 -input $input -output $output -mapper "score_map.py" -file score_map.py -reducer "score_reduce.py" -file score_reduce.py

result_file="result_score.txt"
hadoop fs -text $output/part* > $result_file


#===========物品关联============
input=$output/part*
output="/test/relation_output"

hadoop fs -rm -r -skipTrash $output 2>/dev/null
hadoop jar $streaming -Dmapred.job.map=2 -Dmapred.job.reduces=2 -Dmapreduce.map.memory.mb=8192 -Dmapreduce.reduce.memory.mb=8192 -input $input -output $output -mapper "relation_map.py" -file relation_map.py -reducer "relation_reduce.py" -file relation_reduce.py

result_file="result_relation.txt"
hadoop fs -text $output/part* > $result_file

#===========兴趣得分============
input=$output/part*
output="/test/interest_output"

hadoop fs -rm -r -skipTrash $output 2>/dev/null
hadoop jar $streaming -Dmapred.job.map=2 -Dmapred.job.reduces=2 -Dmapreduce.map.memory.mb=8192 -Dmapreduce.reduce.memory.mb=8192 -input $input -output $output -mapper "interest_map.py" -file interest_map.py -reducer "interest_reduce.py" -file interest_reduce.py

result_file="result_interest.txt"
hadoop fs -text $output/part* > $result_file
