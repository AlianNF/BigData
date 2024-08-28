
from conexion import *


def InsertPerson(p):

    db=client.ejemplo1
    collection=db['Person']
    collection.insert_one(p)

def FilterRut(search):
    #conectamos a la database
    db=client.ejemplo1

    collection=db['Person']

    show_data_count = len(list(collection.find(search)))

    if show_data_count > 0:
        show_data = collection.find(search)

        for i in show_data:
            print(i)
    else:
        print('No existe el rut ingresado')