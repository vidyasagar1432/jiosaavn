
from typing import Optional, Callable
from pydantic import validate_arguments, Field
from pydantic.typing import Annotated

from . import _fetch
from ._fetch import Type

class JioSaavn:

    '''
    ### Create an instance of JioSaavn with async methods.
    '''
    @validate_arguments
    @staticmethod
    async def search(
        query: str,
        type: Type = Type.song,
        page: Annotated[int, Field(gt=0)] = 1,
        limit: Annotated[int, Field(gt=0, lt=30)] = 10,
        raw: bool = False,):
        '''Searches for [song, album, playlist, artist] in JioSaavn.
        
        Args:
            query (str): Sets the search query.
            type (Type,optional): Sets the search type.
            page (int, optional): Sets page to the number of page. Defaults to 1.
            limit (int, optional): Sets limit to the number of results. Defaults to 10. Max to 30.
            raw(bool,optional): Sets the response of result. Defaults to `False`.
        
        Note:
            To get raw response Set `raw` to `True`
        
        Example:
            Calling `searchSong` method gives the search result.
            >>> from jiosaavn.Async import JioSaavn
            >>> search = await JioSaavn.search(query = 'alone', type = Type.song, page = 1, limit = 5)
            >>> print(search)
        <https://github.com/vidyasagar1432/jiosaavn>
        '''
        search = _fetch.Search(query=query,type=type,page=page,limit=limit,raw=raw)
        return await search.a_get()

