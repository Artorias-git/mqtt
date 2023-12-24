import time
import paho.mqtt.client as paho
from gg import *
import random

broker = "broker.emqx.io"


def on_message(client, userdata, message):
    time.sleep(1)
    data = str(message.payload.decode("utf-8"))
    print("received message =", data)
    print(send_command(data, resp_length=2))

client = paho.Client("client-2451111")
client.on_message = on_message
print("Connecting to broker", broker)
client.connect(broker)
client.loop_start()
print("Subcribing")
client.subscribe("house/RED_ALERT")
time.sleep(1800)

client.disconnect()
client.loop_stop()