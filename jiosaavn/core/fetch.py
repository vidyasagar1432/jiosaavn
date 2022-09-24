import json
import random
import aiohttp
import requests

from enum import Enum

from . import encoder ,validate, parsers ,exceptions
from .encoder import SetIntStr,DictIntStrAny ,Optional

class Type(Enum):
    song = 'song'
    album = 'album'
    playlist = 'playlist'
    lyrics ='lyrics'

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


def syncGet(url:str):
    _response = requests.get(url=url,headers=getHeaders(),params=params)
    if _response.status_code == 200:
            return _response.json()



async def asyncGet(url:str):
    async with aiohttp.ClientSession(headers=getHeaders()) as session:
        async with session.get(url) as _response:
            if _response.status == 200:
                textResponse = await _response.text()
                return json.loads(textResponse)

                



# info = {

#     "song": {
#         'id' : {
#             'url' : lambda id: f'{BASE_URL}song.getDetails&pids={id}{FORMAT}{MAKER}{VERSION(0)}{CTX}',
#             'parse' : encoder.song,
#         },
#         'url':{
#             'url': lambda token: f'{BASE_URL}webapi.get&token={token}&type=song{FORMAT}{MAKER}{VERSION(0)}{CTX}',
#             'parse' : encoder.song,
#             'validate' : validate.isSongUrl
#         },
#         'parse' : parsers._parseSong
#     },

#     'album' :{
#         'id' : {
#             'url' : lambda id: f'{BASE_URL}content.getAlbumDetails&albumid={id}{FORMAT}{MAKER}{VERSION(0)}{CTX}',
#             'parse' : encoder.album,
#         },
#         'url':{
#             'url': lambda token: f'{BASE_URL}webapi.get&token={token}&type=album{FORMAT}{MAKER}{VERSION(0)}{CTX}',
#             'parse' : encoder.album,
#             'validate' : validate.isAlbumUrl
#         },
#         'parse' : parsers._parseAlbum
#     },

    # # with `id` all songs will return
    # # with `url` 5 songs will return but can get next 5.... by &p=1,2,3,4... 
    # 'playlist':{
    #     'id' : {
    #         'url' : lambda id: f'{BASE_URL}playlist.getDetails&listid={id}{FORMAT}{MAKER}{VERSION(0)}{CTX}',
    #         'parse' : parsePlaylist,
    #     },
    #     'url':{
    #         'url': lambda token: f'{BASE_URL}webapi.get&token={token}&type=playlist&p=0&{FORMAT}{MAKER}{VERSION(0)}{CTX}',
    #         'parse' : parsePlaylist,
    #         'validate' : validate.isPlaylistUrl
    #     },
    #     'parse' : parsePlaylist
    # },

    # # with `id` only lyrics is returned
    # # with `url` lyrics and song info is returned
    # 'lyrics':{
    #     'id' : {
    #         'url' : lambda id: f'{BASE_URL}lyrics.getLyrics&lyrics_id={id}{FORMAT}{MAKER}{VERSION(0)}{CTX}',
    #         'parse' : parseLyricsId,
    #     },
    #     'url':{
    #         'url': lambda token: f'{BASE_URL}webapi.get&token={token}&type=lyrics&{FORMAT}{MAKER}{VERSION(0)}{CTX}',
    #         'parse' : parseLyricsUrl,
    #         'validate' : validate.isSongUrl
    #     },
    #     'parse' : parseLyrics
    # },

# } 


