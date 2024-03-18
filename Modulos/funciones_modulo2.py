'''
En este modulo estan contenidas las funciones responsables de la creación musical (creación de albumes, playlists y canciones)
Ademas de el buscador del musico
'''
import sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)

from Class.class_users import Listener
from Class.class_songs import Song, Playlist, Album
from utilities import validation, int_validatión, linkvalidation, randomid, getdate

'''
Estos menus estan dedicados a la creación musical de los artistas
'''

#Función para crear canciones:
def crear_canción(user, songs):
    while  True:
        os.system('clear')
        elec = validation(int_validatión('>1. Crear canción\n>2. Salir\n>>>'), 1, 2)
        if elec == 1:
            nombre = input('Nombre de la canción: ')
            minu = validation(int_validatión('Diga cuantos minutos dura su canción\n>>>'), 10, 60) 
            segs = validation(int_validatión('Diga cuantos segundos dura su canción\n>>>'), 10, 60) 
            duration = f'{minu}:{segs}'
            link = linkvalidation()
            x = Song(randomid(), nombre, duration, link)
            user.songs.append(x)
            songs.append(x)
        else:
            break
        
#Función para crear albumes:
def crear_album(user, albums):
    while True:
        elec = validation(int_validatión('>1. Crear album\n>2. Salir\n'), 1, 2)
        os.system('clear')
        if elec == 1:
            elec2 = validation(int_validatión('Cuantas canciones va a tener su album?\n>>>'), 1, 100)
            nombre = input('Nombre del Album: ')
            descripción = input('Descripción del Album:\n>>> ')
            cover = linkvalidation()
            genero = input('Diga el genero de su album: ')
            y = Album(randomid(), nombre, descripción, cover, getdate(), genero, user)
            for i in range(elec2):
                nombre = input('Nombre de la canción: ')
                minu = validation(int_validatión('Diga cuantos minutos dura su canción\n>>>'), 0, 60) 
                segs = validation(int_validatión('Diga cuantos segundos dura su canción\n>>>'), 10, 60) 
                duration = f'{minu}:{segs}'
                link = linkvalidation()
                x = Song(randomid(), nombre, duration, link)
                user.songs.append(x)
                y.tracklist.append(x)
            user.albums.append(y)
        else:
            break
#Función para crear Playlists
def crear_playlists(user, playlists, songs):
    names = [song.name for song in songs]
    while True:
        elec = validation(int_validatión('>1. Crear Playlist\n>2. Salir\n>>>'), 1, 2)
        if elec == 1:
            nombre = input('Nombre de la Playlist: ')
            description = input('Descripción de la playlist: ')
            x = Playlist(randomid(), nombre, description, user)
            while True:
                elec2 = validation(int_validatión('>1. Agregar canción\n>2. Salir\n>>>'), 1, 2)
                if elec2 == 1:
                    song_name = input('Diga el nombre de la canción que desea agregar: ')
                    if song_name in names:
                        for song in songs:
                            if song.name == song_name:
                                x.tracklist.append(song)
                                print('Canción agregada...✅')
                    else:
                        print('Canción no existente')
                else:
                    break
            user.created_playlist.append(x)
        else:
            break

'''
Este menú esta dedicado a la gestion del usuario Musician.
'''
def musician_gestion_de_usuario(user):
    while True:
        elec = validation(int_validatión(f'Que desea gestionar {user.name}?\n>1. Gestionar Datos Personales\n>2. Ver Datos Musicales\n>3. Gestionar Datos Musicales \n>4. Salir\n>>>'), 1, 4)
        os.system('clear')
        if elec == 1:
            user.settings()
        elif elec == 2:
            show_musical_data(user)

        elif elec == 3:
            user.musical_settings()
        else:
            break
        
