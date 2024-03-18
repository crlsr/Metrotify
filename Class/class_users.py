'''
Este archivo contiene las clases relacionadas con el usuario de Metrotify.
'''
import sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)
from random import randint
from utilities import validation, int_validatión, mailvalidation
#Clase abstracta User:
class User:
    def __init__(self, id, name, mail, username, tpe):
        self.id = id
        self.name = name
        self.mail = mail
        self.username = username
        self.tpe = tpe
    def __repr__(self):
        return self.name


#Subclases de la clase User:
class Musician(User): 
    def __init__(self, id, name, mail, username, tpe, albums = [], songs = [], reprototal = 0):
        super().__init__(id, name, mail, username, tpe)  
        self.albums = albums
        self.songs = songs
        self.reprototal = int(reprototal)
    def __repr__(self):
        return self.id
    def __str__(self):
        return self.name
    
    def settings(self):
        while True:
            print(f'Que desea gestionar de su cuenta {self.name}?')
            elec = validation(int_validatión('>1. Cambiar nombre \n>2. Cambiar nombre de usuario \n>3. Cambiar Gmail\n>4. Salir\n>>>'), 1, 4)
            os.system('clear')
            if elec == 1:
                nombre = input('Diga nuevo nombre: ')
                self.name = nombre
                print('Acción realizada con exito...✅')
            elif elec == 2:
                username_new = input('Diga el nuevo nombre de usuario que desea: ')
                self.username = username_new
                print('Acción realizada con exito...✅')
            elif elec == 3:
                nmail = mailvalidation(input('Diga su nuevo mail: '))
                self.mail = nmail
                print('Acción realizada con exito...✅')
            else:
                break
    
    def show_songsn(self):
        if len(self.songs) <= 1:
            for album in self.albums:
                self.songs += album.tracklist
        else:
            pass
        cc = 0
        for song in self.songs:
            cc += 1
            print(f'\n\n>{cc} {song}\n')
    def show_albums(self):
        cc = 0
        for album in self.albums:
            cc += 1
            print(f'\n\n>{cc} {album}\n')
            print('>> Tracklist:\n')
            for track in album.tracklist:
                print('>>>',track)
                
    def show_songs(self):
        if len(self.songs) <= 1:
            for album in self.albums:
                self.songs += album.tracklist
        else:
            pass
        n = len(self.songs)
        for song in self.songs: #Creamos número aleatorio de visitas para cada canción
            song.repro = randint(1, 100000)
            
        for i in range(n): #Usamos selection sort para organizar las canciones de mayor a menor en función a sus reproducciones.
            max_in = i
            for j in range(i+1, n):
                if self.songs[max_in].repro < self.songs[j].repro:
                    max_in = j
            self.songs[i], self.songs[max_in] = self.songs[max_in], self.songs[i]  
        cc = 0
        
        #Mostramos las canciones.
        for i in range(10):
            cc += 1
            print('Top 10 canciones del artista')
            print(f'>{cc}. {self.songs[i]}')
          
        #Redefinimos las reproducciones del usuario en función a los nuevos valores de las canciones.  
        repros = [song.repro for song in self.songs]
        self.reprototal = sum(repros)
        
    def musical_settings(self):
        while True:
            elec = validation(int_validatión(f'Que deseas hacer {self.name}?\n>1. Gestionar canciones\n>2. Gestionar Albumes\n>3. Salir\n>>>'), 1, 3)
            os.system('clear')
            if elec == 1:
                try:
                    self.show_songsn()
                    elec2 = validation(int_validatión('Diga el número de la canción que desee eliminar (escriba 0 si desea salir)\n>>>'), 0, len(self.songs))
                    if elec2>0:
                        self.songs.pop(elec2-1)
                        print('Operación exitosa...✅')
                    else:
                        continue
                except IndexError:
                    print('No hay canciones')
            elif elec == 2:
                try:
                    self.show_albums()
                    elec2 = validation(int_validatión('Diga el número del album que desea eliminar (si desea salir escriba 0)'), 0, len(self.albums))
                    if elec2 > 0:
                        self.albums.pop(elec2-1)
                        print('Operación exitosa...✅')
                    else:
                        continue
                except IndexError:
                    print('No hay albumes')
            else:
                break
    def stats(self): #Este método tiene como fin mostrarle al músico sus estadisticas generales.
        print(f'Canciones: {len(self.songs)}\nAlbumes: {len(self.albums)}\nReproducciones totales: {self.reprototal}')
            
