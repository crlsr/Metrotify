
import json, sys, os
actual_dir = os.path.dirname(os.path.abspath(__file__))
principal_dir = os.path.join(actual_dir, '..')
sys.path.append(principal_dir)

from Class.class_songs import Song, Album, Playlist
import utilities

def load_API_songs(songs, albums, playlists):
    directory = 'API//'
    with open(directory+'albums.json', 'r', encoding= 'UTF-8') as data_albums:
            data = json.load(data_albums)
            for album in data:
                alb = Album(album['id'], album['name'], utilities.eliminar(album['description']), album['cover'], album['published'], album['genre'], album['artist'], album['tracklist'])
                cc = 0
                for song in alb.tracklist:
                    sn = Song(song['id'], song['name'], song['duration'], song['link'])
                    if sn in songs:
                        continue
                    else:
                        songs.append(sn)
                    alb.tracklist[cc] = sn
                    cc += 1
                albums.append(alb)

    with open(directory+ '//playlists.json', 'r', encoding= 'uTF-8') as data_playlists:
        data = json.load(data_playlists)
        for playlist in data:
            pl = Playlist(playlist['id'], playlist['name'], utilities.eliminar(playlist['description']), playlist['creator'], playlist['tracks'])
            cc = 0
            for id_num in pl.tracklist:
                for song in songs:
                    if song.id == id_num:
                        pl.tracklist[cc] = song
                    else:
                        continue
                cc += 1
            playlists.append(pl)
            
