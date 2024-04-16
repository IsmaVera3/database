import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("C:\\Users\\PROA_109\\Documents\\6to Programacion\\base datos\\proyectoisma-8217f-firebase-adminsdk-wou28-feee059bcd.json")
firebase_admin.initialize_app(cred)
ref = db.reference('/proyectoisma')
firebase_admin.initalize_app(cred,{ 'databaseURL' : 'https://proyectoisma-8217f-default-rtdb.firebaseio.com/' })

def main():
    opcion = int(input('Ingrese 1 para agregar un dato, 2 para borrar un dato o 3 para cambiar un dato: '))
    
    if opcion == 1:
        dato = input('Ingrese el nuevo dato: ')
        # añadimos un tipo de dato nuevo
        db.collection('proyectoisma').add({'nose': dato})
    elif opcion == 2:
        dato = input('Ingrese el dato que desea borrar: ')
        # borramos dato
        # .where busca el dato
        # .stream itera por todo el diccionario
        docs = db.collection('proyectoisma').where('dato', '==', dato).stream()
        for i in docs:
            i.reference.delete()
    elif opcion == 3:
        posicion = int(input('Ingrese la posición del dato que desea cambiar: '))
        nuevovalor = input('Ingrese el nuevo valor: ')
        docs = db.collection('proyectoisma').stream()
        contador = 1
        for i in docs:
            if contador == posicion:
                # cambiamos el valor
                i.reference.update({'dato': nuevovalor})
                break
            contador += 1
    else:
        print('debes de escribir un numero del 1 al 3')


main()
