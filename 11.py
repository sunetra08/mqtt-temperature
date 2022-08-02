import base64
import paho.mqtt.client as mqtt
# from paho.mqtt import client as mqtt
import requests
import time
import json
import random


def weather():
    api_key = "APIKEY__2"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = 'KOLKATA'

    complete_url = base_url + "appid=" + \
        'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        current_temperature = y["temp"]-273.25
        current_temperature = "{:.2f}".format(current_temperature)

        return current_temperature

    else:
        return(" City Not Found ")


di = {}
i = 0
try:
    while True:
        ops = random.randint(0, 10)
        di[f"temperature"+str(i)] = str(weather())
        time.sleep(0.1)
        print(di)
        i += 1

except KeyboardInterrupt:
    json_object = json.dumps(di)
    with open("2.json", "w") as file:
        file.write(json_object)
    print("user have pressed ctrl + c \n exit...")


client = mqtt.Client()
client.connect('mqtt.eclipseprojects.io')
client.subscribe("topic")


with open('2.json', 'rb') as file:
    f = file.read()

j = f
base64_bytes = base64.b64encode(j)
base64_m = base64_bytes.decode('ascii')

client.publish('topic', base64_m)
