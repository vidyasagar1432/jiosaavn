from typing import Optional
from pydantic import validate_arguments, Field
from pydantic.typing import Annotated

from . import __asyncrequests
from . import __baseApiUrl
from . import __asyncparse
from .__asyncrequests import getText
from .__exceptions import ValidationError,InvalidURL
from .__validation import isAlbumUrl,isSongUrl,isPlaylistUrl
from .__constants import Response
from .__helper import getSongId,getAlbumId,getPlaylistId



@validate_arguments
async def searchSong(query:str,page:Annotated[int, Field(gt=0)]=1,limit:Annotated[int, Field(gt=0,lt=30)]=10,response:str='json'):
    '''Searches for song in JioSaavn.
    
    Args:
        query (str): Sets the search query.
        page (int, optional): Sets page to the number of page. Defaults to 1.
        limit (int, optional): Sets limit to the number of results. Defaults to 10. Max to 30.
        response(str,optional): Sets the response of result. Defaults to `json`.
    
    Note:
        To get raw result Set `response` to `raw`
        
    Examples:
        Calling `searchSong` function gives the search result.
        >>> from jiosaavn.Async import searchSong
        >>> search = await searchSong('alone')
        >>> print(search)
    <https://github.com/vidyasagar1432/jiosaavn>
        '''
    if not response in Response:return {'status':'failed','message': 'response should be json or raw'}
    result = await __asyncrequests.getjSON(url=__baseApiUrl.songsearchFromSTRING(query=query,p=page,n=limit))
    if response == 'raw':return result
    return await __asyncparse.makeSearchResponse(data=result)


async def searchAlbum(query:str,response:str='json'):
    '''Searches for album in JioSaavn.
    
    Args:
        query (str): Sets the search query.
        response(str,optional): Sets the response of result. Defaults to `json`.
    
    Note:
        To get raw result Set `response` to `raw`
            
    Examples:
        Calling `searchAlbum` function gives the search result.
        >>> from jiosaavn.Async import searchAlbum
        >>> search = await searchAlbum('Alone')
        >>> print(search)
    <https://github.com/vidyasagar1432/jiosaavn>
    '''
    if not response in Response:return {'status':'failed','message': 'response should be json or raw'}
    result = await __asyncrequests.getjSON(__baseApiUrl.albumsearchFromSTRING(query=query))
    if response == 'raw':return result
    return await __asyncparse.makeAlbumSearchResponse(data=result)


async def song(url:Optional[str]=None,id:Optional[str]=None,lyrics:bool=False,response:str='json'):
    '''Get song info from JioSaavn.
    
    Args:
        url (str): Sets the url of song.
        id (str): Sets the id of song.
        lyrics (bool): Sets the lyrics whether to get lyrics. Defaults to `False`.
        response(str,optional): Sets the response of result. Defaults to `json`.
        
    Note:
        To get raw result Set `response` to `raw`
        
    Examples:
        Calling `song` function gives the search result.
        >>> from jiosaavn.Async import song
        >>> result = await song(id='veJXEDAz')
        >>> print(result)
    <https://github.com/vidyasagar1432/jiosaavn>
    '''
    if not (url or id):return {'status':'failed','message': 'Please provide a url or id of a song'}
    if not response in Response:return {'status':'failed','message': 'response should be json or raw'}
    if url:
        if not isSongUrl(url=url):return {'status':'failed','message': 'Please provide a valid jiosaavn song url'}
        id = getSongId(response= await getText(url=url,data=[('bitrate', '320')]))
        if not id:return {'status':'failed','message': f'invalid song url "{url}"'}
    result = await __asyncrequests.getjSON(url=__baseApiUrl.songFromID(id=id))
    if response == 'raw':return result
    return await __asyncparse.makeSongResponse(song=result[id],lyrics=lyrics) if result else {'status':'failed','message': f'invalid song Id "{id}"'}



