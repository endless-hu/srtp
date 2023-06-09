#!/bin/bash

# Kafka 3.4.0
wget https://dlcdn.apache.org/kafka/3.4.0/kafka_2.13-3.4.0.tgz
tar -xzf kafka_2.13-3.4.0.tgz
rm -rf kafka_2.13-3.4.0.tgz
cd kafka_2.13-3.4.0
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
# Format Log Dir
bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties

# start server
#nohup bin/kafka-server-start.sh config/kraft/server.properties
# Create a topic named "pv"
#bin/kafka-topics.sh --create --topic pv --bootstrap-server localhost:9092
# Show topic info
#bin/kafka-topics.sh --describe --topic pv --bootstrap-server localhost:9092
# Write into the topic
#bin/kafka-console-producer.sh --topic pv --bootstrap-server localhost:9092
# Read from the topic
#bin/kafka-console-consumer.sh --topic pv --from-beginning --bootstrap-server localhost:9092

