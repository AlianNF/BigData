#este archivo sirve para llamar a las funciones que se encuentran en el archivo models.py
#tambien sirve para solicitar datos de entrada

from models import *


#ingresamos datos

def Ingresa():
    #solicita datos a n personas
    while True:
        #ingresa datos
        nombre = input('Ingresa el nombre\n')
        try:
            edad = int(input('Ingresa la edad\n'))
        except:
            print('No se ingreso un numero, se asumira cero')
            edad=''
        rut = input('Ingresa el rut\n')
        #fin ingreso de datos
        #json para enviar al metodo de insert
        p={}
        if len(nombre)>0:
            p['nombre'] = nombre
        if len(str(edad)>0):
            p['edad'] = edad
        if len(rut>0):
            p['rut']=rut
        #fin del json para enviar el metodo de insercion
        InsertPerson(p)
        opcion=input("si para continuar, no para finalizar\n")
        while opcion.lower()!='si' and opcion.lower()!='no':
            print('error\n')
            opcion=input("si para continuar, no para finalizar\n")
        if opcion == 'no':
            break #fin del ciclo
#fin del ciclo para crear datos
def MuestraDatosRut():
    return