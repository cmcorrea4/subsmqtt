import streamlit as st
import time

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("your_topic")

def on_message(client, userdata, msg):
    st.write(msg.topic+" "+str(msg.payload))

def main():
    st.title("MQTT subscriber")

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("mqtt.eclipse.org", 1883, 60)

    while True:
        client.loop_start()
        time.sleep(1)

    st.button("Close")

if __name__ == "__main__":
    main()
