from confluent_kafka import Producer
import socket
from config import my_kafka_config

conf = {**my_kafka_config, 'client.id': socket.gethostname()}

producer = Producer(conf)

def acked(err, msg):
    if err is not None:
        print('Failed to deliver message: %s: %s' % (str(msg), str(err)))
    else:
        print('Message produced: %s' % (str(msg)))


def push_message(topic, msg):
    producer.produce(topic, value=msg, callback=acked)

    # Wait up to 1 second for events. Callbacks will be invoked during
    # this method call if the message is acknowledged.
    producer.poll(1)
