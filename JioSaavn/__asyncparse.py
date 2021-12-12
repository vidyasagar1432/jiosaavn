
from . import _asyncFetch
from ._commonparse import (_makeSongResponse,
                            _makeAlbumResponse,
                            _makeAlbumSearchResponse,
                            _makePlaylistResponse,
                            _makeSearchResponse,
                            )

async def makeSongResponse(song,lyrics:bool=False) -> dict:
    result = _makeSongResponse(song)
    result.update({
        'lyrics':await _asyncFetch.lyrics(id=song.get('id')) if song.get('has_lyrics') == "true" and lyrics else None
    })
    return result

async def makeSearchResponse(data) -> dict:
    return _makeSearchResponse(data)


async def makeAlbumSearchResponse(data) -> dict:
    return _makeAlbumSearchResponse(data)

async def makeAlbumResponse(data,lyrics:bool=False) -> dict:
    result = _makeAlbumResponse(data)
    if result:
        result.update({'songs':[await makeSongResponse(song=song,lyrics=lyrics) for song in data['songs']],})
        return result


async def makePlaylistResponse(data,lyrics:bool=False) -> dict:
    result = _makePlaylistResponse(data)
    if result:
        result.update({
            'songs':[await makeSongResponse(song=song,lyrics=lyrics) for song in data['songs']],
        })
        return result