'''
Este modulo va a contener las funciones respondables de la lectura y guardado de información en la base de datos.
'''
import sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)

from Class.class_users import Listener, Musician
def end_load_data(users, songs, albumes, playlists):
    directory = 'db//'
    try: cargar_users(directory, users)
    except FileNotFoundError: 
        open(directory+'users.txt', 'x')
        cargar_users(directory, users)

    try: cargar_albums(directory, albumes)
    except FileNotFoundError:
        open(directory+'albums.txt', 'x')
        cargar_albums(directory, albumes)

    try: cargar_playlists(directory, playlists)
    except FileNotFoundError:
        open(directory+'playlists.txt', 'x')
        cargar_playlists(directory, playlists)
        
    try: cargar_songs(directory, songs)
    except FileNotFoundError:
        open(directory+'songs.txt', 'x')
        cargar_playlists(directory, playlists)
        
        
def cargar_users(directory, users):
    with open(directory+'users.txt', 'w', encoding= 'UTF-8') as data:
        for user in users:
            if type(user) == Listener:
                data.write(f'{user.id};{user.name.strip()};{user.mail};{user.username};{user.tpe};{[user.liked_albm]};{[user.liked_songs]};{[user.liked_musician]};{[]};{[user.liked_playlists]};{user.streams};\n')
            elif type(user) == Musician:    
                data.write(f'{user.id};{user.name.strip()};{user.mail};{user.username};{user.tpe};{[]};{[]};{user.reprototal};\n')
                
def cargar_albums(directory, albumes):
    with open(directory+'albums.txt', 'w', encoding= 'UTF-8') as data:
        for album in albumes:    
            data.write(f'{album.id};{album.name};{album.description};{album.cover};{album.publicate};{album.genre};{album.artist};{[song.id for song in album.tracklist]};{album.repro};\n')
            
def cargar_playlists(directory, playlists):
    with open(directory+'playlists.txt', 'w', encoding= 'UTF-8') as data:
        for playlist in playlists:
            data.write(f'{playlist.id};{playlist.name};{playlist.description};{playlist.creator};{[song.id for song in playlist.tracklist]};\n')
            
def cargar_songs(directory, songs):
    with open(directory+'songs.txt', 'w', encoding= 'UTF-8') as data:
        for song in songs:
            data.write(f'{song.id};{song.name};{song.duration};{song.link};{song.repro};\n')

            

    