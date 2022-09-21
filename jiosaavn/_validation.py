
from . import _exceptions


def isJioSaavnUrl(url:str):
    if not url.startswith('https://www.jiosaavn.com'):
        raise _exceptions.InvalidURL('Please provide a valid jiosaavn url')

def isAlbumUrl(url:str):
    isJioSaavnUrl(url)
    if not ('album' in url):
        raise _exceptions.InvalidURL('Please provide a valid jiosaavn album url')


def isSongUrl(url:str):
    isJioSaavnUrl(url)
    if not ('song' in url):
        raise _exceptions.InvalidURL('Please provide a valid jiosaavn song url')


def isPlaylistUrl(url:str):
    isJioSaavnUrl(url)
    if not ('featured' in url or 'playlist' in url):
        raise _exceptions.InvalidURL('Please provide a valid jiosaavn playlist url')


URL_FUNCTION = { 
    'song' : isSongUrl,
    'album' : isAlbumUrl,
    'playlist' : isPlaylistUrl,
    # 'artist' : _artistSearchResponse,
    }