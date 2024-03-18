'''
En este modulo se van a crear las instancias en función a lo encontrado en la API (en caso de no encontrar la base de datos creara el archivo).
'''
import sys, os, json
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)

from Class.class_users import Musician, Listener

def load_API_users(user: list):
    print('Iniciando descarga del API...')
    directory = 'API//'
    with open(directory + 'users.json', 'r') as data_users:
        data = json.load(data_users)
        for users in data:
            if users['type'] == 'musician':
                user.append(Musician(users['id'], users['name'], users['email'], users['username'], users['type']))
            else:
                user.append(Listener(users['id'], users['name'], users['email'], users['username'], users['type']))
            
    print('Descarga completada de manera exitosa...')

'''
try: 
    with open('db//bd_users', 'r') as db:
        db.read()
except FileNotFoundError: open('db//bd_users', 'x')
'''




