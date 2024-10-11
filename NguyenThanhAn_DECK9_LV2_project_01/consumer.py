import os
from confluent_kafka import Consumer, KafkaException, KafkaError
import pymongo
from config import my_kafka_config
import json
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')

consumer = Consumer({
    **my_kafka_config,
    'auto.offset.reset': 'earliest',
    'group.id': 'An',
})

MIN_COMMIT_COUNT = 2

running = True

client = pymongo.MongoClient(MONGODB_URI)
db = client['kafka']
collection = db['product_view']


def write_message_to_mongodb(message):
    collection.insert_one(message)


def consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    print('End of partition event')
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                print(msg.value())
                doc = json.loads(msg.value().decode('utf-8'))
                write_message_to_mongodb(doc)
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()


consume_loop(consumer, ['topic-1'])
