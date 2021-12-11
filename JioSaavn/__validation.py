
def isJioSaavnUrl(url:str):
    return url.startswith('https://www.jiosaavn.com')

def isAlbumUrl(url:str):
    return isJioSaavnUrl(url) and 'album' in url

def isSongUrl(url:str):
    return isJioSaavnUrl(url) and 'song' in url

def isPlaylistUrl(url:str):
    return isJioSaavnUrl(url) and 'featured' in url or 'playlist' in url