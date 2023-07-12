import json
import streamlit as st
from paho.mqtt import client as mqtt



# Create a line chart
my_chart = st.line_chart([0.])

# Initialize MQTT client
mqtt_client = mqtt.Client()

# Connect to MQTT broker
mqtt_client.connect("157.230.214.127", 1883)

# Define a function to handle incoming MQTT messages
def on_message(client, userdata, msg):
    st.write(f'Message received:  {msg.payload}')

        
# Set the function to handle incoming messages
mqtt_client.on_message = on_message


# Create a "Start subscription" button
if st.button("Start subscription"):
    mqtt_client.subscribe("Sensores")
    mqtt_client.loop_forever()

# Create a "Stop subscription" button
if st.button("Stop subscription"):
    mqtt_client.disconnect()
	# Tried with loop_stop() as well, same issue
	#mqtt_client.loop_stop()
	
    
if st.button("dummy"):
    pass
