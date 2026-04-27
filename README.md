# 🚀 Hadoop - Spark - Pig Cluster Setup & Data Processing

## 📌 Giới thiệu

Triển khai và vận hành hệ thống **Big Data phân tán** sử dụng:

* Apache Hadoop (HDFS, YARN)
* Apache Spark
* Apache Pig

Hệ thống được xây dựng trên môi trường **Ubuntu (Linux)** với mô hình **Cluster (Master - Slave)** nhằm:

* Lưu trữ dữ liệu lớn (HDFS)
* Xử lý dữ liệu phân tán (Spark, Pig)
* Phân tích và trực quan hóa dữ liệu

---

## 🏗️ Kiến trúc hệ thống

* **Master Node**

  * NameNode (HDFS)
  * ResourceManager (YARN)
  * Spark Master

* **Slave Nodes**

  * DataNode
  * NodeManager
  * Spark Worker

---

## 🛠️ Công nghệ sử dụng

* Linux (Ubuntu)
* SSH (Passwordless)
* Apache Hadoop (HDFS, YARN)
* Apache Spark
* Apache Pig (Pig Latin)
* Python (Visualization)

---

## 📂 Cấu trúc thư mục

```bash
hadoop-spark-pig-setup/
└── screenshots/
    ├── 01-prerequisites/
    ├── 02-hadoop-installation/
    ├── 03-cluster-network-setup/
    ├── 04-hadoop-configuration/
    ├── 05-hdfs-setup/
    ├── 06-yarn-setup/
    ├── 07-spark/
    └── 08-pig/
```

---

## ⚙️ 1. Chuẩn bị môi trường (Prerequisites)

* Cài đặt SSH, pdsh
* Tạo SSH key và cấu hình passwordless
* Kiểm tra Java & Python

📸 Ví dụ:

* SSH setup
* Authorized keys
* Java verification

---

## 🧱 2. Cài đặt Hadoop

* Giải nén Hadoop
* Cấu hình `JAVA_HOME`
* Thiết lập thư mục làm việc

---

## 🌐 3. Thiết lập Cluster & Network

* Cấu hình `/etc/hosts`
* Đặt hostname cho các node
* Phân phối SSH key giữa các node

---

## ⚙️ 4. Cấu hình Hadoop

* `core-site.xml`
* `hdfs-site.xml`
* `workers`
* Đồng bộ cấu hình từ master → slaves

---

## 💾 5. HDFS (Storage Layer)

* Format HDFS
* Khởi động DFS
* Truy cập Web UI (port 9870)

📸 Demo:

* HDFS Web UI

---

## ⚡ 6. YARN (Resource Management)

* Cấu hình `yarn-site.xml`
* Khởi động YARN
* Kiểm tra Resource Manager (port 8088)

📸 Demo:

* YARN UI

---

## 🔥 7. Apache Spark (Distributed Processing)

### ✔ Thiết lập

* Kiểm tra cài đặt Spark
* Cấu hình `bashrc`
* Khởi động Spark Master & Workers

### ✔ Kiểm tra

* Spark Master UI (port 8080)
* Worker UI (port 8081)

### ✔ Thực thi job

* Tạo dữ liệu input
* Viết chương trình WordCount (Python)
* Chạy bằng `spark-submit`
* Kiểm tra trạng thái job

📸 Demo:

* Spark UI
* Job execution

---

## 🐘 8. Apache Pig (Data Processing & ETL)

### ✔ Chế độ chạy

* Local Mode
* MapReduce Mode

### ✔ Xử lý dữ liệu

* Viết script Pig Latin:

  * Lọc dữ liệu
  * Nhóm dữ liệu
  * Phân tích delay

### ✔ Bài toán thực tế

* Tháng có delay thấp nhất / cao nhất
* Top hãng bay ít delay nhất
* Sân bay có delay cao

### ✔ Visualization

* Xuất dữ liệu từ HDFS
* Dùng Python vẽ biểu đồ:

  * Top carriers
  * Monthly delay rate

📸 Demo:

* Pig script
* Output HDFS
* Biểu đồ phân tích

---

## 📊 Kết quả đạt được

* Triển khai thành công hệ thống Big Data phân tán
* Xử lý dữ liệu lớn bằng Spark & Pig
* Xây dựng pipeline:

  > Data → Processing → Analysis → Visualization
* Hiểu rõ:

  * HDFS (storage)
  * YARN (resource)
  * Spark / Pig (processing)

---

## 🎯 Kỹ năng đạt được

* Linux system administration
* Distributed system setup
* Data processing (Spark, Pig)
* ETL pipeline
* Data analysis & visualization
* Debug & vận hành cluster

---

## 📌 Ghi chú

* Dự án mang tính **lab + thực hành triển khai thực tế**
* Tập trung vào:

  * Setup hệ thống
  * Xử lý dữ liệu
  * Hiểu pipeline Big Data

