
from . import _syncFetch
from ._commonparse import (_makeSongResponse,
                            _makeAlbumResponse,
                            _makeAlbumSearchResponse,
                            _makePlaylistResponse,
                            _makeSearchResponse,
                            )

def makeSongResponse(song,lyrics:bool=False) -> dict:
    result = _makeSongResponse(song)
    result.update({'lyrics': _syncFetch.lyrics(id=song.get('id')) if song.get('has_lyrics') == "true" and lyrics else None})
    return result

def makeSearchResponse(data) -> dict:
    return _makeSearchResponse(data)


def makeAlbumSearchResponse(data) -> dict:
    return _makeAlbumSearchResponse(data)

def makeAlbumResponse(data,lyrics:bool=False):
    result = _makeAlbumResponse(data)
    if result:
        result.update({'songs':[makeSongResponse(song=song,lyrics=lyrics) for song in data['songs']],})
        return result

def makePlaylistResponse(data,lyrics:bool=False) -> dict:
    result = _makePlaylistResponse(data)
    if result:
        result.update({
            'songs':[makeSongResponse(song=song,lyrics=lyrics) for song in data['songs']],
        })
        return result