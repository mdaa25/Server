import passw #donde estaria almaceado los datos de las creddenciales
import paho.mqtt.client as mqtt 
import os, urlparse 




def accion(msg):
#ejercicios diferentes: 
#led=1 / 0 encender el led o apagar el led
#sensor=p/i/l
    mensaje=msg.split('=')
    if (mensaje[0]=='led'):
        if int(mensaje[1]):
            print('led ON')
        else:
            print('led OFF')

    if (mensaje[0]=='led'):
        if int(mensaje[1]):
            print('led ON')
        else:
            print('led OFF')


# Define event callbacks
def publish(msg): # es una funcion creada para publicar un mensaje
	print (msg) # imprime el mensaje
	mqttc.publish(topic, msg)
 
    
# las ON se utiliza en programas diferentes
def on_connect(client, userdata, flags, rc): # sirve para conectarnos al servidor
    print("rc: " + str(rc))
    

def new_message(client, obj, msg): 
    #print('new message='+str(msg.payload));
    accion(str(msg.payload))

def on_publish(client, obj, mid):
    pass#print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

mqttc = mqtt.Client() # crea un nuevo cliente
# Assign event callbacks--- asigna eventos
mqttc.on_message = new_message # evento=funcion, cada vez que ocurra un evento salta a una funcion
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log


# Connect
mqttc.username_pw_set(passw.user, passw.psw) #  son los nombres que se generaron en passw.py donde pendo el server port user psw
mqttc.connect(passw.server, passw.port) # se conecta al server y al puerto
topic='test' # se crea una variable topic
# Start subscribe, with QoS level 0
mqttc.subscribe('led', 0) #como me suscribo al topic, el cero es por defecto, el topic puede ser cualquiera
#cuando se cambia al subscriber se recibira algo diferente a lo que se eat enviando
# Publish a message
mqttc.publish(topic, 'test')# topico, mensaje(se publica mensajes)
#mqttc.publish(topic,topic)
# Continue the network loop, exit when an error occurs
rc = 0
import time
i=0
while rc == 0:
	time.sleep(2)
	i=i+1
	mqttc.publish(topic, 'p='+str(i)) #siempre se utiliza para publicar, mqttc es el cliente y se necesita para publicar
	rc=mqttc.loop()# para recibir mensajes
print("rc: " + str(rc))






