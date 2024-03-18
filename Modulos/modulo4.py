'''
Este modulo tiene como fin crear todas las graficas relacionadas con las estadisticas globales Metrotify (top streams)
'''
import sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)
from Class.class_users import Listener, Musician
from random import randint
from utilities import validation, int_validatión
#Función para generar una cantidad aleatoria de streams para los users y los ordenamos usando selection sort

#Usamos selection sort para organizar las canciones de mayor a menor en función a sus reproducciones.            
def selection_sort_users(listeners, musicians):
    nl = len(listeners)
    for i in range(nl):
        max_ind = i
        for j in range(i+1, nl):
            if listeners[max_ind].streams<listeners[j].streams:
                max_ind = j
        listeners[i], listeners[max_ind] = listeners[max_ind], listeners[i]
    
    nm = len(musicians)
    for i in range(nm):
        max_ind = i
        for j in range(i+1, nm):
            if musicians[max_ind].reprototal<musicians[j].reprototal:
                max_ind = j
        musicians[i], musicians[max_ind] = musicians[max_ind], musicians[i]
    print('Top 5 Streams y Reproducciones en usuarios\n')
    print('Top 5 Listeners')
    cc = 0
    for i in range(5):
        cc += 1
        print(f'>{cc}. {listeners[i].username}\n{listeners[i].streams}\n')

    print('Top 5 Musicians')
    cc = 0
    for i in range(5):
        cc += 1
        print(f'>{cc}. {musicians[i].username}\n{musicians[i].reprototal}\n')

            
def random_stream_users(users):
    listeners = [user for user in users if (type(user) == Listener)] 
    musicians = [user for user in users if (type(user) == Musician)]
    #Generamso cifras random para las streams y reproducciones.
    for listener in listeners:
        listener.streams = randint(1, 100000)
    for musician in musicians:
        musician.reprototal = randint(1, 100000)
    
    selection_sort_users(listeners, musicians)
        
#Función para generar una cantidad aleatoria de streams para los users y los ordenamos usando selection sort
def random_stream_albums(albums):
    for album in albums:
        album.repro = randint(1, 100000)
        
    na = len(albums)
    for i in range(na):
        max_ind = i
        for j in range(i+1, na):
            if albums[max_ind].repro<albums[j].repro:
                max_ind = j
        albums[i], albums[max_ind] = albums[max_ind], albums[i]
    print('\nTop 5 Albumes')
    cc = 0
    for i in range(5):
        cc += 1
        print(f'>{cc}. {albums[i]}\n{albums[i].repro}\n\n')

#Función para generar una cantidad aleatoria de streams para los users y los ordenamos usando selection sort
def random_stream_songs(songs):
    for song in songs:
        song.repro = randint(1, 100000)
        
    na = len(songs)
    for i in range(na):
        max_ind = i
        for j in range(i+1, na):
            if songs[max_ind].repro<songs[j].repro:
                max_ind = j
        songs[i], songs[max_ind] = songs[max_ind], songs[i]
    print('\nTop 5 Canciones')
    cc = 0
    for i in range(5):
        cc += 1
        print(f'>{cc}. {songs[i]}\n\n')
    
#Función principal

def top_streams(users, albums, songs):
    while True:
        elec = validation(int_validatión('>1. Ver top Streams\n>2. Salir\n>>>'), 1, 2)
        if elec == 1:
            os.system('clear')
            random_stream_users(users)
            random_stream_albums(albums)
            random_stream_songs(songs)
        else:
            break


