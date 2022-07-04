import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

# Al recibir CONNACK desde el servidor
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conexión exitosa")
        print('Codigo de  retorno: ' + str(rc))
         # Inicio o renovación de subscripción
        client.subscribe(topic)
    else:
        print('Fallo en la conexión')

def on_message(client, userdata, msg):
    print('Mensaje recibido de ' + msg.topic)
    topic = msg.topic 
    mensaje = str(msg.payload.decode("utf-8"))
    print('Mensaje: ', mensaje)
    #print('Qos: ', msg.qos)
    return ()

mqttBroker = "127.0.0.1"
client = mqtt.Client()
topic = "campus/Bicicletas/Petition"
port = 1883
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqttBroker, port, 60)
i = 1
while True:
    if i == 1:
        mensaje = {'LocalID': '1012451451', 'group':2}
        client.publish("campus/Bicicletas/Petition", str(mensaje))
        print(mensaje)
    elif i == 2:
        mensaje = {'LocalID': '1012451451', 'ID':52475874}
        client.publish("campus/Bicicletas/Validate", str(mensaje))
        print(mensaje)
    elif i == 3:
        mensaje = {'LocalID': '1012451451', 'IDNumber':586, 'Bike': 4}
        client.publish("campus/Bicicletas/Borrow", str(mensaje))
        print(mensaje)
    elif i == 4:
        mensaje = {'LocalID': '1012451451', 'Bike':2, 'Status': 'dañada', 'Station': 'CyT'}
        client.publish("campus/Bicicletas/GiveBack", str(mensaje))
        print(mensaje)
    elif i == 5:
        mensaje = {'LocalID': '1012451451', 'IDNumber':586, 'Bikes': 6, 'Station': 'entrada 30'}
        client.publish("campus/Bicicletas/Distribution", str(mensaje))
        print(mensaje)
    else: 
        mensaje = {'LocalID': '1012451451', 'group':1}
        client.publish("campus/Bicicletas/Petition", str(mensaje))
        print(mensaje) 
    i+=1
    time.sleep(4)
client.loop_forever()