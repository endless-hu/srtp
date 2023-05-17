"""
Read the .csv file and send the data to the Kafka topic 'pv'.
Before running this script, make sure the Kafka server is running, and the
Kafka topic 'pv' is created, otherwise the script will create the topic
The .csv format is:
line 1: meaningless header
line 2: YYYY-MM-DDTHH:MM:SS, value
...

Currently, the kafka server is running on localhost:9092
"""
import sys
import os
import pyalink
from kafka import KafkaProducer, KafkaAdminClient, NewTopic

# Kafka server address
KAFKA_SERVER = 'localhost:9092'
# Kafka topic name
KAFKA_TOPIC = 'pv'
# Path to the .csv file
DATA_PATH = 'data/pv.csv'

# First check if the Kafka server is running
# If not, exit with error
if not sys.run('lsof -i:9092'):
    exit('Kafka server is not running, please start it first')

# Then check if the Kafka topic 'pv' exists, if not, create it
admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_SERVER)
if KAFKA_TOPIC not in admin_client.list_topics():
    topic_list = []
    topic_list.append(NewTopic(name=KAFKA_TOPIC, num_partitions=1, replication_factor=1))
    admin_client.create_topics(new_topics=topic_list, validate_only=False)

# Finally check if the .csv file exists, if not, download it from
# https://stacks.stanford.edu/file/druid:sm043zf7254/2017_pv_raw.csv
# and save it to the path DATA_PATH
if not os.path.exists(DATA_PATH):
    print('Downloading the .csv file from https://stacks.stanford.edu/file/druid:sm043zf7254/2017_pv_raw.csv')
    sys.run('wget https://stacks.stanford.edu/file/druid:sm043zf7254/2017_pv_raw.csv -O data/pv.csv')

sink = Kafka011SinkStreamOp()\
    .setBootstrapServers("localhost:9092")\
    .setDataFormat("json")\
    .setTopic(KAFKA_TOPIC)
# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

SCHEMA_STR = "time string, value double"
data = CsvSourceStreamOp().setFilePath(DATA_PATH).setSchemaStr(SCHEMA_STR)

sink = Kafka011SinkStreamOp()\
    .setBootstrapServers("localhost:9092")\
    .setDataFormat("json")\
    .setTopic(KAFKA_TOPIC)

data.link(sink)

StreamOperator.execute()
