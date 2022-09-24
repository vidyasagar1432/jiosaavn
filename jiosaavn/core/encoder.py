from typing import Any, Optional, Set,Dict,Optional


from . import schemas
from .parsers import _parseSong ,_parseAlbum,_parsePlaylist,_parseLyrics,_parseSearch
from .models import Model,IncludeModel,ExcludeModel


SetIntStr = Set[int | str]
DictIntStrAny = Dict[int | str, Any]


def jsonable_encoder(
    response: dict,
    response_model: Model ,
    include: Optional[SetIntStr | DictIntStrAny] = None,
    exclude: Optional[SetIntStr | DictIntStrAny] = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    **kwargs
    ):

    obj = response_model(**response)

    if include is not None and not isinstance(include, (set, dict)):
        include = set(include)
    if exclude is not None and not isinstance(exclude, (set, dict)):
        exclude = set(exclude)
    
    return obj.dict(
        include=include,
        exclude=exclude,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,
    )

def song(
    response:dict,
    include: Optional[SetIntStr | DictIntStrAny] = None,
    exclude: Optional[SetIntStr | DictIntStrAny] = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    **kwargs
    ):
    # return _parseSong(response=response,_internal=kwargs.get('_internal'))

    return jsonable_encoder(
        response=_parseSong(response=response,**kwargs),
        response_model=schemas.Song,
        include=include,
        exclude=exclude,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,)

def album(
    response:dict,
    include_song: Optional[SetIntStr | DictIntStrAny] = None,
    exclude_song: Optional[SetIntStr | DictIntStrAny] = None,
    include: Optional[SetIntStr | DictIntStrAny] = None,
    exclude: Optional[SetIntStr | DictIntStrAny] = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    ):

    obj = _parseAlbum(
        response=response,
        include_song=include_song,
        exclude_song=exclude_song,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none
        )

    # return obj
    if not obj:
        raise Exception('pls provide valid aldumid or url')

    return jsonable_encoder(
        response=obj,
        response_model=schemas.Album,
        include=include,
        exclude=exclude,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,)

def playlist(
    response:dict,
    include_song: Optional[SetIntStr | DictIntStrAny] = None,
    exclude_song: Optional[SetIntStr | DictIntStrAny] = None,
    include: Optional[SetIntStr | DictIntStrAny] = None,
    exclude: Optional[SetIntStr | DictIntStrAny] = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    ):

    obj = _parsePlaylist(
        response=response,
        include_song=include_song,
        exclude_song=exclude_song,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none
        )

    # return obj

    return jsonable_encoder(
        response=obj,
        response_model=schemas.Playlist,
        include=include,
        exclude=exclude,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,)

def lyrics(
    response:dict,
    include: Optional[SetIntStr | DictIntStrAny] = None,
    exclude: Optional[SetIntStr | DictIntStrAny] = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    ):

    obj = _parseLyrics(response=response,)

    # return obj

    return jsonable_encoder(
        response=obj,
        response_model=schemas.Playlist,
        include=include,
        exclude=exclude,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,)

def searchSong(
    response:dict,
    include: Optional[SetIntStr | DictIntStrAny] = None,
    exclude: Optional[SetIntStr | DictIntStrAny] = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    ):

    obj = _parseSearch(
        response=response,
        include=include,
        exclude=exclude,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none)

    return obj

    # return jsonable_encoder(
    #     response=obj,
    #     response_model=schemas.Playlist,
    #     include=include,
    #     exclude=exclude,
    #     by_alias=by_alias,
    #     exclude_unset=exclude_unset,
    #     exclude_defaults=exclude_defaults,
    #     exclude_none=exclude_none,)

