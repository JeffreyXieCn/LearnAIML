#!/usr/bin/env bash

set -e

die() { echo $* ; exit 1; }

# Check if JAVA_HOME is defined
test -n "${JAVA_HOME}" || die Please define JAVA_HOME
echo JAVA_HOME=${JAVA_HOME}

# Download release if not there
HADOOP_VERSION=3.3.0
URL=http://apache.forsale.plus/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
HADOOP_RELEASE=hadoop-${HADOOP_VERSION}.tar.gz
test -f ${HADOOP_RELEASE} || wget ${URL}

# Unpack release, set variables, configure JAVA_HOME in Hadoop config
\rm -Rf hadoop-${HADOOP_VERSION} && tar xf ${HADOOP_RELEASE} 
export HADOOP=$PWD/hadoop-${HADOOP_VERSION}
export PATH=$PATH:${HADOOP}/bin:${HADOOP}/sbin
echo JAVA_HOME=${JAVA_HOME} >> ${HADOOP}/etc/hadoop/hadoop-env.sh

# Test installation
hadoop version &>hadoop.log || (cat hadoop.log && rm hadoop.log && die "Installation failed!")

# Print instructions
echo Installation complete!
echo export HADOOP=$PWD/hadoop-${HADOOP_VERSION} >> ~/.bashrc
echo 'export PATH=$PATH:${HADOOP}/bin:${HADOOP}/sbin' >> ~/.bashrc