def show_musical_data(user):
    while True:
        elec = validation(int_validatión('>1. Ver canciones\n>2. Ver top 10 canciones más escuchadas\n>3. Ver albumes\n>4. Salir\n>>>'), 1, 4)
        os.system('clear')
        if elec == 1:
            try:
                user.show_songsn()
                elec2 = validation(int_validatión('Diga el número de la canción con la que desee interactuar(Si desea salir escriba 0).\n\n>>>'), 0, len(user.songs))
                if elec2 > 0:
                    song_interaction(user.songs[elec2-1])
                else:
                    pass
            except AttributeError:
                print('No hay canciones')
        elif elec == 2:
            try:
                user.show_songs()
                elec2 = validation(int_validatión('Diga el número de la canción con la que desee interactuar(Si desea salir escriba 0).\n\n>>>'), 0, 10)
                if elec2 > 0:
                    song_interaction(user.songs[elec2-1])
                else:
                    pass
            except AttributeError:
                print('No hay canciones')
        elif elec == 3:
            try:
                user.show_albums()
                elec2 = validation(int_validatión('Diga el número del album con la que desee interactuar(Si desea salir escriba 0).\n\n>>>'), 0, len(user.albums))
                if elec2 > 0:
                    album_interaction(user.albums[elec2-1])
                else:
                    pass
            except AttributeError:
                print('No hay albumes')
        else:
            break

'''
Estas son las funciones dedicadas a la busqueda del musician (son iguales a las funciones de busqueda del user pero con la diferencia de que no se puede dar like)
'''
def buscador_musician(user, users, songs, albums, playlists):
    while True:
        elec = validation(int_validatión(f'Que deseas buscar {user.name}?\n>1. Usuarios\n>2. Albumes\n>3. Playlists\n>4. Canciones\n>5. Salir\nEscriba la opción que desea elegir\n\n>>>'), 1, 5)
        os.system('clear')
        if elec == 1:
            user_search(users) 
        elif elec == 2:
            album_search(albums) 
        elif elec == 3:
            playlists_search(playlists) 
        elif elec == 4:
            song_search(songs) 
        else:
            break  

#Función para bucar usuarios.        
def user_search(users):
    usernames = [user.username for user in users]
    while True:
        search = input('+ Diga el nombre del usuario que esta buscando, si desea salir escriba salir.\n\n>>> ')
        os.system('clear')
        if search in usernames:
            for user in users:
                if user.username == search:
                    if type(user) == Listener:
                        listener_interaction(user)
                    else:
                        musician_interaction(user)
        elif search.casefold() == 'salir':
            break
        else:
            print('Usuario no existente, porfavor vuelva a introducir a otro usuario.')

#Función para buscar albumes.
def album_search(albums):
    names = [album.name for album in albums]
    while True:
        search = input('+ Diga el nombre del album que desea buscar, si desea salir escriba salir.\n\n>>> ')
        os.system('clear')
        if search in names:
            for album in albums:
                if album.name == search:
                    print('estoy')
                    album_interaction(album)
        elif search.casefold() == 'salir':
            break
        else:
            print('Album no existente, porfavor vuelva a introducir otro album.')

#Función para bsucar playlists.
def playlists_search(playlists):
    names = [playlist.name for playlist in playlists]
    while True:
        search = input('Diga la playlist que desea buscar, si desea salir escriba salir.\n\n>>> ') 
        os.system('clear')
        if search in names:
            for playlist in playlists:
                if playlist.name == search:
                    playlist_interaction(playlist)
        elif search.casefold() == 'salir':
            break
        else:
            print('Playlist no existente, porfavor vuelva a introducir otra playlist.')

#Función para buscar canciones
def song_search(songs):
    names = [song.name for song in songs]
    while True:
        search = input('Diga el nombre de la canción que desea buscar, si desea salir escriba salir.\n\n>>>')
        os.system('clear')
        if search in names:
            for song in songs:
                if song.name == search:
                    song_interaction(song)
        elif search.casefold() == 'salir':
            break
        else:
            print('Canción no existente, pruebe con otra canción.')     
            
            
