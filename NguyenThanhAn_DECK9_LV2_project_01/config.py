import os
from dotenv import load_dotenv

load_dotenv()

UNIGAP_KAFKA_BOOTSTRAP_SERVER=os.getenv('UNIGAP_KAFKA_BOOTSTRAP_SERVER')
UNIGAP_KAFKA_SECURITY=os.getenv('UNIGAP_KAFKA_SECURITY')
UNIGAP_KAFKA_MECHANISM=os.getenv('UNIGAP_KAFKA_MECHANISM')
UNIGAP_KAFKA_USERNAME=os.getenv('UNIGAP_KAFKA_USERNAME')
UNIGAP_KAFKA_PASSWORD=os.getenv('UNIGAP_KAFKA_PASSWORD')

MY_KAFKA_BOOTSTRAP_SERVER=os.getenv('MY_KAFKA_BOOTSTRAP_SERVER')
MY_KAFKA_SECURITY=os.getenv('MY_KAFKA_SECURITY')
MY_KAFKA_MECHANISM=os.getenv('MY_KAFKA_MECHANISM')
MY_KAFKA_USERNAME=os.getenv('MY_KAFKA_USERNAME')
MY_KAFKA_PASSWORD=os.getenv('MY_KAFKA_PASSWORD')

unigap_kafka_config = {
    'bootstrap.servers': UNIGAP_KAFKA_BOOTSTRAP_SERVER,
    'security.protocol': UNIGAP_KAFKA_SECURITY,
    'sasl.mechanism': UNIGAP_KAFKA_MECHANISM,
    'sasl.username': UNIGAP_KAFKA_USERNAME,
    'sasl.password': UNIGAP_KAFKA_PASSWORD,
    'auto.offset.reset': 'earliest',
    'group.id': 'An',
    'enable.auto.commit': 'true',
    'enable.auto.offset.store': 'true'
}

my_kafka_config = {
    'bootstrap.servers': MY_KAFKA_BOOTSTRAP_SERVER,
    'security.protocol': MY_KAFKA_SECURITY,
    'sasl.mechanism': MY_KAFKA_MECHANISM,
    'sasl.username': MY_KAFKA_USERNAME,
    'sasl.password': MY_KAFKA_PASSWORD,
}
