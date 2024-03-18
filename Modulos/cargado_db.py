import sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)

from Class.class_users import Listener, Musician
from Class.class_songs import Song, Album, Playlist

def load_data_db(users, songs, albums, playlists):
    directory = 'db//'
    try: load_users_db(directory, users)
    except FileNotFoundError:
        open(directory + 'users.txt', 'x')
        load_users_db(directory, users) 
    try: load_songs_db(directory, songs)
    except FileNotFoundError:
        open(directory + 'songs.txt', 'x')
        load_songs_db(directory, songs)
        
    try: load_albums_db(directory, songs, albums)
    except FileNotFoundError:  
        open(directory + 'albums.txt', 'x')
        load_songs_db(directory, songs)
        
    try: load_playlists_db(directory, songs, playlists)
    except FileNotFoundError: 
        open(directory + 'playlists.txt', 'x')
        load_playlists_db(directory, songs, playlists)

def sort_data_db(users, songs, albums, playlists):
    sort_songs_arrays(users , albums, playlists)
    sort_users_data(songs, albums, playlists, users)
    format_users(users)
    
    
def load_users_db(directory, users: list):
    with open(directory + 'users.txt', 'r') as data:
        for user in data:
            array = user.split(';')
            array.pop()
            if 'listener' in array:
                id, name, mail, username, tpe, liked_albm, liked_songs, liked_musician, created_playlist, liked_playlists, streams = array
                liked_albm = getarray(liked_albm)
                liked_songs = getarray(liked_songs)
                liked_musician = getarray(liked_musician)
                created_playlist = getarray(created_playlist)
                liked_playlists = getarray(liked_playlists)
                x = Listener(id, name, mail, username, tpe, liked_albm, liked_songs, liked_musician, created_playlist, liked_playlists, streams)
                users.append(x)
            elif 'musician' in array:
                id, name, mail, username, tpe, albums, songs, reprototal = array
                albums = getarray(albums)
                songs = getarray(songs)
                y = Musician(id, name, mail, username, tpe, albums, songs, reprototal)
                users.append(y)
            else:
                pass
                
def load_songs_db(directory, songs):
    with open(directory + 'songs.txt', 'r', encoding= 'UTF-8') as data:
        for song in data:
            array = song.split(';')
            array.pop()
            id, name, duration, link, repro = array
            songs.append(Song(id, name, duration, link, repro))
            
def load_albums_db(directory, songs, albums):
    with open(directory + 'albums.txt', 'r', encoding= 'UTF-8') as data:
        for album in data:
            array = album.split(';')
            array.pop()
            id, name, description, cover, publicate, genre, artist_id, tlist, repro = array
            tracklist = getarray(tlist)
            alb = Album(id, name, description,cover, publicate, genre, artist_id, tracklist, repro)
            cc = 0
            for song_id in alb.tracklist:
                for song in songs:
                    if song.id == song_id:
                        alb.tracklist[cc] = song
                        cc += 1
                    else:
                        continue
            albums.append(alb)
                
def load_playlists_db(directory, songs, playlists):
    with open(directory + 'playlists.txt', 'r', encoding= 'UTF-8') as data:
        for playlist in data:
            array = playlist.split(';')
            array.pop()
            id, name, description, creator, tracklist = array
            tracklist = getarray(tracklist)
            pl = Playlist(id, name, description, creator, tracklist)
            cc = 0
            for song_id in pl.tracklist:
                for song in songs:
                    if song.id == song_id:
                        pl.tracklist[cc] = song
                        cc += 1
                    else:
                        continue
            playlists.append(pl)

def sort_songs_arrays(users, albums, playlists):
    for user in users:
        if type(user) == Musician:
            for album in albums:
                if user.id == album.artist:
                    album.artist = user
        else:
            for playlist in playlists:
                if user.id == playlist.creator:
                    playlist.creator = user
                            
def sort_users_data(songs, albums, playlists, users): 
    for user in users:
        if type(user) == Listener:
        #Ordenamiento de datos Listeners
            cc = 0
            dd = 0
            mm = 0
            bb = 0
            pp = 0
            for id in user.liked_albm:
                for album in albums:
                    if album.id == id:
                        if type(user.liked_songs[0]) == '':
                            user.liked_songs.pop(0)
                        else:
                            pass
                        user.liked_albm[cc] = album
                        cc += 1
                    
            for id in user.liked_songs:
                for song in songs:
                    if song.id == id:
                        if type(user.liked_songs[0]) == '':
                            user.liked_songs.pop(0)
                        else:
                            pass
                        user.liked_songs[dd] = song
                        dd += 1
                    
            for id in user.liked_musician:
                for musician in users:
                    if musician.id == id:
                        if type(user.liked_musician[0]) == '':
                            user.liked_musician.pop(0)
                        else:
                            pass
                        user.liked_musician[mm] = musician
                        mm += 1
            
            for id in user.liked_playlists:
                for playlist in playlists:
                    if playlist.id == id:
                        if type(user.liked_playlists[0]) == '':
                            user.liked_playlists.pop(0)
                        else:
                            pass
                        user.liked_playlists[bb] = playlist
                        bb += 1
                                    
            for playlist in playlists:
                if user == playlist.creator:
                    user.created_playlist.append(playlist) 
                  
        else:
            #Odenamiento datos musicians:
            for album in albums:
                if user == album.artist:
                    user.albums.append(album)
            for id in user.songs:
                if user.songs[0] == '':
                    user.songs.pop(0)
                else:
                    pass
                for song in songs:
                    if song.id == id:
                        user.songs[pp] = song
                        pp += 1
                       
def getarray(miniarray):
    array = miniarray.replace('[', '').replace(']', '')
    array = array.split(',')
    cc = 0
    for s_id in array:
        s_id = s_id.strip().replace("'", '')
        array[cc] = s_id
        cc += 1
    return array

def format_users(users):
    musicians = [user for user in users if(type(user) == Musician)]
    listeners = [user for user in users if(type(user) == Listener)]
    for user1 in listeners:
        user1.created_playlist.pop(0)
    for user2 in musicians:
        user2.albums.pop(0)
        



        


