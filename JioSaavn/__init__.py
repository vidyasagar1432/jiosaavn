from . import Async, Sync
from .Sync import JioSaavn,searchSong,searchAlbum,song,album,playlist,lyrics

__version__ = 'v0.1.0'
__title__ = "jiosaavn"
__description__ = "Search for JioSaavn songs & album. Get song ,album, lyric & playlist information from url or id."


__all__ =[
    'JioSaavn',
    'Async',
    'Sync',
    'searchSong',
    'searchAlbum',
    'song',
    'album',
    'lyrics',
    'playlist',
]
