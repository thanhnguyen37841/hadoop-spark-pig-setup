# 🚀 Hadoop - Spark - Pig: End-to-End Big Data Pipeline

## 📌 Tổng quan
Tập trung vào việc thiết kế và triển khai một **cụm tính toán phân tán (Distributed Cluster)** hoàn chỉnh. Mục tiêu là giải quyết bài toán xử lý dữ liệu hàng không (Airline Delay) quy mô lớn, từ khâu lưu trữ thô đến khi trích xuất thông tin có giá trị (Insights).

## 🔄 Data Pipeline
Airline Data → HDFS → Pig ETL → Aggregated Output → Visualization → Insights

Amazon Metadata → Spark MLlib → Model Evaluation → Insights

## 🏗️ Kiến trúc hệ thống & Stack kỹ thuật
* **Cluster Topology:** 01 Master Node & 02 Slave Nodes (Virtualization environment).
* **Storage Layer:** HDFS với cấu hình Replication Factor phù hợp để đảm bảo an toàn dữ liệu.
* **Resource Management:** YARN điều phối tài nguyên động giữa Spark và Pig.
* **Processing Engine:** 
  * **PySpark:** 
    * Xử lý tính toán phân tán (WordCount, Data Processing)
    * Xây dựng mô hình Machine Learning với Spark MLlib (Amazon Metadata Classification)
  * **Pig Latin:** Xây dựng các luồng ETL (Extract - Transform - Load)

<details>
<summary><b>🛠️ Nhấn vào đây để xem chi tiết các bước triển khai</b></summary>

### ⚙️ Quy trình triển khai chi tiết (8 Bước)

**1. Chuẩn bị môi trường (Prerequisites)**
* Cài đặt các gói hỗ trợ kết nối: SSH, pdsh.
* Thiết lập an ninh: Tạo SSH key và cấu hình đăng nhập không mật khẩu (passwordless) giữa các node.
* Kiểm tra các nền tảng cơ bản: Đảm bảo Java và Python đã được cài đặt và hoạt động đúng.

**2. Cài đặt Hadoop**
* Giải nén gói cài đặt Apache Hadoop.
* Khai báo môi trường: Cấu hình biến `JAVA_HOME` để Hadoop nhận diện môi trường thực thi.
* Thiết lập cấu trúc: Định nghĩa các thư mục làm việc hệ thống.

**3. Thiết lập Cluster & Network**
* Phân giải tên miền cục bộ: Cấu hình file `/etc/hosts` để các máy nhận diện nhau qua IP/Hostname.
* Đặt định danh: Thiết lập hostname riêng biệt cho Master và các Slave node.
* Kết nối mạng nội bộ: Phân phối SSH public key từ Master đến tất cả các Slave.

**4. Cấu hình các thành phần Hadoop**
* Tùy chỉnh các tệp cấu hình lõi: Chỉnh sửa `core-site.xml` (định nghĩa hệ thống file) và `hdfs-site.xml` (cấu hình lưu trữ).
* Quản lý nhân sự: Cập nhật file `workers` để liệt kê danh sách các node thực thi.
* Đồng bộ hóa: Sao chép toàn bộ cấu hình từ Master sang các Slave để đảm bảo tính nhất quán.

**5. HDFS (Storage Layer)**
* Khởi tạo: Thực hiện format NameNode lần đầu tiên để thiết lập cấu trúc HDFS.
* Vận hành: Khởi động dịch vụ Distributed File System (DFS).
* Giám sát: Kiểm tra trạng thái lưu trữ thông qua Web UI tại cổng 9870.

**6. YARN (Resource Management)**
* Cấu hình tài nguyên: Thiết lập các thông số trong `yarn-site.xml`.
* Khởi động bộ điều phối: Chạy dịch vụ YARN để quản lý tài nguyên tính toán của cụm.
* Quản lý tập trung: Theo dõi các ứng dụng và tài nguyên qua cổng 8088.

**7. Apache Spark (Distributed Processing)**
* Thiết lập môi trường chạy: Cấu hình file `.bashrc` và các tham số Spark.
* Kích hoạt cụm: Khởi động Spark Master và các Spark Worker trên từng node.
* Thực thi: Sử dụng lệnh `spark-submit` để đẩy các job tính toán (như WordCount) lên cụm.

**8. Apache Pig (Data Processing & ETL)**
* Lựa chọn chế độ: Chạy ở Local Mode (thử nghiệm) hoặc MapReduce Mode (trên Cluster).
* Xử lý dữ liệu: Viết script Pig Latin để thực hiện ETL (Lọc, nhóm, tính toán thống kê delay).
* Trực quan hóa: Xuất kết quả từ HDFS và sử dụng Python để vẽ biểu đồ phân tích (hãng bay, thời gian delay).

</details>

## 🤖 Machine Learning with Spark MLlib

Triển khai Machine Learning với Spark MLlib trên dataset Amazon Metadata.

- Feature: price, salesRank, brand
- Pipeline: StringIndexer → VectorAssembler → Train/Test Split
- Models: Decision Tree, Random Forest, Logistic Regression, Gradient Boosted Tree
- Evaluation: Accuracy comparison giữa các mô hình
  
## ⚡ Điểm nhấn kỹ thuật (Key Highlights)
* **Cấu hình Cluster thực tế:** Không chạy Standalone, dự án mô phỏng môi trường thực tế với kết nối SSH Passwordless và quản lý Node qua cấu hình `workers`.
* **ETL Pipeline chuyên sâu:**  Lọc và làm sạch dữ liệu nhiễu từ bộ dữ liệu hàng không.
  * Phân tích xu hướng delay theo hãng bay (Carriers) và thời gian (Monthly).
* **Visualization:** Tích hợp Python để chuyển đổi kết quả từ HDFS thành biểu đồ trực quan, giúp đưa ra quyết định kinh doanh.
* **Machine Learning Pipeline:** Huấn luyện và so sánh nhiều mô hình bằng Spark MLlib trên dữ liệu Amazon.

## 🛠️ Hướng dẫn triển khai nhanh (Quick Start)
* **Start Services:**
```bash
start-dfs.sh && start-yarn.sh
```

* **Submit Spark Job:**
```bash
spark-submit --master yarn ./spark/wordcount.py
```

* **Run Pig Script:**
```bash
pig -x mapreduce ./pig/top5_carriers.pig
pig -x mapreduce ./pig/monthly_delay_rate.pig
```

* **Run Spark ML Job:**
```bash
spark-submit --master spark://<master-ip>:7077 ./spark/amazon_ml_analysis.py
```


## 📊 Kết quả đạt được
* Vận hành ổn định cụm Multi-node với đầy đủ các Web UI giám sát.
* Xử lý thành công tập dữ liệu hàng không, tìm ra các "điểm nghẽn" gây delay chuyến bay.
* Xây dựng nền tảng kiến thức về Linux System Administration và Big Data Troubleshooting.
* Xây dựng và đánh giá mô hình Machine Learning phân tán với Spark MLlib trên dataset Amazon.
  
## 👤 Tác giả

**Nguyễn Chí Thành** - Công nghệ thông tin (Khóa 14) - Trường Đại học Công Thương TPHCM (HUIT)
