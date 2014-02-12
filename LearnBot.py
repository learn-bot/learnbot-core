import serial
import time
import json
from collections import namedtuple

#Apertura del puerto serie donde está conectada la placa arduino
arduino = arduino = serial.Serial('/dev/ttyUSB0', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1)
arduino.close()
arduino.open()
#Espera 3 segundos
print("Preparing port ...")
time.sleep(3)

#Si el puerto se ha abierto correctamente
if(arduino.isOpen()):
    print("COM Port is opened.")
    arduino.write(str("?0?").encode("us-ascii"))
    while True:
        response = arduino.readline()
        #Si la cadena leida desde el puerto no está vacía
        if(response!=str('').encode("us-ascii")):
            print(response.decode("utf-8"))
            responseObj = json.loads(response.decode("utf-8"), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            print(responseObj.SFRONT.VALUES[0])
           
#Si el puerto no se ha abierto correctamente
else:
    print("COM Port is not available.")
    
    
    