async def album(url:Optional[str]=None,id:Optional[str]=None,lyrics:bool=False,response:str='json'):
    '''Get album info from JioSaavn.
    
    Args:
        url (str): Sets the url of album.
        id (str): Sets the id of album.
        lyrics (bool): Sets the lyrics whether to get lyrics. Defaults to `False`.
        response(str,optional): Sets the response of result. Defaults to `json`.
    
    Note:
        To get raw result Set `response` to `raw`
    
    Examples:
        Calling `album` function gives the search result.
        >>> from jiosaavn.Async import album
        >>> result = await album(id='10496527')
        >>> print(result)
    <https://github.com/vidyasagar1432/jiosaavn>
    '''
    if not (url or id):return {'status':'failed','message': 'Please provide a url or id of an album'}
    if not response in Response:return {'status':'failed','message': 'response should be json or raw'}
    if url:
        if not isAlbumUrl(url=url):return {'status':'failed','message': 'Please provide a valid jiosaavn album url'}
        id = getAlbumId(response= await getText(url=url))
        if not id:return {'status':'failed','message': f'invalid album url "{url}"'}
    result = await __asyncrequests.getjSON(url=__baseApiUrl.albumFromID(id=id))
    if response == 'raw':return result
    result = await __asyncparse.makeAlbumResponse(data=result,lyrics=lyrics)
    return result if result else {'status':'failed','message': f'invalid album Id "{id}"'}



async def playlist(url:Optional[str]=None,id:Optional[str]=None,lyrics:bool=False,response:str='json'):
    '''Get playlist info from JioSaavn.
    
    Args:
        url (str): Sets the url of playlist.
        id (str): Sets the id of playlist.
        lyrics (bool): Sets the lyrics whether to get lyrics. Defaults to `False`.
        response(str,optional): Sets the response of result. Defaults to `json`.
    
    Note:
        To get raw result Set `response` to `raw`
    
    Examples:
        Calling `playlist` function gives the search result.
        >>> from jiosaavn.Async import playlist
        >>> result = await playlist(url='https://www.jiosaavn.com/s/playlist/88063878238ad9a391a33c0e628d2b01/90s_Love/OykxHSA0YytFo9wdEAzFBA__')
        >>> print(result)
    <https://github.com/vidyasagar1432/jiosaavn>
    '''
    if not (url or id):return {'status':'failed','message': 'Please provide a url or id of playlist'}
    if not response in Response:return {'status':'failed','message': 'response should be json or raw'}
    if url:
        if not isPlaylistUrl(url=url):return {'status':'failed','message': 'Please provide a valid jiosaavn playlist url'}
        id = getPlaylistId(response= await getText(url=url))
        if not id:return {'status':'failed','message': f'invalid playlist url "{url}"'}
    result = await __asyncrequests.getjSON(url=__baseApiUrl.playlistFromID(id=id))
    if response == 'raw':return result
    result = await __asyncparse.makePlaylistResponse(data=result ,lyrics=lyrics)
    return result if result else {'status':'failed','message': f'invalid playlist Id "{id}"'}


async def lyrics(url:Optional[str]=None,id:Optional[str]=None,response:str='json'):
    '''Get lyrics of a song (If Available)
    
    Args:
        url (str): Sets the url of playlist.
        id (str): Sets the id of song.
        response(str,optional): Sets the response of result. Defaults to `json`.
        
    Note:
        To get raw result Set `response` to `raw`
    
    Examples:
        Calling `lyrics` function gives the search result.
        >>> from jiosaavn.Async import lyrics
        >>> result = await lyrics(id='blMuXL1P')
        >>> print(result)
    <https://github.com/vidyasagar1432/jiosaavn>
    '''
    
    if not (url or id):return {'status':'failed','message': 'Please provide a url or id of a song'}
    if not response in Response:return {'status':'failed','message': 'response should be json or raw'}
    if url:
        if not isSongUrl(url=url):return {'status':'failed','message': 'Please provide a valid jiosaavn song url'}
        id = getSongId(response= await getText(url=url,data=[('bitrate', '320')]))
        if not id:return {'status':'failed','message': f'invalid song url "{url}"'}
    result = await __asyncrequests.getjSON(url=__baseApiUrl.lyricsFromID(id=id))
    if response == 'raw':return result
    if result.get('status') == "failure":return {'status': 'no lyric'}
    return {'lyrics':result.get('lyrics'),
            'lyrics_copyright':result.get('lyrics_copyright'),
            'snippet':result.get('snippet')
            } if result else {'status':'failed','message': f'invalid song Id "{id}"'}
