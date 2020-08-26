#!/usr/bin/env bash

set -e

ok() { echo -e "[  \e[32mOK\e[39m  ]" $*; }
die() { echo -e "[  \e[31mFAIL\e[39m  ]" $* ; exit 1; }
mytest() { command=$* ; ${command} && ok ${command} || die ${command}; }


mytest "cp -f test_cluster/yarn-site.xml $HOME/hadoop-3.3.0/etc/hadoop"
echo export HADOOP_CONF_DIR=$HOME/hadoop-3.3.0/etc/hadoop >> $HOME/.bashrc

echo Installation complete!


