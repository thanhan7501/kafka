from confluent_kafka import Consumer, KafkaException, KafkaError
from config import unigap_kafka_config
from producer import push_message

consumer = Consumer(unigap_kafka_config)

MIN_COMMIT_COUNT = 2

running = True


def consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)
            print(msg)
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
                push_message('topic-1', msg.value())
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()

consume_loop(consumer, ['product_view'])