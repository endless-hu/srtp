"""
Read the data from the Kafka topic 'pv' and run K-means clustering on it in a streaming fashion.
"""
import json
import time
import sys
import os
import numpy as np
from kafka import KafkaConsumer, KafkaAdminClient, NewTopic
import pyalink

# Kafka server address
KAFKA_SERVER = 'localhost:9092'
# Kafka topic name
KAFKA_TOPIC = 'pv'

# First check if the Kafka server is running
# If not, exit with error
if not sys.run('lsof -i:9092'):
    exit('Kafka server is not running, please start it first')

# Then check if the Kafka topic 'pv' exists, if not, exit with error
admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_SERVER)
if KAFKA_TOPIC not in admin_client.list_topics():
    exit('Kafka topic {} does not exist, please create it first'.format(KAFKA_TOPIC))

# -------------------
# Start ALink session
# -------------------
source = Kafka011SourceStreamOp()\
    .setBootstrapServers("localhost:9092")\
    .setTopic(KAFKA_TOPIC)\
    .setStartupMode("EARLIEST")\
    .setGroupId("alink_group")

kmeans_model = KMeansTrainStreamOp().setK(3)  # set the number of clusters to 3, representing sunny, cloudy and rainy

source.link(kmeans_model)

StreamOperator.execute()
