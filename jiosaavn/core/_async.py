from typing import Any, Optional, Set,Dict,Optional

from . import encoder ,validate, parsers ,exceptions ,fetch
from .encoder import SetIntStr,DictIntStrAny 

BASE_URL = "https://www.jiosaavn.com/api.php?__call="
CTX = "&ctx=wap6dot0"
META_TAGS = "&includeMetaTags=0"
FORMAT = "&_format=json"
MAKER = "&_marker=0"
VERSION = lambda num: f"&api_version={num}"

def checkUrlOrId(id:str,url:str):
    if not (url or id):
        raise exceptions.ValidationError('Please provide a url or id')

def getToken(url:str):
    return url[url.rindex('/')+1:]


async def song(
    id:str=None,
    url:str=None,
    include: Optional[SetIntStr | DictIntStrAny] = None,
    exclude: Optional[SetIntStr | DictIntStrAny] = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    raw: bool = False,
    ):

    checkUrlOrId(id=id,url=url)

    if id:
        response = await fetch.asyncGet(url = f'{BASE_URL}song.getDetails&pids={id}{FORMAT}{MAKER}{VERSION(0)}{CTX}')
    elif url:
        validate.isSongUrl(url)
        response = await fetch.asyncGet(url = f'{BASE_URL}webapi.get&token={getToken(url)}&type=song{FORMAT}{MAKER}{VERSION(0)}{CTX}')
    
    return response if raw else encoder.song(
        response=response,
        include=include,
        exclude=exclude,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,
        )

async def album(
    id:str=None,
    url:str=None,
    include: Optional[SetIntStr | DictIntStrAny] = None,
    exclude: Optional[SetIntStr | DictIntStrAny] = None,
    include_song: Optional[SetIntStr | DictIntStrAny] = None,
    exclude_song: Optional[SetIntStr | DictIntStrAny] = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    raw: bool = False,
    ):

    checkUrlOrId(id=id,url=url)

    if id:
        response = await fetch.asyncGet(url = f'{BASE_URL}content.getAlbumDetails&albumid={id}{FORMAT}{MAKER}{VERSION(0)}{CTX}')
    elif url:
        validate.isAlbumUrl(url)
        response = await fetch.asyncGet(url = f'{BASE_URL}webapi.get&token={getToken(url)}&type=album{FORMAT}{MAKER}{VERSION(0)}{CTX}')
    
    return response if raw else encoder.album(
        response=response,
        include=include,
        exclude=exclude,
        include_song=include_song,
        exclude_song=exclude_song,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,
        )

async def playlist(
    id:str=None,
    url:str=None,
    include: Optional[SetIntStr | DictIntStrAny] = None,
    exclude: Optional[SetIntStr | DictIntStrAny] = None,
    include_song: Optional[SetIntStr | DictIntStrAny] = None,
    exclude_song: Optional[SetIntStr | DictIntStrAny] = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    raw: bool = False,
    ):

    checkUrlOrId(id=id,url=url)

    if id:
        response = await fetch.asyncGet(url = f'{BASE_URL}playlist.getDetails&listid={id}{FORMAT}{MAKER}{VERSION(0)}{CTX}')
    elif url:
        validate.isPlaylistUrl(url)
        response = await fetch.asyncGet(url = f'{BASE_URL}webapi.get&token={getToken(url)}&type=playlist{FORMAT}{MAKER}{VERSION(0)}{CTX}')
    
    return response if raw else encoder.playlist(
        response=response,
        include=include,
        exclude=exclude,
        include_song=include_song,
        exclude_song=exclude_song,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,
        )
    
async def lyrics(
    id:str=None,
    url:str=None,
    include: Optional[SetIntStr | DictIntStrAny] = None,
    exclude: Optional[SetIntStr | DictIntStrAny] = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    raw: bool = False,
    ):

    checkUrlOrId(id=id,url=url)

    if id:
        response = await fetch.asyncGet(url = f'{BASE_URL}lyrics.getLyrics&lyrics_id={id}{FORMAT}{MAKER}{VERSION(0)}{CTX}')
    elif url:
        validate.isSongUrl(url)
        response = await fetch.asyncGet(url = f'{BASE_URL}webapi.get&token={getToken(url)}&type=lyrics{FORMAT}{MAKER}{VERSION(0)}{CTX}')
    
    return response if raw else encoder.lyrics(
        response=response,
        include=include,
        exclude=exclude,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,
        )

