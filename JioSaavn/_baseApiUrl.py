

def albumFromID(id:int):
    return f'https://www.jiosaavn.com/api.php?__call=content.getAlbumDetails&_format=json&cc=in&_marker=0%3F_marker=0&albumid={id}'

def albumsearchFromSTRING(query:str):
    return f'https://www.jiosaavn.com/api.php?__call=autocomplete.get&_format=json&_marker=0&cc=in&includeMetaTags=1&query={"+".join(query.split(" "))}'

def songFromID(id:str):
    return f'https://www.jiosaavn.com/api.php?__call=song.getDetails&cc=in&_marker=0%3F_marker%3D0&_format=json&pids={id}'

def songsearchFromSTRING(query:str,p:int,n:int):
    return f'https://www.jiosaavn.com/api.php?p={p}&_format=json&_marker=0&api_version=4&ctx=wap6dot0&n={n}&__call=search.getResults&q={"+".join(query.split(" "))}'

def lyricsFromID(id:str):
    return f'https://www.jiosaavn.com/api.php?__call=lyrics.getLyrics&ctx=web6dot0&api_version=4&_format=json&_marker=0%3F_marker=0&lyrics_id={id}'

def playlistFromID(id:str):
    return f'https://www.jiosaavn.com/api.php?__call=playlist.getDetails&_format=json&cc=in&_marker=0%3F_marker%3D0&listid={id}'
