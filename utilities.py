'''
En este mnodulo se van a crear funciones las cuales luego utilizaremos como herramientas para podermejorar
el funcionamiento de nuesteo codigo.
'''
#Importamos la libreria uuid para poder crear una función la cual pueda generar ids al azar y request para validar inputs de links.
import uuid, requests, os
from datetime import datetime

#Esta función tiene como fin validar un falor en función a un rango de valores que le pasemos.
def validation(val, minval, maxval): 
    while val<minval or val>maxval:
        try:
            val = int(input (f'Error, recuerde que los valores que puede elegir van desde {minval} hasta {maxval}: '))
        except ValueError:
            print('Valor incorrecto, solo se admiten números')
    return val

#Esta función tiene como fin crear ids al azar para cada usuario, cancion o arreglo de canciones (como albums y playlists) que se creen.
def randomid(): 
    return str(uuid.uuid4())

#Función para obtener el tiempo actual.
def getdate():
    return datetime.now()

#Esta función tiene como fin validar si un link tiene lo necesario para ser un link real.
def linkvalidation(): 
    while True:
        link = input('Diga link: ')
        try:
            response = requests.get(link)
            if response.status_code == 200:
                return link
            else:
                print('Error, link incorrecto')
                continue
        except requests.exceptions.RequestException:
            print('Error, link incorrecto')
            continue
            
  

#Función para eliminar saltos de linea no deseados en strings.     
def eliminar(string):
    new_str = string.replace('\n', '')
    return new_str

#FUnción para validar un mail.
def mailvalidation(mail):
    while not '@' in mail:
        mail = input('Gmail no valido, recuerde que su gmail debe de tener al menos un @: ')
    return mail

#Función para eliminar corchetes extras en un string.
def eliminatecorch(string):
    new_str = string.replace('[', '').replace(']', '')
    return new_str

#Función para validar que un input es efectivamente un número, en caso de que sea número se retorna el valor introducido
def int_validatión(string):
    while True:
        try: 
            valor = int(input(string))
            return valor 
        except ValueError:
            print('Error, valor incorrecto, solo se admiten números.')
            
#Funciones para evitar que un usuario se registren con el mismo username o gmail:
def username_validation(usernames, user):
    while user in usernames:
        user = input('Usuario ya existente, porfavor pruebe de uno nuevo con un nuevo username: ')
    return user

def gmail_norrep(gmail, gmails):
    while gmail in gmails:
        gmail = mailvalidation(input('Mail ya existente, porfavor ingrese otro: '))
    return gmail
  


        
    