async def searchSong(
    type:str,
    query:str,
    page:int=0,
    limit:int=10,
    include: Optional[SetIntStr | DictIntStrAny] = None,
    exclude: Optional[SetIntStr | DictIntStrAny] = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    raw: bool = False,
    ):

    response = await fetch.asyncGet(url = f'{BASE_URL}search.getResults&p={page}&n={limit}&q={"+".join(query.split(" "))}{FORMAT}{MAKER}{VERSION(0)}{CTX}')

    return response if raw else encoder.searchSong(
        response=response,
        include=include,
        exclude=exclude,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,
        )

# async def searchAlbum(
#     id:str=None,
#     url:str=None,
#     include: Optional[SetIntStr | DictIntStrAny] = None,
#     exclude: Optional[SetIntStr | DictIntStrAny] = None,
#     include_song: Optional[SetIntStr | DictIntStrAny] = None,
#     exclude_song: Optional[SetIntStr | DictIntStrAny] = None,
#     by_alias: bool = True,
#     exclude_unset: bool = False,
#     exclude_defaults: bool = False,
#     exclude_none: bool = False,
#     raw: bool = False,
#     ):

#     checkUrlOrId(id=id,url=url)

#     if id:
#         response = await fetch.asyncGet(url = f'{BASE_URL}content.getAlbumDetails&albumid={id}{FORMAT}{MAKER}{VERSION(0)}{CTX}')
#     elif url:
#         validate.isAlbumUrl(url)
#         response = await fetch.asyncGet(url = f'{BASE_URL}webapi.get&token={getToken(url)}&type=album{FORMAT}{MAKER}{VERSION(0)}{CTX}')
    
#     return response if raw else encoder.album(
#         response=response,
#         include=include,
#         exclude=exclude,
#         include_song=include_song,
#         exclude_song=exclude_song,
#         by_alias=by_alias,
#         exclude_unset=exclude_unset,
#         exclude_defaults=exclude_defaults,
#         exclude_none=exclude_none,
#         )

# async def searchPlaylist(
#     id:str=None,
#     url:str=None,
#     include: Optional[SetIntStr | DictIntStrAny] = None,
#     exclude: Optional[SetIntStr | DictIntStrAny] = None,
#     include_song: Optional[SetIntStr | DictIntStrAny] = None,
#     exclude_song: Optional[SetIntStr | DictIntStrAny] = None,
#     by_alias: bool = True,
#     exclude_unset: bool = False,
#     exclude_defaults: bool = False,
#     exclude_none: bool = False,
#     raw: bool = False,
#     ):

#     checkUrlOrId(id=id,url=url)

#     if id:
#         response = await fetch.asyncGet(url = f'{BASE_URL}playlist.getDetails&listid={id}{FORMAT}{MAKER}{VERSION(0)}{CTX}')
#     elif url:
#         validate.isPlaylistUrl(url)
#         response = await fetch.asyncGet(url = f'{BASE_URL}webapi.get&token={getToken(url)}&type=playlist{FORMAT}{MAKER}{VERSION(0)}{CTX}')
    
#     return response if raw else encoder.playlist(
#         response=response,
#         include=include,
#         exclude=exclude,
#         include_song=include_song,
#         exclude_song=exclude_song,
#         by_alias=by_alias,
#         exclude_unset=exclude_unset,
#         exclude_defaults=exclude_defaults,
#         exclude_none=exclude_none,
#         )
    
# async def searchArtist(
#     id:str=None,
#     url:str=None,
#     include: Optional[SetIntStr | DictIntStrAny] = None,
#     exclude: Optional[SetIntStr | DictIntStrAny] = None,
#     by_alias: bool = True,
#     exclude_unset: bool = False,
#     exclude_defaults: bool = False,
#     exclude_none: bool = False,
#     raw: bool = False,
#     ):

#     checkUrlOrId(id=id,url=url)

#     if id:
#         response = await fetch.asyncGet(url = f'{BASE_URL}lyrics.getLyrics&lyrics_id={id}{FORMAT}{MAKER}{VERSION(0)}{CTX}')
#     elif url:
#         validate.isSongUrl(url)
#         response = await fetch.asyncGet(url = f'{BASE_URL}webapi.get&token={getToken(url)}&type=lyrics{FORMAT}{MAKER}{VERSION(0)}{CTX}')
    
#     return response if raw else encoder.lyrics(
#         response=response,
#         include=include,
#         exclude=exclude,
#         by_alias=by_alias,
#         exclude_unset=exclude_unset,
#         exclude_defaults=exclude_defaults,
#         exclude_none=exclude_none,
#         )

