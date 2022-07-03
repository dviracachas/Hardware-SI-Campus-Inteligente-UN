import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "127.0.0.1"
client = mqtt.Client("Bibliotecas")
client.connect(mqttBroker)

i = 1
while True:
    if i == 1:
        mensaje = {'localID': '1012451451', 'group':2}
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