import sys
sys.path.insert(0, '/opt/spark/python')
sys.path.insert(0, '/opt/spark/python/lib/py4j-0.10.9.7-src.zip')

from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier, RandomForestClassifier, LogisticRegression, GBTClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql.functions import when, col

# Thay 'localhost' bằng địa chỉ IP của Master Node (Ví dụ: 192.168.1.x)
# 1. Khởi tạo SparkSession kết nối với Master
spark = SparkSession.builder \
    .appName("AmazonMetadataCluster") \
    .master("spark://localhost:7077") \
    .config("spark.executor.memory", "2g") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")
print("✅ SparkSession OK!")
print("Master:", spark.sparkContext.master)

# 2. Tải và tiền xử lý dữ liệu
df = spark.read.option("header", "true").option("inferSchema", "true") \
    .csv("/opt/spark/data/amazon_metadata.csv")

df = df.select("price", "salesRank", "brand", "categories").na.drop()

label_indexer = StringIndexer(inputCol="categories", outputCol="label")
brand_indexer = StringIndexer(inputCol="brand", outputCol="brandIndex")
assembler = VectorAssembler(
    inputCols=["price", "salesRank", "brandIndex"],
    outputCol="features"
)

pipeline = Pipeline(stages=[label_indexer, brand_indexer, assembler])
data = pipeline.fit(df).transform(df)
train, test = data.randomSplit([0.8, 0.2], seed=42)

print(f"Train: {train.count():,} dòng")
print(f"Test : {test.count():,} dòng")

eval = MulticlassClassificationEvaluator(labelCol="label", metricName="accuracy")

# 3. Huấn luyện các mô hình

# a. Decision Tree
dt = DecisionTreeClassifier(labelCol="label", featuresCol="features", maxBins=4200)
model_dt = dt.fit(train)
pred_dt = model_dt.transform(test)
acc_dt = eval.evaluate(pred_dt)
print("Decision Tree Accuracy:", round(acc_dt, 4))

# b. Random Forest
rf = RandomForestClassifier(labelCol="label", featuresCol="features", numTrees=20, maxBins=4200)
model_rf = rf.fit(train)
pred_rf = model_rf.transform(test)
acc_rf = eval.evaluate(pred_rf)
print("Random Forest Accuracy:", round(acc_rf, 4))

# c. Logistic Regression
lr = LogisticRegression(labelCol="label", featuresCol="features", maxIter=20)
model_lr = lr.fit(train)
pred_lr = model_lr.transform(test)
acc_lr = eval.evaluate(pred_lr)
print("Logistic Regression Accuracy:", round(acc_lr, 4))

# d. Gradient Boosted Tree 
train_bin = train.withColumn("label", when(col("label") == 0, 0.0).otherwise(1.0))
test_bin = test.withColumn("label", when(col("label") == 0, 0.0).otherwise(1.0))

gbt = GBTClassifier(labelCol="label", featuresCol="features", maxIter=10, maxBins=4200)
model_gbt = gbt.fit(train_bin)
pred_gbt = model_gbt.transform(test_bin)
acc_gbt = eval.evaluate(pred_gbt)
print("Gradient Boosted Tree Accuracy:", round(acc_gbt, 4))

# 4. So sánh và hiển thị kết quả
models = [
    ("Decision Tree", acc_dt),
    ("Random Forest", acc_rf),
    ("Logistic Regression", acc_lr),
    ("Gradient Boosted Tree", acc_gbt)
]

result = spark.createDataFrame(models, ["Model", "Accuracy"])
result.show()