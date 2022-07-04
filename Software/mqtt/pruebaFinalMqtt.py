from importlib.metadata import distribution
import paho.mqtt.client as mqtt
import ast

# Funciones de conexión y mensaje
# Al recibir CONNACK desde el servidor
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conexión exitosa")
        print('Codigo de  retorno: ' + str(rc))
         # Inicio o renovación de subscripción
        client.subscribe(topic)
    else:
        print('Fallo en la conexión')

# el tópico tiene una publicación
def on_message(client, userdata, msg):
    #print('Mensaje recibido de ' + msg.topic)
    topic = msg.topic 
    mensaje = str(msg.payload.decode("utf-8"))
    #print('Mensaje: ', mensaje)
    #print('Qos: ', msg.qos)
    atenderSolicitudes(topic, mensaje)
    return ()

# Atiende Solicitud
def atenderSolicitudes(topic:str, mensaje):
    datosCanal = topic.split('/')
    servicio = datosCanal[1]
    tipoSolicitud = datosCanal[2]
    global turno
    turno += 1
    if servicio == 'Bicicletas':
        bicicletas(tipoSolicitud, mensaje, turno)
    elif servicio == 'Bibliotecas':
        bibliotecas(tipoSolicitud, mensaje, turno)
    elif servicio == 'Comedores':
        a = 1
        #comedore(tipoSolicitud, mensaje, turno)
    else:
        print('Este servicio no existe')

def bicicletas(tipoSolicitud, mensaje, turno):
    mensajeDecodificado = definirMensaje(mensaje)
    if tipoSolicitud == 'Petition':
        print('Entró a petición ', turno)
        confirm = {'LocalID':mensajeDecodificado['group'], 'PeID': str(turno)}
    elif tipoSolicitud == 'Validate':
        print('Entró a validate ', turno)
        localID = mensajeDecodificado['LocalID']
        idCarnet = mensajeDecodificado['ID']
        #Busqueda en base de datos y recopilar datos para enviar IDdata (publicador)
    elif tipoSolicitud == 'Borrow':
        print('Entró a borrow ', turno)
        localID = mensajeDecodificado['LocalID']
        idNumber = mensajeDecodificado['IDNumber']
        bike = mensajeDecodificado['Bike']
        #Escritura en la base de datos con bici presta y actualiza datos
    elif tipoSolicitud == 'GiveBack':
        print('Entró a Give Back ', turno)
        localID = mensajeDecodificado['LocalID']
        bike = mensajeDecodificado['Bike']
        status = mensajeDecodificado['Status']
        station = mensajeDecodificado['Station']
        #Actualiza estado, con devolución de bicicleta estación asignada y actualiza lista asignada a funcionario
    elif tipoSolicitud == 'Distribution':
        print('Entró a distribution ', turno)
        localID = mensajeDecodificado['LocalID']
        idNumber = mensajeDecodificado['IDNumber']
        bikes = mensajeDecodificado['Bikes']
        station = mensajeDecodificado['Station']
        #   Actualiza lista de bicis disponibles y actualiza lista asignada a funcionario
    else:
        print('Petición no existente en este servicio')

def bibliotecas(tipoSolicitud, mensaje, turno):
    mensajeDecodificado = definirMensaje(mensaje)
    if tipoSolicitud == 'Petition':
        print('Entró a petición bibliotecas', turno)
        confirm = {'LocalID':mensajeDecodificado['group'], 'PeID': str(turno)}
    elif tipoSolicitud == 'Validate_book':
        print('Entró a Validate Book ', turno)
        idCarnet = mensajeDecodificado['ID']
        #Consulta id y envia datos relacionados al usuario
    elif tipoSolicitud == 'Borrow':
        print('Entró a borrow bibliotecas ', turno)
        idNumber = mensajeDecodificado['IDNumber']
        book = mensajeDecodificado['Book']
        #Asocia el libro al usuario 
    elif tipoSolicitud == 'Give_Back':
        idNumber = mensajeDecodificado['IDNumber']
        book = mensajeDecodificado['Book']
        library = mensajeDecodificado['Library']
    else: 
        print('Petición no existente en este servicio')

def comedores(tipoSolicitud, mensaje, turno):
    mensajeDecodificado = definirMensaje(mensaje)
    if tipoSolicitud == 'Petition':
        print('Entró a petición bibliotecas', turno)
        confirm = {'LocalID':mensajeDecodificado['group'], 'PeID': str(turno)}
    elif tipoSolicitud == 'NewTurn':
        localID = mensajeDecodificado['LocalID']
        idNumber = mensajeDecodificado['IDNumber']
        comedor = mensajeDecodificado['Comedor']
        schedule = mensajeDecodificado['Schedule']
        menu = mensajeDecodificado['Menu']
        #Guarda el nuevo turno y envia el ticket
    elif tipoSolicitud == 'Statistics':
        localID = mensajeDecodificado['LocalID']
        comedor = mensajeDecodificado['Comedor']
        #Busca el comedor y envia las estadisticas
    elif tipoSolicitud == 'Confirmation':
        localID = mensajeDecodificado['LocalID']
        idNumber = mensajeDecodificado['IDNumber']
        #Retorna la confirmación del turno y el restaurante del mismo
    elif tipoSolicitud == 'Payment':
        localID = mensajeDecodificado['LocalID']
        id = mensajeDecodificado['ID']
    elif tipoSolicitud == 'Update':
        localID = mensajeDecodificado['LocalID']
        ticket = mensajeDecodificado['ticket']
        comedor = mensajeDecodificado['Comedor']
    else: 
        print('Petición no existente en este servicio.')

def definirMensaje(mensaje):
    dicMensaje = ast.literal_eval(mensaje)
    return dicMensaje

# INGRESO
# Parametros para la conexión
mqttServer = "127.0.0.1"
port = 1883
clientName = 'SistemaInformacion'
topic = "campus/#"
turno = 0
client = mqtt.Client(clientName)
print('conectando al Broker MQTT ', mqttServer)
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqttServer, port, 60)
client.loop_forever()