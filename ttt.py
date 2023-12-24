import time
import paho.mqtt.client as paho
import random

# broker = "broker.emqx.io"
broker = "broker.hivemq.com"


client = paho.Client("client-isu-001")

print(f"Contnrcting to broker {broker}")
client.connect(broker)
client.loop_start()
print("Publishing")


for _ in range(10):
    state = " Never gonna give you up " \
            "Never gonna let you down " \
            "Never gonna run around and desert you " \
            "Never gonna make you cry " \
            "Never gonna say goodbye " \
            "Never gonna tell a lie " \
            "and hurt you." if random.randint(0,1) else "nununnunn"
    print(f"state is {state}")
    client.publish("house/bulb1",state)
    time.sleep(random.randint(4, 10))

client.disconnect()
client.loop_stop()