import json
import random
import time
import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, broker, port, topic):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker")
        else:
            print(f"Failed to connect, return code {rc}")

    def connect(self):
        self.client.connect(self.broker, self.port, 60)

    def publish(self, payload):
        self.client.publish(self.topic, payload)

    def disconnect(self):
        self.client.disconnect()

def generate_data():
    return {
        "temperature": random.uniform(5.0, 40.0),
        "humidity": random.uniform(30.0, 60.0)
    }

def main():
    mqtt_broker = "mqtt.beia-telemetrie.ro"
    mqtt_port = 1883
    mqtt_topic = "training/device/Niculcea-Silviu_Andrei"

    mqtt_client = MQTTClient(mqtt_broker, mqtt_port, mqtt_topic)
    mqtt_client.connect()

    try:
        while True:
            data = generate_data()
            payload = json.dumps(data)
            mqtt_client.publish(payload)
            print(f"Published data: {payload}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        mqtt_client.disconnect()

if __name__ == "__main__":
    main()
