'''
Este archivo contiene las clases relacionadas con las canciones, albumes, etc... de Metrotify.
'''
import webbrowser #Importamos webbroser para poder reproducir nuestras canciones en la web

#Clase Song
class Song:
    def __init__(self, id, name, duration, link, repro = 0):
        self.id = id
        self.name = name
        self.duration = duration
        self.link = link
        self.repro = int(repro)
        
    def play(self): #Método que permite que la canción se reproduzca para el usuario. #####CAMBIARRRRR
        webbrowser.open(self.link)
        self.repro += 1
    def __str__(self): #Este método nos permite definir como deseamos que se vea el objeto en la terminal al imprimirlo.
        return f'{self.name}\n{self.duration}\n{self.repro}'
    def __repr__(self): #Este método nos permite definir como deseamos que se vea nuestro objeto dentro de una estructura de datos.
        return self.id
        
#Clase Album
class Album:
    def __init__(self, id, name, description, cover, publicate, genre, artist, tracklist = [], repro = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cover = cover
        self.publicate = publicate
        self.genre = genre
        self.artist = artist
        self.tracklist = tracklist
        self.repro = int(repro)
    def view_tracklist(self): #Este método tiene como finalidad enseñar todo el tracklist del album.
        cc = 0 
        for i in self.tracklist:
            cc+=1
            print('>>',cc, i)
    def __str__(self): #Este método nos permite definir como deseamos que se vea el objeto en la terminal al imprimirlo.
        return f'{self.name}\n\n{self.description}'
    def __repr__(self):
        return self.id
  
#Clase Playlist  
class Playlist:
    def __init__(self, id, name, description, creator, tracklist = []):
        self.id = id
        self.name = name
        self.description = description
        self.creator = creator
        self.tracklist = tracklist
    def view_tracklist(self): #Este método tiene como finalidad enseñar todo el tracklist de la playlist.
        cc = 0 
        for i in self.tracklist:
            cc+=1
            print('>>',cc, i)
    def __repr__(self) -> str:
        return self.id
    def remove_song(self):
        self.view_tracklist()
        elec = input('Diga el número de la canción que desea eliminar de la playlist\n>>>')
        #validation use
        del self.tracklist[elec-1]
    def __str__(self): #Este método nos permite definir como deseamos que se vea el objeto en la terminal al imprimirlo.
        return f'{self.name}\n\n{self.description}\n' 