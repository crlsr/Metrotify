def API_filter(users, albums, playlists):
    for album in albums:
        for user in users:
            if album.artist == user.id:
                album.artist = user
            else:
                continue
    for playlist in playlists:
        for user in users:
            if playlist.creator == user.id:
                playlist.creator = user
            else:
                continue