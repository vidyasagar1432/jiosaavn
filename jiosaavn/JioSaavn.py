

import asyncio
from operator import itemgetter
import json
import httpx
import typing
import random
from pydantic import create_model
from httpx._types import QueryParamTypes,HeaderTypes,URLTypes,ProxiesTypes

from core import encoder

from enum import Enum

class Type(Enum):
    getSong = 'getSong'
    getAlbum = 'getAlbum'
    getPlaylist = 'getPlaylist'
    getArtist = 'getArtist'
    getLyrics ='getLyrics'

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

BASE_URL = "https://www.jiosaavn.com/api.php"

defaultParams = {
            'ctx':'wap6dot0',
            '_format':'json',
            '_marker':'0',
            'api_version':'0',
            'includeMetaTags':'0'
        }

def checkUrlOrId(id:str,url:str):
    if not (url or id):
        raise exceptions.ValidationError('Please provide a url or id')

def getTokenFromUrl(url:str):
    '''Return `token` for url'''
    return url[url.rindex('/')+1:]



infoApi = {
        "getSong": {
            'id':{
                'params': lambda id : {
                    '__call':'song.getDetails',
                    'pids':id
                },
                # 'parse' : _parseSong,
            },
            'url':{
                'params': lambda token :{
                    '__call':'webapi.get',
                    'token':token
                },
                # 'parse' : _parseSong,
            },
            'parse' : encoder.song,
        },
        "getAlbum": {
            'id':{
                'params': lambda id : {
                    '__call':'content.getAlbumDetails',
                    'albumid':id
                },
                # 'parse' : _parseSong,
            },
            'url':{
                'params': lambda token :{
                    '__call':'webapi.get',
                    'token':token
                },
                # 'parse' : _parseSong,
            },
            'parse' : encoder.album,
        }
    }
 


# 29060166
class Async:

    def __init__(
        self,
        session:bool=True,
        headers: typing.Optional[HeaderTypes]=getHeaders(),
        http2:bool=False,
        proxies:ProxiesTypes=None,
        ): 
        self.headers = headers

        if session:
            self.session = httpx.AsyncClient(
                http2=http2,
                headers=headers,
                proxies=proxies
                )
        else:
            self.session = None

    async def get(
        self,
        type:Type,
        id:str=None,
        url:str=None,
        raw: bool = False,
        params:typing.Optional[QueryParamTypes]=defaultParams,
    ):
        checkUrlOrId(id,url)

        if id:
            _params = infoApi[type]['id']['params'](id)
        elif url:
            _params = infoApi[type]['url']['params'](getTokenFromUrl(url))
        
        _params.update(params)

        if self.session:
            _response = await self.session.get(url=BASE_URL,params=_params)
        else: 
            async with httpx.AsyncClient() as client:
                _response = await client.get(url=BASE_URL,params=_params,headers=self.headers)
        
        if _response.status_code == 200:
            response = _response.json()
            return response if raw else infoApi[type]['parse'](response)
        
    def close_session(self):
        if self.session:
            self.session.aclose()



class Sync:

    def __init__(
        self,
        session:bool=True,
        headers: typing.Optional[HeaderTypes]=getHeaders(),
        http2:bool=False,
        proxies:ProxiesTypes=None,
        ): 
        self.headers = headers

        if session:
            self.session = httpx.Client(
                http2=http2,
                headers=headers,
                proxies=proxies
                )
        else:
            self.session = None

    def get(
        self,
        type:Type,
        id:str=None,
        url:str=None,
        include: encoder.SetIntStr | encoder.DictIntStrAny = None,
        exclude: encoder.SetIntStr | encoder.DictIntStrAny = None,
        raw: bool = False,
        params:typing.Optional[QueryParamTypes]=defaultParams,
        **kwargs
    ):
        ''' extra kwargs for album :
                include_song : SetIntStr | DictIntStrAny
                exclude_song : SetIntStr | DictIntStrAny
        '''
        checkUrlOrId(id,url)

        if id:
            _params = infoApi[type.value]['id']['params'](id)
        elif url:
            _params = infoApi[type.value]['url']['params'](getTokenFromUrl(url))
        
        _params.update(params)

        if self.session:
            _response = self.session.get(url=BASE_URL,params=_params)
        else: 
            with httpx.Client() as client:
                _response = Client.get(url=BASE_URL,params=_params,headers=self.headers)
        
        if _response.status_code == 200:
            try:
                response = _response.json()
            except json.JSONDecodeError as e:
                raise Exception('pls provide valid id or url')
            return response if raw else infoApi[type.value]['parse'](
                response,
                include=include,
                exclude=exclude,
                **kwargs
                )
        
    def close_session(self):
        if self.session:
            self.session.aclose()

jiosaavn = Sync()

# 29060166
# mPTrDSun
# https://www.jiosaavn.com/s/playlist/88063878238ad9a391a33c0e628d2b01/90s_Love/OykxHSA0YytFo9wdEAzFBA__
response = jiosaavn.get(type=Type.getSong, id='mPTrDSun')

print(response)