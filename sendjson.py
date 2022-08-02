import paho.mqtt.client as mqtt
import base64
import json

try:
    client = mqtt.Client()
    client.connect('mqtt.eclipseprojects.io')
    client.subscribe("topic")

    def on_message(client, userdata, message):
        msg = str(message.payload.decode('utf-8'))

        f = msg.encode("ascii")

        final = base64.b64decode(f)

        open('receive.json', 'wb').write(final)

    client.on_message = on_message

    client.loop_forever()


except KeyboardInterrupt:
    print("user have entered ctrl + c \n exit...")
