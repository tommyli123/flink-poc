from kafka import KafkaConsumer
consumer = KafkaConsumer('test', bootstrap_servers='localhost:9093')
for message in consumer:
    print (message)