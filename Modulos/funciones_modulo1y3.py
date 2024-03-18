'''
Este modulo tiene como finalidad administrar todo los menus y opciones del usuario con respecto al inicio de sesión y la gestion de interacciones.

Este modulo proporciona las siguientes opciones:
-> Inicio de sesión o registro en la app.
-> Buscar perfiles.
-> Realizar ajustes en las propiedades de la cuenta seleccionada.
-> Borrar datos de la cuenta.
'''

#Importamos sys y os para poder redirigir las rutas absolutas de paquetes al sys principal de nuestro modulo con el fin de evitar errores de inportación circular.
import sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)
from utilities import randomid, mailvalidation, validation, int_validatión, username_validation, gmail_norrep
from Class.class_users import Listener, Musician 

'''
En esta función lo que haremos es solicitarle al usuario un nombre de usuario y lo buscamos
en nuestra base de datos momentanea, en caso de que exista buscamos en nuestro array de usuarios
el usuario que posea con dicho nombre de usuario y le asignamos al usuario principal del programa dicho 
objeto user.
'''

#Función para iniciar sesión en el programa.
def log_in(users, main_user): 
    os.system('clear')
    print('💻Inicio de sesión🔐'.center(125))
    while True:
        usernames = [user.username for user in users] #Compresión de lista que toma todos los usernames existentes en nuestra basde de datos momentanea.
        name = input('>> Diga su nombre de usuario: ')
        os.system('clear')
        if name in usernames:
            for user in users:
                if user.username == name:
                    main_user = user
            break
        elif name.casefold() == 'salir':
            break
        else:
            print('Username no existente, porfavor pruebe de nuevo (si desea salir y registrarse, escriba salir)')
    return main_user

#Función para registrarse en el programa.
def register(users: list):
    os.system('clear')
    print('💻Registro de usuario🧑‍💻'.center(125))
    usernames = [user.username for user in users]
    gmails = [user.mail for user in users]
    id = randomid()
    name = input('Diga su nombre: ')
    mail = mailvalidation(input('Diga su gmail: '))
    mail = gmail_norrep(mail, gmails)
    username = input('Diga su nombre de usuario: ') 
    username = username_validation(usernames, username)
    tpe = validation(int_validatión('Que tipo de usuario eres?\n>1. Musician\n>2. Listeners\n>>> '), 1, 2)
    if tpe == 1:
        user = Musician(id, name, mail, username, 'musician')
        users.append(user)
    else:
        user = Listener(id, name, mail, username, 'listener')
        users.append(user)

#Función principal de inicio de sesión. Retorna el usuario con le que se inicio sesión.
def log_in_register(usuarios, user):
    while True:
        os.system('clear')
        elec = validation(int_validatión('>1. Iniciar sesión\n>2. Registrarse \n>3. Salir\n>>Elija que opción desea escribiendola en la terminal.\n\n>>>'), 1, 3)    
        if elec == 1:
            user = log_in(usuarios, user)
            break
        elif elec == 2:
            register(usuarios)
        else:
            os.system('clear')
            return 3 
    os.system('clear')
    return user


'''
Estas funciones tienen como fin configurar todo lo relacionado al sistema de busqueda de la app.
'''

#Buscador del escucha.
def buscador_listener(user, users, songs, albums, playlists):
    while True:
        elec = validation(int_validatión(f'Que deseas buscar {user.name}?\n>1. Usuarios\n>2. Albumes\n>3. Playlists\n>4. Canciones\n>5. Salir\nEscriba la opción que desea elegir\n\n>>>'), 1, 5)
        os.system('clear')
        if elec == 1:
            user_search(users, user) 
        elif elec == 2:
            album_search(albums, user) 
        elif elec == 3:
            playlists_search(playlists, user) 
        elif elec == 4:
            song_search(songs, user) 
        else:
            break  

#Función para bucar usuarios.        
def user_search(users, user1):
    usernames = [user.username for user in users]
    while True:
        search = input('+ Diga el nombre del usuario que esta buscando, si desea salir escriba salir.\n\n>>> ')
        os.system('clear')
        if search in usernames:
            for user in users:
                if user.username == search:
                    if type(user) == Listener:
                        listener_interaction(user, user1)
                    else:
                        musician_interaction(user, user1)
        elif search.casefold() == 'salir':
            break
        else:
            print('Usuario no existente, porfavor vuelva a introducir a otro usuario.')

