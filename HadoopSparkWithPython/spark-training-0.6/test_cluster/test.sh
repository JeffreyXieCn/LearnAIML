#!/usr/bin/env bash

set -e

ok() { echo -e "[  \e[32mOK\e[39m  ]"; }
die() { echo -e "[  \e[31mFAIL\e[39m  ]"; cat lastlog ; \rm lastlog ; exit 1; }
mytest() { command=$1 ; echo -n ${command}"... "  ; ${command} &>lastlog && ok || die ; }

FS_URL=hdfs://10.0.2.8:9000

echo test > test.txt

declare -a commands=(\
"hdfs dfs --fs ${FS_URL} -ls /user" \
"hdfs dfs --fs ${FS_URL} -mkdir -p /user/tristan" \
"hdfs dfs --fs ${FS_URL} -ls /user/tristan" \
"hdfs dfs --fs ${FS_URL} -rm -f /user/tristan/test.txt"
"hdfs dfs --fs ${FS_URL} -put test.txt /user/tristan/test.txt" \
"hdfs dfs --fs ${FS_URL} -ls /user/tristan/test.txt" \
"hdfs dfs --fs ${FS_URL} -get /user/tristan/test.txt test_download.txt" \
"hdfs dfs --fs ${FS_URL} -cat /user/tristan/test.txt" \
"hdfs dfs --fs ${FS_URL} -rm -f /user/tristan/test.txt"
)

for command in "${commands[@]}"; do
  mytest "${command}"
done
# Cleanup
\rm -f test.txt test_download.txt


mytest "spark-submit --master yarn --deploy-mode cluster --conf spark.yarn.stagingDir=hdfs://10.0.2.8:9000/user test_cluster/spark_test.py"