class Listener(User):
    def __init__(self, id, name, mail, username, tpe, liked_albm = [], liked_songs = [], liked_musician = [], created_playlist = [], liked_playlists = [], streams = 0):
        super().__init__(id, name, mail, username, tpe)    
        self.liked_albm = liked_albm
        self.liked_songs = liked_songs
        self.liked_musician = liked_musician
        self.created_playlist = created_playlist
        self.liked_playlists = liked_playlists
        self.streams = int(streams)
    def __repr__(self):
        return self.id
        
    def show_songs(self):
        cc = 0
        for song in self.liked_songs:
            cc += 1 
            print(f'>{cc}. {song}\n')
    def show_albums(self):
        cc = 0
        for album in self.liked_albm:
            cc += 1 
            print(f'>{cc}. {album}\n')
    def show_playlists(self):
        cc = 0
        for playlist in self.liked_playlists:
            cc += 1 
            print(f'>{cc}. {playlist}\n')
    def show_playlistc(self):
        cc = 0
        for playlist in self.created_playlist:
            cc += 1 
            print(f'>{cc}. {playlist}\n')
    def show_artist(self):
        cc = 0
        for artist in self.liked_musician:
            cc += 1 
            print(f'>{cc}. {artist}\n')
        
    def showatrr(self):
        return f'Username: {self.username}\nAlbumes Gustados: {self.liked_albm}\nCanciones Gustadas{self.liked_songs}\nPlaylists Creadas: {self.created_playlist}\nPlaylists Guardados: {self.liked_playlists}\nArtistas Gustados: {self.liked_musician}\n'
    
    def settings(self):
        while True:
            print(f'Que desea gestionar de su cuenta {self.name}?')
            elec = validation(int_validatión('>1. Cambiar nombre \n>2. Cambiar nombre de usuario \n>3. Cambiar Gmail\n>4. Salir\n>>>'), 1, 4)
            os.system('clear')
            if elec == 1:
                nombre = input('Diga nuevo nombre: ')
                self.name = nombre
                print('Acción realizada con exito...✅')
            elif elec == 2:
                username_new = input('Diga el nuevo nombre de usuario que desea: ')
                self.username = username_new
                print('Acción realizada con exito...✅')
            elif elec == 3:
                nmail = mailvalidation(input('Diga su nuevo mail: '))
                self.mail = nmail
                print('Acción realizada con exito...✅')
            else:
                break
            
    def music_settings(self):
        while True:
            print(f'Que desea gestionar de su musica {self.name}?')
            elec = validation(int_validatión('>1. Canciones guardadas\n>2. Albumes Guardados \n>3. Playlists Guardadas \n>4. Artistas Guardados\n>5. Salir\n>>>'), 1, 5)
            os.system('clear')
            if elec == 1:
                self.show_songs()
                try:
                    elec2 = validation(int_validatión('Diga el número de la canción que desea eliminar (escriba 0 para salir): '), 0, len(self.liked_songs))
                    if elec2 > 0:
                        self.liked_songs.pop(elec2-1)
                        print('Operación exitosa...✅')
                    else:
                        pass
                except IndexError:
                    print('No hay canciones que borrar')
            elif elec == 2:
                self.show_albums()
                try:
                    elec2 = validation(int_validatión('Diga el número del album que desea eliminar (escriba 0 para salir): '), 0, len(self.liked_albm))
                    if elec2 > 0:
                        self.liked_albm.pop(elec2-1)
                        print('Operación exitosa...✅')
                    else:
                        pass
                except IndexError:
                    print('No hay albumes que borrar')
            elif elec == 3:
                self.show_playlists()
                try:
                    elec2 = validation(int_validatión('Diga el número de la playlist que desea eliminar (escriba 0 para salir): '), 0, len(self.liked_playlists))
                    if elec2 > 0:
                        self.liked_playlists.pop(elec2-1)
                        print('Operación exitosa...✅')
                    else:
                        pass
                except IndexError:
                    print('No hay Playlists que borrar')
            elif elec == 4:
                self.show_artist()
                try:
                    elec2 = validation(int_validatión('Diga el número del artista que desea eliminar (escriba 0 para salir): '), 0, len(self.liked_musician))
                    if elec2 > 0:
                        self.liked_musician.pop(elec2-1)
                        print('Operación exitosa...✅')
                    else:
                        pass
                except IndexError:
                    print('No hay artistas que borrar')
            else:
                break