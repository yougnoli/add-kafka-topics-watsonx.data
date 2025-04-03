from confluent_kafka import Producer
import requests
import time
import json

producer_config = {
    'bootstrap.servers': 'broker-3-xxx.kafka.svc04.us-south.eventstreams.cloud.ibm.com:9093,'
                         'broker-1-xxx.kafka.svc04.us-south.eventstreams.cloud.ibm.com:9093,'
                         'broker-4-xxx.kafka.svc04.us-south.eventstreams.cloud.ibm.com:9093,'
                         'broker-5-xxx.kafka.svc04.us-south.eventstreams.cloud.ibm.com:9093,'
                         'broker-0-xxx.kafka.svc04.us-south.eventstreams.cloud.ibm.com:9093,'
                         'broker-2-xxx.kafka.svc04.us-south.eventstreams.cloud.ibm.com:9093',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'token',
    'sasl.password': 'YOUR_PASSWORD'
}

producer = Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print('Message delivery failed:', err)
    else:
        print('Message delivered:', msg.topic(), msg.partition())

url = 'http://api.open-notify.org/iss-now.json'
topic_name = 'iss-data'

while True:
    try:
        response = requests.get(url)
        data = response.json()

        producer.produce(topic_name, key=str(time.time()), value=json.dumps(data), callback=delivery_report)
        producer.poll(1)
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(10)

producer.flush()
