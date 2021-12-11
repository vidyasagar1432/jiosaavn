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
    assert response in Response,'response should be json or raw'
    result = await __asyncrequests.getjSON(url=__baseApiUrl.songsearchFromSTRING(query=query,p=page,n=limit))
    if response == 'raw':
        return result
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
    assert response in Response,'response should be json or raw'
    result = await __asyncrequests.getjSON(__baseApiUrl.albumsearchFromSTRING(query=query))
    if response == 'raw':
        return result
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
    if not (url or id):
        raise ValidationError('Please provide a url or id of a song')
    if url:
        if not isSongUrl(url=url):
            raise InvalidURL('Please provide a valid jiosaavn song url')
        id = getSongId(response= await getText(url=url,data=[('bitrate', '320')]))
    assert response in Response,'response should be json or raw'
    result = await __asyncrequests.getjSON(url=__baseApiUrl.songFromID(id=id))
    if response == 'raw':
        return result
    return await __asyncparse.makeSongResponse(song=result[id],lyrics=lyrics)


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
    if not (url or id):
        raise ValidationError('Please provide a url or id of an album')
    if url:
        if not isAlbumUrl(url=url):
            raise InvalidURL('Please provide a valid jiosaavn album url')
        id = getAlbumId(await getText(url=url))
    assert response in Response,'response should be json or raw'
    result = await __asyncrequests.getjSON(__baseApiUrl.albumFromID(id=id))
    if response == 'raw':
        return result
    return await __asyncparse.makeAlbumResponse(data=result,lyrics=lyrics)


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
    if not (url or id):
        raise ValidationError('Please provide a url or id of playlist')
    if url:
        if not isPlaylistUrl(url=url):
            raise InvalidURL('Please provide a valid jiosaavn playlist url')
        id = getPlaylistId(await getText(url=url))
    assert response in Response,'response should be json or raw'
    result = await __asyncrequests.getjSON(url=__baseApiUrl.playlistFromID(id=id))
    if response == 'raw':
        return result
    return await __asyncparse.makePlaylistResponse(data=result ,lyrics=lyrics)


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
    if not (url or id):
        raise ValidationError('Please provide a url or id of a song')
    if url:
        if not isSongUrl(url=url):
            raise InvalidURL('Please provide a valid jiosaavn song url')
        id = getSongId(response= await getText(url=url,data=[('bitrate', '320')]))
    assert response in Response,'response should be json or raw'
    result = await __asyncrequests.getjSON(__baseApiUrl.lyricsFromID(id=id))
    if response == 'raw':
        return result
    if result.get('status' ) == "failure":
        return {'status': f'no lyric'}
    return {'lyrics':result.get('lyrics'),
            'lyrics_copyright':result.get('lyrics_copyright'),
            'snippet':result.get('snippet')
            }