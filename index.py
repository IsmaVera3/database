import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("proyectoisma-8217f-firebase-adminsdk-wou28-feee059bcd.json")

try:
    firebase_admin.initialize_app(cred,{ 'databaseURL' : 'https://proyectoisma-8217f-default-rtdb.firebaseio.com/' })
except:
    print('no tenes wifi jaja')

ref = db.reference('/proyectoisma')

def escritura():
    dato = input('Ingrese el nuevo dato: ')
    id = input('id: ')
    # añadimos un tipo de dato nuevo
    ref.child(id).set({'Datos': dato})

def borro():
    id = input('Ingrese el id del dato que desea borrar: ')
    ref.child(str(id)).delete()

def cambio():
    id = input('Ingrese el id del dato que desea cambiar: ')
    nuevovalor = input('Ingrese el nuevo valor: ')
    ref.child(id).set({'Dato': nuevovalor})

def main():
    while True:
        opcion = int(input('Ingrese 1 para agregar un dato, 2 para borrar un dato o 3 para cambiar un dato: '))
        if opcion == 1:
            print(ref.child("proyectoisma"))
            escritura()
            break
        elif opcion == 2:
            print(ref.child("proyectoisma"))
            borro()
            break
        elif opcion == 3:
            print(ref.child("proyectoisma"))
            cambio()
            break
        else:
            print('debes de escribir un numero del 1 al 3')


main()


