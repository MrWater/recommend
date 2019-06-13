#!/bin/bash

workdir=/root/test/reconmend
cd $workdir

input=/test/test.csv
output="/test/score_output"
streaming=/soft/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.7.jar
	
hadoop fs -rm -r -skipTrash $output 2>/dev/null
hadoop jar $streaming -Dmapred.job.map=2 -Dmapred.job.reduces=2 -Dmapreduce.map.memory.mb=8192 -Dmapreduce.reduce.memory.mb=8192 -input $input -output $output -mapper "score_map.py" -file score_map.py -reducer "score_reduce.py" -file score_reduce.py

result_file="result1.txt"
hadoop fs -text $output/part* > $result_file

input=$output/part*
output="/test/relation_step1_output"

hadoop fs -rm -r -skipTrash $output 2>/dev/null
hadoop jar $streaming -Dmapred.job.map=2 -Dmapred.job.reduces=2 -Dmapreduce.map.memory.mb=8192 -Dmapreduce.reduce.memory.mb=8192 -input $input -output $output -mapper "relation_step1_map.py" -file relation_step1_map.py -reducer "relation_step1_reduce.py" -file relation_step1_reduce.py

result_file="result2.txt"
hadoop fs -text $output/part* > $result_file
