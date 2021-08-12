import json
import os
import random
import time

import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from paho.mqtt import publish

load_dotenv()

host = os.getenv("HOST")
port = os.getenv("MQTT_BROKER_PORT")

dataset = {"name": "MQTT-Test-Device", "cmd": "randnum", "randnum": random.random()}

devices = ["MQTT-Test-Device", "demo-device"]

# todo: 지속적으로 랜덤 값 pub

# todo: 특정 명령어를 구독하고, 특정 값 반환


def make_msg():
    dataset["randnum"] = round(random.uniform(25, 29), 1)
    return dataset


while True:
    time.sleep(2)
    for device in devices:
        dataset["name"] = device
        dataset["randnum"] = round(random.uniform(25, 29), 1)
        publish.single("DataTopic", json.dumps(dataset), hostname=host, port=port)
    # publish.single("DataTopic", json.dumps(make_msg()),hostname=host, port=port)
