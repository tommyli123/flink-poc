from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9093')
print(producer)
r = producer.send('test', key=b'message-one', value=b'Hello, World!')
print(r)

producer.send('test', key=b'message-two', value=b'This is Kafka-Python')
producer.flush()
