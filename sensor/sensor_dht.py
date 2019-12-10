#!/usr/bin/python

# Importa las librerias necesarias
import sys
import time
import Adafruit_DHT
import os
import requests


# Configuracion del tipo de sensor DHT
sensor = Adafruit_DHT.AM2302 # corresponde al sensor que estoy utilizando...
#print("hola")

# Configuracion del puerto GPIO al cual esta conectado  (GPIO 23)
pin = 23

# Intenta ejecutar las siguientes instrucciones, si falla va a la instruccion except

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

params = (
    ('db', 'temperature'),
)

while True:
    try:
    # caps,machine=vsbc1A,type=virtual cap=9,max_peer=9
        data = 'sensor,machine=pi1,type=sensor temperature=%s,humidity=%s' % (temperature,humidity)

        response = requests.post('http://localhost:8086/write', params=params, data=data)
        time.sleep(3)
        print(data + " " + response)

    except Exception as e:

        print(e)
