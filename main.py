##!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import random


if __name__ == '__main__':
    # This is the Publisher
    wait_interval = 30
    BROKER_URL = "3.65.154.195"
    BROKER_PORT = 1883

    client = mqtt.Client()
    client.connect(BROKER_URL, BROKER_PORT)

    while True:
        temp_type = random.randint(0, 2)
        temp = 0.0

        if temp_type == 0:
            temp = 40 * random.random() + 20
        elif temp_type == 1:
            temp = 60 * random.random() + 20
        elif temp_type == 2:
            temp = 80 * random.random() + 20
        try:
            # client.publish("topic/test", "Hello world!")
            client.publish("temp", temp, qos=1)
            client.disconnect()
            time.sleep(wait_interval)
        except Exception as e:
            client.connect(BROKER_URL, BROKER_PORT)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