#Función para buscar albumes.
def album_search(albums, user1):
    names = [album.name for album in albums]
    while True:
        search = input('+ Diga el nombre del album que desea buscar, si desea salir escriba salir.\n\n>>> ')
        os.system('clear')
        if search in names:
            for album in albums:
                if album.name == search:
                    print('estoy')
                    album_interaction(album, user1)
        elif search.casefold() == 'salir':
            break
        else:
            print('Album no existente, porfavor vuelva a introducir otro album.')

#Función para bsucar playlists.
def playlists_search(playlists, user1):
    names = [playlist.name for playlist in playlists]
    while True:
        search = input('Diga la playlist que desea buscar, si desea salir escriba salir.\n\n>>> ') 
        os.system('clear')
        if search in names:
            for playlist in playlists:
                if playlist.name == search:
                    playlist_interaction(playlist, user1)
        elif search.casefold() == 'salir':
            break
        else:
            print('Playlist no existente, porfavor vuelva a introducir otra playlist.')

#Función para buscar canciones
def song_search(songs, user1):
    names = [song.name for song in songs]
    while True:
        search = input('Diga el nombre de la canción que desea buscar, si desea salir escriba salir.\n\n>>>')
        os.system('clear')
        if search in names:
            for song in songs:
                if song.name == search:
                    song_interaction(song, user1)
        elif search.casefold() == 'salir':
            break
        else:
            print('Canción no existente, pruebe con otra canción.')     
            
            
'''
Estas funciones tienen como fin poder gestionar y crear todo el sistema de interación entre el usuario y al buscador
con los objetos que busca.
'''
def listener_interaction(user, user1):
    while True:
        print(f'User = {user.name}\nUsername = {user.username}')
        elec = validation(int_validatión('>1. Ver canciones gustadas\n>2. Ver albumes gustados\n>3. Ver artistas gustados\n>4. Ver playlists guardadas\n>5. Ver playlists creadas\n>6. Salir\n>>>'), 1, 6)
        os.system('clear')
        if elec == 1:
            user.show_songs()
            try: 
                elec2 = validation(int_validatión('Diga el número de la canción con la que desee interactuar (para salir escriba 0)\n>>>'), 0, len(user.liked_songs))
                if elec2 > 0:    
                    song_interaction(user.liked_songs[elec2-1], user1)
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
                    album_interaction(user.liked_albm[elec2-1], user1)
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
                    musician_interaction(user.liked_musician[elec2-1], user1)
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
                    playlist_interaction(user.liked_playlists[elec2-1], user1)
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
                    playlist_interaction(user.created_playlist[elec2-1], user1)
                else:
                    pass
            except AttributeError:
                print('No hay albumes creados')
                continue
        else:
            break
  
def musician_interaction(user, user1):
    while True:
        print(f'Metrotify artist: {user.name}')
        elec = validation(int_validatión(f'>1. Albumes y tracklist de cada uno\n>2. Top 10 canciones más escuchadas\n>3. Reproduciones Totales\n>4. Dar like a {user.name}\n>5. Quitar like a {user.name}\n>6. Salir\n>>>'), 1, 6)
        os.system('clear') 
        if elec == 1:
            user.show_albums()
            elecalb = validation(int_validatión('Elije el número del album con la que desees interactuar (escribe 0 si deseas salir):\n>>>'), 0, len(user.albums))
            if elecalb > 0:
                album_interaction(user.albums[elecalb-1], user1)
            else:
                pass
        elif elec == 2:
            user.show_songs()
            elec2 = validation(int_validatión('Elije el número de la canción con la que desees interactuar (escribe 0 si deseas salir):\n>>>'), 0, len(user.songs))
            if elec2 > 0:
                song_interaction(user.songs[elec2-1], user1)
            else:
                continue
        elif elec == 3:
            print(f'Reproducciones torales de {user.name} = {user.reprototal}')
        elif elec == 4:
            if not user in user1.liked_musician:
                print('👍🏻')
                user1.liked_musician.append(user)
            else:
                print('Ya le diste like a este musico 🥱')
        elif elec == 5:
            if user in user1.liked_musician:
                print('👎🏻')
                user1.liked_musician.remove(user)
            else:
                print('No puedes quitarle el like a un musician al cual no has likeado 🤧')
        else:
            break
        
