#!/bin/bash

echo "🛑 Đang tiến hành tắt hệ thống Big Data Cluster..."

echo "1. Tắt Apache Spark..."
$SPARK_HOME/sbin/stop-workers.sh
$SPARK_HOME/sbin/stop-master.sh

echo "2. Tắt Hadoop YARN & HDFS..."
stop-yarn.sh
stop-dfs.sh

echo "✅ Hệ thống đã được tắt an toàn."