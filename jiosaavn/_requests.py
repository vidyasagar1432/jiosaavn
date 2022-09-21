
import json
import random
import aiohttp
import requests

from enum import Enum

class Response(Enum):
    json = 'json'
    text = 'text'

data = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        ]

def getHeaders():
    return {
        'Host': 'www.jiosaavn.com',
        'accept': 'application/json, text/plain, */*',
        'user-agent': random.choice(data),
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9'
        }


def syncGet(url:str, response:Response=Response.json, params=None):

    _response = requests.get(url=url,headers=getHeaders(),params=params)

    if _response.status_code == 200:

        if response.value == Response.json.name:
            return _response.json()
        
        return _response.text


async def asyncGet(url:str, response:Response=Response.json, params=None):

    async with aiohttp.ClientSession(headers=getHeaders()) as session:
        async with session.get(url,data=params) as _response:
            if _response.status == 200:

                textResponse = await _response.text()

                if response.value == Response.json.name:
                    return json.loads(textResponse)
                
                return textResponse
                


def _albumSearch(query:str):
    '''Limited use'''
    return f'https://www.jiosaavn.com/api.php?__call=autocomplete.get&_format=json&_marker=0&query={"+".join(query.split(" "))}'

# def song(id:str):
#     return f'https://www.jiosaavn.com/api.php?__call=song.getDetails&cc=in&_marker=0%3F_marker%3D0&_format=json&pids={id}'

# def album(id:int):
#     return f'https://www.jiosaavn.com/api.php?__call=content.getAlbumDetails&_format=json&cc=in&_marker=0%3F_marker=0&albumid={id}'

# def playlist(id:str):
#     return f'https://www.jiosaavn.com/api.php?__call=playlist.getDetails&_format=json&cc=in&_marker=0%3F_marker%3D0&listid={id}'

# def lyrics(id:str):
#     return f'https://www.jiosaavn.com/api.php?__call=lyrics.getLyrics&lyrics_id={id}&ctx=web6dot0&api_version=4&_format=json&_marker=0'


'https://www.jiosaavn.com/api.php?__call=search.topAlbumsoftheYear&api_version=4&_format=json&_marker=0&ctx=web6dot0&album_year=2022&album_lang=punjabi'
'https://www.jiosaavn.com/api.php?__call=content.getTrending&api_version=4&_format=json&_marker=0&ctx=web6dot0&entity_type=album&entity_language=punjabi'
'https://www.jiosaavn.com/api.php?__call=search.artistOtherTopSongs&api_version=4&_format=json&_marker=0&ctx=web6dot0&artist_ids=742638&song_id=yCgClm0_&language=punjabi'
'https://www.jiosaavn.com/api.php?__call=reco.getAlbumReco&api_version=4&_format=json&_marker=0&ctx=web6dot0&albumid=34303918'

# API_URLS ={ 
#     'song' : song,
#     'album' : album,
#     'playlist' : playlist,
#     # 'artist' : 'getArtistResults',
#     'lyrics' : lyrics
#     }

API_CORE_FUNCTION ={ 
    'song' : 'song.getDetails&pids',
    'album' : 'content.getAlbumDetails&albumid',
    'playlist' : 'playlist.getDetails&listid',
    # 'artist' : 'artist.getDetails&pids',
    'lyrics' : 'lyrics.getLyrics&lyrics_id'
    }


def coreApiURL(id:str,type:str):
    return f'https://www.jiosaavn.com/api.php?__call={API_CORE_FUNCTION[type]}={id}&ctx=web6dot0&api_version=4&_format=json&_marker=0'


API_SEARCH_FUNCTION = { 
    'song' : 'getResults',
    'album' : 'getAlbumResults',
    'playlist' : 'getPlaylistResults',
    'artist' : 'getArtistResults',
    }

def searchApiURL(query:str,type:str, page:int, limit:int):
    return f'https://www.jiosaavn.com/api.php?p={page}&q={"+".join(query.split(" "))}&_format=json&_marker=0&api_version=4&ctx=web6dot0&n={limit}&__call=search.{API_SEARCH_FUNCTION[type]}'





