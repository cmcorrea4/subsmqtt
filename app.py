import paho.mqtt.client as mqtt
import time
import streamlit as st

# Callback function on connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        st.write("Connected to broker")
        global Connected
        Connected = True
    else:
        st.write("Connection failed")

# Callback function on receive message
def on_message(client, userdata, message):
    st.write(f'Message received:  {message.payload}')

Connected = False

broker_address = 'broker.hivemq.com'
port = 1883

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port=port)

client.loop_start()  # start MQTT client

while Connected != True:  # Wait for connection
    time.sleep(0.2)

client.subscribe('Sensores')  # Subscribe to topic
client.publish("Sensores", "Hello from Streamlit")  # Publish message

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    st.write("Disconnected")
    client.disconnect()
    client.loop_stop()
