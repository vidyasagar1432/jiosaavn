from typing import Any, Optional, Set, Dict, Optional

from . import encoder

# from .encoder import SetIntStr,DictIntStrAny


def capitalize(string: str):
    if string:
        return string.capitalize()


def makeDifferentQualityMediaUrls(url: str):
    if url:
        replaced = url.replace("preview.saavncdn.com", "aac.saavncdn.com")
        return {
            "96_KBPS": replaced.replace("_96_p", "_96"),
            "160_KBPS": replaced.replace("_96_p", "_160"),
            "320_KBPS": replaced.replace("_96_p", "_320"),
        }


def makeDifferentQualityImages(image: str, sep: str):
    if image:
        image = image[: image.rfind(sep)]
        return {
            "50x50": f"{image}{sep}50x50.jpg",
            "150x150": f"{image}{sep}150x150.jpg",
            "500x500": f"{image}{sep}500x500.jpg",
        }


def _parseSong(response: dict, _internal: bool = False,**kwargs):
    # print('**kwargs')
    # return response
    if not _internal:
        if not response.get("songs"):
            raise Exception('pls provide valid songid or url')
        response = response["songs"][0]


    return {
        "id": response.get("id"),
        "title": response.get("song"),
        "albumId": response.get("albumid"),
        "albumTitle": response.get("album"),
        "duration": response.get("duration"),
        "playCount": response.get("play_count"),
        "year": response.get("year"),
        "releaseDate": response.get("release_date"),
        "language": capitalize(response.get("language")),
        "hasLyrics": response.get("has_lyrics"),
        "singers": response.get("singers"),
        "starring": response.get("starring"),
        "label": response.get("label"),
        "music": response.get("music"),
        "copyright": response.get("copyright_text"),
        "musicId": response.get("music_id"),
        "primaryArtists": response.get("primary_artists"),
        "primaryArtistsId": response.get("primary_artists_id"),
        "featuredArtists": response.get("featured_artists"),
        "featuredArtistsId": response.get("featured_artists_id"),
        "artistMap": response.get("artistMap"),
        "url": response.get("perma_url"),
        "albumUrl": response.get("album_url"),
        "labelUrl": f"https://www.jiosaavn.com{response.get('label_url')}"
        if response.get("label_url")
        else None,
        "imageUrls": makeDifferentQualityImages(response.get("image"), sep="-"),
        "audioUrls": makeDifferentQualityMediaUrls(response.get("media_preview_url")),
    }


def _parseAlbum(
    response: dict,
    include_song: Any = None,
    exclude_song: Any = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    ):

    if include_song is not None or exclude_song is not None:
        __parseSong = encoder.song
    else:
        __parseSong = _parseSong
    return {
            "id": response.get("albumid"),
            "title": response.get("title"),
            "name": response.get("name"),
            "year": response.get("year"),
            "url": response.get("perma_url"),
            "imageUrls": makeDifferentQualityImages(response.get("image"), sep="-"),
            "primaryArtists": response.get("primary_artists"),
            "primaryArtistsId": response.get("primary_artists_id"),
            "songs": [
                __parseSong(
                    response=song,
                    _internal=True,
                    include=include_song,
                    exclude=exclude_song,
                    by_alias=by_alias,
                    exclude_unset=exclude_unset,
                    exclude_defaults=exclude_defaults,
                    exclude_none=exclude_none,
                )
                for song in response["songs"]
            ],
        } if response.get("albumid") != '0' else None



def _parsePlaylist(
    response:dict,
    include_song: Any = None,
    exclude_song: Any = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
    ):
    if include_song is not None or exclude_song is not None:
        __parseSong = encoder.song
    else:
        __parseSong = _parseSong
    return {
        'id': response.get('listid'),
        'title': response.get('listname'),
        'listCount': response.get('list_count'),
        'followerCount': response.get('follower_count'),
        'url': response.get('perma_url'),
        'image': response.get('image'),
        'songs':[__parseSong(
                    response=song,
                    _internal=True,
                    include=include_song,
                    exclude=exclude_song,
                    by_alias=by_alias,
                    exclude_unset=exclude_unset,
                    exclude_defaults=exclude_defaults,
                    exclude_none=exclude_none,
                ) for song in response['songs']]
    } if response.get('listid') else None


def _parseLyrics(response:dict):
    _lyrics = response.get('lyrics')
    if isinstance(_lyrics, dict):
        return __parseLyricsId(_lyrics)
    return __parseLyricsId(response)

def __parseLyricsId(response:dict):
    return {'lyrics':response.get('lyrics'),
            'lyrics_copyright':response.get('lyrics_copyright'),
            'snippet':response.get('snippet')
            }


def _parseSearch(
    response:dict,
    include: Any = None,
    exclude: Any= None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,):
    return [encoder.song(
        response=song,
        include=include,
        exclude=exclude,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,
        _internal=True
        ) for song in  response.get('results')]

def _parseAlbumSearch(response:dict):
    return [{
            'id': i.get('id'),
            'title': i.get('title'),
            'music': i.get('more_info').get('music'),
            # 'type' : i.get('type'),
            'year': i.get('year'),
            'language': capitalize(i.get('language')),
            'songCount':i.get('more_info').get('song_count'),
            'albumUrl': i.get('perma_url'),
            'imageUrls':makeDifferentQualityImages(i.get('image'),sep='-'),
            'primaryArtists':i.get('more_info').get('artistMap').get('primary_artists'),
            'featuredArtists':i.get('more_info').get('artistMap').get('featured_artists'),
            'artists':i.get('more_info').get('artistMap').get('artists'),
        }for i in  response.get('results')]

def _parsePlaylistSearch(response:dict):
    return [{
            'id': i.get('listid'),
            'title': i.get('listname'),
            'type' : i.get('entity_type'),
            'language': _helper.capitalize(i.get('language')),
            'songCount':i.get('count'),
            'url': i.get('perma_url'),
            'imageUrls':makeDifferentQualityImages(i.get('image'),sep='_'),
        }for i in  response.get('results')]

def _parseArtistSearch(response:dict):
    return [{
            'id': i.get('id'),
            'name': i.get('name'),
            'role' : i.get('role'),
            'type' : i.get('type'),
            'url': i.get('perma_url'),
            'imageUrls':makeDifferentQualityImages(i.get('image'),sep='-'),
        }for i in  response.get('results')]

