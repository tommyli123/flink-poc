# create topic
```
docker exec -it kafka_kafka_1 /opt/bitnami/kafka/bin/kafka-topics.sh \
    --create \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1 \
    --topic test
```

# view messages push to topic
```
docker exec -it kafka_kafka_1 /opt/bitnami/kafka/bin/kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --from-beginning \
  --topic test
```

# push messages to topic
```
docker exec -it kafka_kafka_1 /opt/bitnami/kafka/bin/kafka-console-producer.sh \
    --broker-list localhost:9092 \
    --topic test

```