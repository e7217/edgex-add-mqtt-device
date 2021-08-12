import paho.mqtt.client as mqtt
from paho.mqtt import publish
import json, os
from dotenv import load_dotenv
load_dotenv()

host = os.getenv('HOST')
port = os.getenv('MQTT_BROKER_PORT')

dataset = {
    "name": "",
    "cmd": "",
    "randnum": ""
}

# todo: 지속적으로 랜덤 값 pub

# todo: 특정 명령어를 구독하고, 특정 값 반환

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # client.subscribe("$SYS/#")
    client.subscribe("#")

def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload))
    payload = msg.payload.decode("utf-8")
    # data = json.loads(json.dumps(payload))
    # print("payload : ", payload)
    if msg.topic in ["DataTopic", "CommandTopic", "ResponseTopic"]:
        data = json.loads(payload)
        print(f"[ {msg.topic} ] - {data}")
    if msg.topic == "CommandTopic":
        if data["method"] == "set":
            msg = data[data["cmd"]]
        else:
            if data["cmd"] == "ping":
                data["ping"] = "pong"
            elif data["cmd"] == "message":
                data["message"] = "test message~~~"
            elif data["cmd"] == "randnum":
                data["randnum"] = 12.123
        publish.single("ResponseTopic", json.dumps(data), hostname=host, port=port)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(host, port, 60)
client.loop_forever()