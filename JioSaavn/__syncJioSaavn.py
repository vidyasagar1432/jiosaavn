
from typing import Optional
from . import _syncFetch

class JioSaavn:
    '''
    ### Create an instance of JioSaavn with sync methods.
    '''
    @staticmethod
    def searchSong(query:str,page:int=1,limit:int=10,response:str='json'):
        '''Searches for song in JioSaavn.
        
        Args:
            query (str): Sets the search query.
            page (int, optional): Sets page to the number of page. Defaults to 1.
            limit (int, optional): Sets limit to the number of results. Defaults to 10. Max to 30.
            response(str,optional): Sets the response of result. Defaults to `json`.
        
        Note:
            To get raw result Set `response` to `raw`
        
        Example:
            Calling `searchSong` method gives the search result of songs.
            >>> from jiosaavn.Sync import jioSaavn
            >>> search = jioSaavn.searchSong('alone')
            >>> print(search)
        <https://github.com/vidyasagar1432/jiosaavn>
        '''
        return _syncFetch.searchSong(query=query,page=page,limit=limit,response=response)

    @staticmethod
    def searchAlbum(query:str,response:str='json'):
        '''Searches for album in JioSaavn.
        
        Args:
            query (str): Sets the search query.
            response(str,optional): Sets the response of result. Defaults to `json`.
        
        Note:
            To get raw result Set `response` to `raw`
                
        Examples:
            Calling `searchAlbum` method gives the search result of albums.
            >>> from jiosaavn.Sync import jioSaavn
            >>> search = jioSaavn.searchAlbum('Alone')
            >>> print(search)
        <https://github.com/vidyasagar1432/jiosaavn>
        '''
        return _syncFetch.searchAlbum(query=query,response=response)

    @staticmethod
    def song(url:Optional[str]=None,id:Optional[str]=None,lyrics:bool=False,response:str='json'):
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
            >>> from jiosaavn.Sync import jioSaavn
            >>> result = jioSaavn.song(id='veJXEDAz')
            >>> print(result)
        <https://github.com/vidyasagar1432/jiosaavn>
        '''
        return _syncFetch.song(url=url,id=id,lyrics=lyrics,response=response)

    @staticmethod
    def album(url:Optional[str]=None,id:Optional[str]=None,lyrics:bool=False,response:str='json'):
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
            >>> from jiosaavn.Sync import jioSaavn
            >>> result = jioSaavn.album(id='10496527')
            >>> print(result)
        <https://github.com/vidyasagar1432/jiosaavn>
        '''
        return _syncFetch.album(url=url,id=id,lyrics=lyrics,response=response)
    
    @staticmethod
    def playlist(url:Optional[str]=None,id:Optional[str]=None,lyrics:bool=False,response:str='json'):
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
            >>> from jiosaavn.Sync import jioSaavn
            >>> result = jioSaavn.playlist(url='https://www.jiosaavn.com/s/playlist/88063878238ad9a391a33c0e628d2b01/90s_Love/OykxHSA0YytFo9wdEAzFBA__')
            >>> print(result)
        <https://github.com/vidyasagar1432/jiosaavn>
        '''
        return _syncFetch.playlist(url=url,id=id,lyrics=lyrics,response=response)
    
    @staticmethod
    def lyrics(url:Optional[str]=None,id:Optional[str]=None,response:str='json'):
        '''Get lyrics of a song (If Available)
        
        Args:
            url (str): Sets the url of playlist.
            id (str): Sets the id of song.
            response(str,optional): Sets the response of result. Defaults to `json`.
            
        Note:
            To get raw result Set `response` to `raw`
        
        Examples:
            Calling `lyrics` method gives the lyrics of song.
            >>> from jiosaavn.Sync import jioSaavn
            >>> result = jioSaavn.lyrics(id='blMuXL1P')
            >>> print(result)
        <https://github.com/vidyasagar1432/jiosaavn>
        '''
        return _syncFetch.lyrics(url=url,id=id,response=response)