def album_interaction(album, user1):
    while True:
        print(f'{album.name}\nAlbum de: {album.artist.name}\nCanciones: {len(album.tracklist)}')
        elec = validation(int_validatión('>1. Ver Artista\n>2. Tracklist\n>3. Darle like al Album\n>4. Quitarle like al album\n>5. Salir\n>>>'), 1, 5)
        os.system('clear')
        if elec == 1:
            musician_interaction(album.artist, user1)
        elif elec == 2:
            album.view_tracklist()
            elec2 = validation(int_validatión('Elije el número de la canción con la que desees interactuar(si deseas salir escribe 0):\n>>>'), 0, len(album.tracklist))
            if elec2 > 0:
                song_interaction(album.tracklist[elec2-1], user1)
            else:
                pass
        elif elec == 3:
            if not album in user1.liked_albm:
                print('👍🏻')
                user1.liked_albm.append(album)
                if not album.artist in user1.liked_musician:
                    user1.liked_musician.append(album.artist)
                else:
                    pass
            else:
                print('No puedes darle dos veces like al mismo album flaco 😐')
        elif elec == 4:
            if album in user1.liked_albm:
                print('👎🏻')
                user1.liked_albm.remove(album)
                if album.artist in user1.liked_musician:
                    user1.liked_musician.remove(album.artist)
                else:
                    pass
            else:
                print('No puedes quitarle el like a un album que no has likeado rey 🥸')
        else:
            break
def playlist_interaction(playlist, user1):
    while True:
        print(f'{playlist.name}\nAlbum de: {playlist.creator.name}\nCanciones: {len(playlist.tracklist)}')
        elec = validation(int_validatión('>1. Ver Creador\n>2. Tracklist\n>3. Guardar playlist.\n>4. Quitar de gaurdados\n>5. Salir\n>>>'), 1, 5)
        os.system('clear')
        if elec == 1:
            listener_interaction(playlist.creator, user1)
        elif elec == 2:
            playlist.view_tracklist() #Implementarle la posibilidad de elegir una canción y reproducirla.
            elec2 = validation(int_validatión('Elije el número de la canción con la que desees interactuar: (si deseas salir escribe 0)\n>>>'), 0, len(playlist.tracklist))
            if elec > 0:
                song_interaction(playlist.tracklist[elec2-1], user1)
            else:
                pass
        elif elec == 3:
            if not playlist in user1.liked_playlists:
                print('👍🏻')
                user1.liked_playlists.append(playlist)
            else:
                print('No le puedes guardar dos veces la misma playlist capo 😴')
        elif elec == 4:
            if playlist in user1.liked_playlists:
                print('👎🏻')
                user1.liked_playlists.remove(playlist)
            else:
                print('No puedes quitar de gustados una playlist que no tienes en gustados crack 👁️👄👁️')
        else:
            break
def song_interaction(song, user1):
    while True:
        print(f'{song}')
        elec = validation(int_validatión('>1. Reproducir\n>2. Dar like\n>3. Quitar like\n>4. Salir\n>>> '), 1, 4)
        os.system('clear')
        if elec == 1:
            song.play()
        elif elec == 2:
            if not song in user1.liked_songs:
                print('👍🏻')
                user1.liked_songs.append(song)
            else:
                print('No puedes darle like dos veces a un canción capo 🥱')
        elif elec == 3:
            if song in user1.liked_songs:
                print('👎🏻')
                user1.liked_songs.remove(song)
            else:
                print('No puedes quitarle like a una canción que no tiene tu like 😐')
        else:
            break
        
'''
Este apartado tiene como fin reajustar datos del perfil del usuario o revisar data del mismo.
'''

def gestion_de_perfil(user):
    while True:
        print(f'Que deseas realizar {user.name}?')
        elec = validation(int_validatión('1. Ver datos guardados \n>2. Gestion de datos\n>3. Salir\n>>>'), 1, 3)
        os.system('clear')
        if elec == 1:
            listener_interaction(user, user)
        elif elec == 2:
            settings(user)
        else:
            break

def settings(user):
    while True:
        elec = validation(int_validatión('>1. Cambiar datos personales\n>2. Gestionar música guardada\n>3. Salir\n>>>'), 1, 3)
        os.system('clear')
        if elec == 1:
            user.settings()
        elif elec == 2:
            user.music_settings()
        else:
            break
        