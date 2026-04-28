# 🏗️ Kiến trúc Big Data Cluster (Architecture Design)

Tài liệu này mô tả chi tiết mô hình triển khai phân tán (Distributed Topology) được sử dụng để xử lý dữ liệu hàng không và mô hình học máy trên Amazon Metadata.

## 1. Topo Mạng (Network Topology)
Hệ thống được triển khai trên 3 node (máy ảo) độc lập chạy hệ điều hành Ubuntu:
* **Master Node:** `hadoop-master` (Đóng vai trò điều phối)
* **Worker Node 1:** `hadoop-slave1` (Đóng vai trò xử lý tính toán)
* **Worker Node 2:** `hadoop-slave2` (Đóng vai trò xử lý tính toán)

## 2. Phân bổ Dịch vụ (Service Allocation)
Việc phân bổ tài nguyên tuân thủ nguyên tắc tách biệt giữa điều phối (Master) và thực thi (Worker) của Hadoop/Spark:

| Thành phần (Component) | Master Node (`hadoop-master`) | Worker Nodes (`hadoop-slave1, 2`) |
| :--- | :--- | :--- |
| **Hadoop HDFS** | NameNode, SecondaryNameNode | DataNode |
| **Hadoop YARN** | ResourceManager | NodeManager |
| **Apache Spark** | Master Daemon | Worker Daemon |

## 3. Cổng Giám sát (Web UI Ports)
Sử dụng các cổng sau để giám sát sức khỏe cụm (Health Check) và tiến độ chạy Job:
* **HDFS NameNode UI:** `http://<master-ip>:9870` (Quản lý block lưu trữ)
* **YARN ResourceManager UI:** `http://<master-ip>:8088` (Quản lý tài nguyên RAM/CPU)
* **Spark Master UI:** `http://<master-ip>:8080` (Giám sát Spark Jobs)

## 4. Giao tiếp nội bộ (Internal Communication)
Các Node giao tiếp và truyền tải dữ liệu với nhau hoàn toàn thông qua giao thức **SSH (Passwordless Authentication)** để đảm bảo quá trình khởi động cụm được tự động hóa hoàn toàn.