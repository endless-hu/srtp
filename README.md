# SRTP

这是SRTP的仓库：使用Kafka+Alink构建分布式模型，对于光伏发电站的流式数据进行分析、处理，
运行一个K-means聚类算法，根据发电数据分类为晴天、阴天、雨天三类，以更好地分析光伏发电站的发电情况。

数据集来源是https://purl.stanford.edu/sm043zf7254，[点此](https://stacks.stanford.edu/file/druid:sm043zf7254/2017_pv_raw.csv)
可以下载到数据集。

在运行本项目代码前，需自行配置好alink的环境方可h正常运行。

## 项目结构

1. `kafka_setup.sh` 用于安装Kafka，并在本地模拟Kafka集群。
2. `src/producer.py` 用于将数据集（csv格式）中的数据流式写入Kafka集群；用于模拟实际光伏发电站的数据流。
3. `src/consumer.py` 用于从Kafka集群中读取数据流，并进行处理。
