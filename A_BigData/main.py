#lanza la aplicacion y funciona como interfaz de usuario
from funciones import *

def Main():
    while True:
        try:
            opcion = int(input('1. para llenar\n2. para ver\n3. para salir'))
            while opcion < 1 or opcion > 4:
                print('error')
                opcion = int(input('1. para llenar\n2. para ver\n3. para salir'))
        except:
            print('error')
    
        if opcion==1:
            Ingresa()
        if opcion==2:
            MuestraDatosRut()
        if opcion==3:
            break

Main()