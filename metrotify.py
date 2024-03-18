'''
En este modulo se construye todo el programa principal
'''
import os
from API.user_instance_setter import load_API_users
from API.songs_instance_setter import load_API_songs
from API.load_end import end_load_data
from API.API_users_filter import API_filter
from Modulos import cargado_db
from Modulos.funciones_modulo1y3 import log_in_register, buscador_listener, gestion_de_perfil
from Modulos.funciones_modulo2 import buscador_musician, musician_gestion_de_usuario, crear_album, crear_canción, crear_playlists
from Modulos.modulo4 import top_streams
import utilities as ut

def metrotify(users_list, songs,  albums, playlists):
    current_user = None
    os.system('clear')
    print('🎵Bienvenido a Metrotify🎵'.center(125))
    
    #Carga de datps en función a que tipo de spotify desea ingresar.
    elec1 = ut.validation(ut.int_validatión('En que Metrotify deseas iniciar?:\n>1. Metrotify Beta.\n>2. Metrotify.\n>>>'), 1, 2)
    if elec1 == 1: #Cargando datos de Spotify Beta (API).
        extra_elec = ut.validation(ut.int_validatión('Esta seguro? Recuerde que si inicia desde la versión beta se borraran todos los datos de la app permanentemente.:\n>1. Si, deseo Metrotify Beta.\n>2. Iniciar en Metrotify.\n>>>'), 1, 2)
        if extra_elec == 1: #Advertencia con respecto a la carga de datos.
            load_API_users(users_list)
            load_API_songs(songs, albums, playlists)
        else: 
            cargado_db.load_data_db(users_list, songs, albums, playlists)
            cargado_db.sort_data_db(users_list, songs, albums, playlists)
    #Carga de datos desde la base de datos.
    else:   
        cargado_db.load_data_db(users_list, songs, albums, playlists) 
        cargado_db.sort_data_db(users_list, songs, albums, playlists)
          
    #Inicio de sesión y registro de usuarios
    while True:
        os.system('clear')
        current_user = log_in_register(users_list, current_user)
        try: 
            if current_user.tpe == 'listener':
                while True: #Menu Listener
                    os.system('clear')
                    print(f'Bienvenid@ {current_user.name}')
                    elecprin = ut.validation(ut.int_validatión('Que desea hacer en Metrotify?\n\n>1. Gestionar mi perfil\n>2. Buscar \n>3. Crear Playlist\n>4. Ver estadísticas globales (top streams)\n>5. Cerrar sesión.\n>>> '), 1, 5)
                    if elecprin == 1: #Gestionar mi perfil.
                        gestion_de_perfil(current_user)
                    elif elecprin == 2: #Buscador
                        buscador_listener(current_user, users_list, songs, albums, playlists)
                    elif elecprin == 3: #Crear Playlist
                        crear_playlists(current_user, playlists, songs)
                    elif elecprin == 4: #Ver Estadisticas Globales.
                        top_streams(users_list, albums, songs)
                    else:
                        break
                    
            elif current_user.tpe == 'musician':
                while True: #Menu Musician
                    os.system('clear')
                    print(f'Bienvenid@ {current_user.name}')
                    elecprin = ut.validation(ut.int_validatión('Que desea hacer en Metrotify?\n\n>1. Gestionar mi perfil\n>2. Buscar \n>3. Crear Album\n>4. Crear Canción\n>5. Ver mis estadisticas\n>6. Ver estadísticas globales (Top streams)\n>7. Cerrar sesión.\n>>> '), 1, 7)
                    if elecprin == 1:
                        musician_gestion_de_usuario(current_user)
                    elif elecprin == 2:
                        buscador_musician(current_user, users_list, songs, albums, playlists)
                    elif elecprin == 3:
                        crear_album(current_user, albums)
                    elif elecprin == 4:
                        crear_canción(current_user, songs)
                    elif elecprin == 5:
                        current_user.stats()
                    elif elecprin == 6:
                        top_streams(users_list, albums, songs)
                    else:
                        break
        except AttributeError:
            break
    end_load_data(users_list, songs, albums, playlists)
    print('La universidad Metropolitana te desea. Feliz día 🥸')

users = []
songs = []
albums = []
playlists = []

metrotify(users, songs, albums, playlists)
