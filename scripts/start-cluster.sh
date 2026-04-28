#!/bin/bash

echo "🚀 Bắt đầu khởi động hệ thống Big Data Cluster..."


echo "1. Khởi động Hadoop HDFS & YARN..."
start-dfs.sh
start-yarn.sh

echo "2. Khởi động Apache Spark (Master & Workers)..."
$SPARK_HOME/sbin/start-master.sh
$SPARK_HOME/sbin/start-workers.sh

echo "✅ Hệ thống đã chạy thành công! Vui lòng kiểm tra các cổng Web UI"