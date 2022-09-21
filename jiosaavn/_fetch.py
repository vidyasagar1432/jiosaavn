from typing import Optional, Callable
from pydantic import validate_arguments, Field
from pydantic.typing import Annotated

from . import _requests, _parse, _helper, _validation

# from . import __baseApiUrl
# from . import __asyncparse
# from .__asyncrequests import getText
# from .__exceptions import ValidationError,InvalidURL
# from .__validation import isAlbumUrl,isSongUrl,isPlaylistUrl
# from .__constants import Response
# from .__helper import getSongId,getAlbumId,getPlaylistId

from enum import Enum


class Type(Enum):
    song = "song"
    album = "album"
    playlist = "playlist"
    artist = "artist"

class Search:

    def __init__(
        self,
        query: str,
        type: Type,
        page: int,
        limit: int,
        raw: bool = False):

        # self.query = query
        self.type = type.value
        # self.page = page
        # self.limit = limit
        self.raw = raw
        self.apiUrl = _requests.searchApiURL(query, self.type, page, limit)
        

    def __prase(self,response:dict):

        if not self.raw:
            return _parse.SEARCH_FUNCTION[self.type](response)
        
        return response


    async def a_get(self):

        return self.__prase(await _requests.asyncGet(self.apiUrl))

    def s_get(self):

        return self.__prase(_requests.syncGet(self.apiUrl))


class JioSaavn:

    def __init__(
        self,
        id:str,
        url:str,
        type:Type = Type.song,
        raw: bool = False):

        if not (url or id):
            raise ValidationError('Please provide a url or id')
        
        self.id = id
        self.url = url
        self.type =type.value
        self.raw = raw
   
    def __prase(self,response:dict):
        if not self.raw:
            return _parse.CORE_FUNCTION[self.type](response=response,id=self.id)
        return response

    def __getapiURL(self):
        print(_requests.coreApiURL(self.id, self.type))
        return _requests.coreApiURL(self.id, self.type)

    async def __aget(self):
        response = await _requests.asyncGet(self.__getapiURL())
        return self.__prase(response=response)

    def __sget(self):
        response = _requests.syncGet(self.__getapiURL())
        return self.__prase(response=response)
    
    async def a_get(self):

        if self.id:
            return await self.__aget()

        if self.url:
            _validation.URL_FUNCTION[self.type](self.url)

            source = await _requests.asyncGet(url=self.url,response=_requests.Response.text,params=[('bitrate', '320')])
            self.id = _parse.ID_FUNCTION[self.type](response= source)
 
            return await self.__aget()

    def s_get(self):

        if self.id:
            return self.__sget()

        if self.url:
            _validation.URL_FUNCTION[self.type](self.url)

            source = _requests.syncGet(url=self.url,response=_requests.Response.text,params=[('bitrate', '320')])
            self.id = _parse.ID_FUNCTION[self.type](response= source)

            return self.__sget()