'''
Estas funciones tienen como fin poder gestionar y crear todo el sistema de interación entre el usuario y al buscador
con los objetos que busca.
'''
def listener_interaction(user):
    while True:
        print(f'User = {user.name}\nUsername = {user.username}')
        elec = validation(int_validatión('>1. Ver canciones gustadas\n>2. Ver albumes gustados\n>3. Ver artistas gustados\n>4. Ver playlists guardadas\n>5. Ver playlists creadas\n>6. Salir\n>>>'), 1, 6)
        os.system('clear')
        if elec == 1:
            user.show_songs()
            try: 
                elec2 = validation(int_validatión('Diga el número de la canción con la que desee interactuar (para salir escriba 0)\n>>>'), 0, len(user.liked_songs))
                if elec2 > 0:    
                    song_interaction(user.liked_songs[elec2-1])
                else:
                    pass
            except AttributeError:
                print('No hay canciones guardadas')
                continue
        elif elec == 2:
            user.show_albums()
            try:
                elec2 = validation(int_validatión('Diga el número del album con el que desee interactuar (si desea salir escriba 0)\n>>>'), 0, len(user.liked_albm))
                if elec2 > 0:    
                    album_interaction(user.liked_albm[elec2-1])
                else:
                    pass
            except AttributeError:
                print('No hay albumes guardados')
                continue
        elif elec == 3:
            user.show_artist()
            try: 
                elec2 = validation(int_validatión('Diga el número del artista con el que desea interactuar (si desea salir escriba 0)\n>>>'), 0, len(user.liked_musician))
                if elec2 > 0:    
                    musician_interaction(user.liked_musician[elec2-1])
                else:
                    pass
            except AttributeError:
                print('No hay artistas guardados')
                continue
        elif elec == 4:
            user.show_playlists()
            try:
                elec2 = validation(int_validatión('Diga el número de la playlist con la que desee interactuar (si desea salir escriba 0)\n>>>'), 0, len(user.liked_playlists))
                if elec2 > 0:    
                    playlist_interaction(user.liked_playlists[elec2-1])
                else:
                    pass
            except AttributeError:
                print('No hay playlist gaurdadas')
                continue
        elif elec == 5:
            user.show_playlistc()
            try:
                elec2 = validation(int_validatión('Diga el número de la playlist con la que desee interactuar (si desea salir escriba 0)\n>>>'), 0, len(user.created_playlist))
                if elec2 > 0:    
                    playlist_interaction(user.created_playlist[elec2-1])
                else:
                    pass
            except AttributeError:
                print('No hay albumes creados')
                continue
        else:
            break
  
def musician_interaction(user):
    while True:
        print(f'Metrotify artist: {user.name}')
        elec = validation(int_validatión(f'>1. Albumes y tracklist de cada uno\n>2. Top 10 canciones más escuchadas\n>3. Reproduciones Totales\n>4. Salir\n>>>'), 1, 4)
        os.system('clear') 
        if elec == 1:
            user.show_albums()
            elecalb = validation(int_validatión('Elije el número del album con la que desees interactuar (escribe 0 si deseas salir):\n>>>'), 0, len(user.albums))
            if elecalb > 0:
                album_interaction(user.albums[elecalb-1])
            else:
                pass
        elif elec == 2:
            user.show_songs()
            elec2 = validation(int_validatión('Elije el número de la canción con la que desees interactuar (escribe 0 si deseas salir):\n>>>'), 0, len(user.songs))
            if elec2 > 0:
                song_interaction(user.songs[elec2-1])
            else:
                continue
        elif elec == 3:
            print(f'Reproducciones torales de {user.name} = {user.reprototal}')
        else:
            break
        
def album_interaction(album):
    while True:
        print(f'{album.name}\nAlbum de: {album.artist.name}\nCanciones: {len(album.tracklist)}')
        elec = validation(int_validatión('>1. Ver Artista\n>2. Tracklist\n>3. Salir\n>>>'), 1, 3)
        os.system('clear')
        if elec == 1:
            musician_interaction(album.artist)
        elif elec == 2:
            album.view_tracklist()
            elec2 = validation(int_validatión('Elije el número de la canción con la que desees interactuar(si deseas salir escribe 0):\n>>>'), 0, len(album.tracklist))
            if elec2 > 0:
                song_interaction(album.tracklist[elec2-1])
            else:
                pass
        else:
            break
def playlist_interaction(playlist):
    while True:
        print(f'{playlist.name}\nAlbum de: {playlist.creator.name}\nCanciones: {len(playlist.tracklist)}')
        elec = validation(int_validatión('>1. Ver Creador\n>2. Tracklist\n>3. Salir\n>>>'), 1, 3)
        os.system('clear')
        if elec == 1:
            listener_interaction(playlist.creator)
        elif elec == 2:
            playlist.view_tracklist() #Implementarle la posibilidad de elegir una canción y reproducirla.
            elec2 = validation(int_validatión('Elije el número de la canción con la que desees interactuar: (si deseas salir escribe 0)\n>>>'), 0, len(playlist.tracklist))
            if elec > 0:
                song_interaction(playlist.tracklist[elec2-1])
            else:
                pass
        else:
            break
def song_interaction(song):
    while True:
        print(f'{song}')
        elec = validation(int_validatión('>1. Reproducir\n>2. Salir\n>>> '), 1, 2)
        os.system('clear')
        if elec == 1:
            song.play()
        else:
            break
        
