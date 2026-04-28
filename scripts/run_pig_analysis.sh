#!/bin/bash

echo "🐷 Đang thực thi các tác vụ MapReduce bằng Apache Pig..."

# Chạy phân tích Top 5 hãng bay
echo "-> Chạy script: top5_arrdelay.pig"
pig -x mapreduce ../pig/top5_arrdelay.pig

# Chạy phân tích độ trễ theo tháng
echo "-> Chạy script: monthly_delay_rate.pig"
pig -x mapreduce ../pig/monthly_delay_rate.pig

echo "✅ Hoàn tất xử lý dữ liệu. Kết quả đã được lưu trữ trên HDFS."