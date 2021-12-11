
from typing import Optional
from . import _asyncFetch

class JioSaavn:
    '''
    ### Create an instance of JioSaavn with async methods.
    '''
    @staticmethod
    async def searchSong(query:str,page:int=1,limit:int=10,response:str='json'):
        '''Searches for song in JioSaavn.
        
        Args:
            query (str): Sets the search query.
            page (int, optional): Sets page to the number of page. Defaults to 1.
            limit (int, optional): Sets limit to the number of results. Defaults to 10. Max to 30.
            response(str,optional): Sets the response of result. Defaults to `json`.
        
        Note:
            To get raw result Set `response` to `raw`
        
        Example:
            Calling `searchSong` method gives the search result.
            >>> from jiosaavn.Async import JioSaavn
            >>> search = await JioSaavn.searchSong('alone')
            >>> print(search)
        <https://github.com/vidyasagar1432/jiosaavn>
        '''
        return await _asyncFetch.searchSong(query=query,page=page,limit=limit,response=response)

    @staticmethod
    async def searchAlbum(query:str,response:str='json'):
        '''Searches for album in JioSaavn.
        
        Args:
            query (str): Sets the search query.
            response(str,optional): Sets the response of result. Defaults to `json`.
        
        Note:
            To get raw result Set `response` to `raw`
                
        Examples:
            Calling `searchAlbum` method gives the search result of albums.
            >>> from jiosaavn.Async import JioSaavn
            >>> search = await JioSaavn.searchAlbum('Alone')
            >>> print(search)
        <https://github.com/vidyasagar1432/jiosaavn>
        '''
        return await _asyncFetch.searchAlbum(query=query,response=response)

    @staticmethod
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
            Calling `song` method gives the song info.
            >>> from jiosaavn.Async import JioSaavn
            >>> result = await JioSaavn.song(id='veJXEDAz')
            >>> print(result)
        <https://github.com/vidyasagar1432/jiosaavn>
        '''
        return await _asyncFetch.song(url=url,id=id,lyrics=lyrics,response=response)

    @staticmethod
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
            Calling `album` method gives the album info.
            >>> from jiosaavn.Async import JioSaavn
            >>> result = await JioSaavn.album(id='10496527')
            >>> print(result)
        <https://github.com/vidyasagar1432/jiosaavn>
        '''
        return await _asyncFetch.album(url=url,id=id,lyrics=lyrics,response=response)
    
    @staticmethod
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
            Calling `playlist` method gives the playlist info.
            >>> from jiosaavn.Async import JioSaavn
            >>> result = await JioSaavn.playlist(url='https://www.jiosaavn.com/s/playlist/88063878238ad9a391a33c0e628d2b01/90s_Love/OykxHSA0YytFo9wdEAzFBA__')
            >>> print(result)
        <https://github.com/vidyasagar1432/jiosaavn>
        '''
        return await _asyncFetch.playlist(url=url,id=id,lyrics=lyrics,response=response)
    
    @staticmethod
    async def lyrics(url:Optional[str]=None,id:Optional[str]=None,response:str='json'):
        '''Get lyrics of a song (If Available)
        
        Args:
            url (str): Sets the url of playlist.
            id (str): Sets the id of song.
            response(str,optional): Sets the response of result. Defaults to `json`.
            
        Note:
            To get raw result Set `response` to `raw`
        
        Examples:
            Calling `lyrics` method gives the lyrics of song.
            >>> from jiosaavn.Async import JioSaavn
            >>> result = await JioSaavn.lyrics(id='blMuXL1P')
            >>> print(result)
        <https://github.com/vidyasagar1432/jiosaavn>
        '''
        return await _asyncFetch.lyrics(url=url,id=id,response=response)

