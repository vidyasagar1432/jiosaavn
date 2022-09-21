
from . import _helper, _exceptions

def song(response:dict,id:str=None):
    if id:
        response = response.get(id)
    return {
    'id': response.get('id'),
    'title':response.get('song'),
    'album' : {
            'id':response.get('albumid'),
            'title':response.get('album'),
            'url':response.get('album_url'),
        },
    'playCount': response.get('play_count'),
    'duration': response.get('duration'),
    # 'primaryArtists': [{'artist':artist,'id':id} for artist,id in zip((song['primary_artists']).split(', '),(song['primary_artists_id']).split(', '))],
    # 'featuredArtists': [{'artist':artist,'id':id} for artist,id in zip((song['featured_artists']).split(', '),(song['featured_artists_id']).split(', '))],
    'singers': response.get('singers'),
    # 'artistMap':response.get('artistMap'),
    'language': _helper.capitalize(response.get('language')),
    'hasLyrics' : response.get('has_lyrics'),
    'releaseDate': response.get('release_date'),
    'url': response.get('perma_url'),
    'imagesUrls': _helper.makeDifferentQualityImages(response.get('image'),sep='-'),
    'audioUrls':_helper.makeDifferentQualityMediaUrls(response.get('media_preview_url')),
    'primaryArtists': response.get('primary_artists'),
    'primaryArtistsId':response.get('primary_artists_id'),
    'featuredArtists': response.get('featured_artists'),
    'featuredArtistsId':response.get('featured_artists_id'),
    # 'label': response.get('label'),
    # 'labelUrl':f"https://www.jiosaavn.com{response.get('label_url')}" if response.get('label_url') else None,
    }

def album(response:dict,id:str=None):
    return {
        'id': response.get('albumid'),
        'title': response.get('title'),
        'name': response.get('name'),
        'year': response.get('year'),
        'primaryArtists': response.get('primary_artists'),
        'primaryArtistsId': response.get('primary_artists_id'),
        'albumUrl': response.get('perma_url'),
        'imageUrls': _helper.makeDifferentQualityImages(response.get('image'),sep='-'),
        'songs':[song(i) for i in response['songs']]
    } if response.get('albumid') != '0' else None

def playlist(response:dict,id:str=None):
    return {
        'id': response.get('listid'),
        'title': response.get('listname'),
        'username': response.get('username'),
        'listCount': response.get('list_count'),
        'followerCount': response.get('follower_count'),
        'url': response.get('perma_url'),
        'image': response.get('image'),
        'songs':[song(i) for i in response['songs']]
    } if response.get('listid') else None



def search(response:dict):
    return [{
        'id':i.get('id'),
        'title':i.get('title'),
        'description':i.get('header_desc'),
        'type' : i.get('type'),
        'language':_helper.capitalize(i.get('language')),
        'hasLyrics':i.get('more_info').get('has_lyrics'),
        'playCount': i.get('play_count'),
        'url':i.get('perma_url'),
        'imagesUrls':_helper.makeDifferentQualityImages(i.get('image'),sep='-'),
        'album' : {
            'id':i.get('more_info').get('album_id'),
            'title':i.get('more_info').get('album'),
            'url':i.get('more_info').get('album_url'),
        },
        'primaryArtists':i.get('more_info').get('artistMap').get('primary_artists'),
        'featuredArtists':i.get('more_info').get('artistMap').get('featured_artists'),
        'artists':i.get('more_info').get('artistMap').get('artists'),
        } for i in  response.get('results')]

def albumSearch(response:dict):
    return [{
            'id': i.get('id'),
            'title': i.get('title'),
            'music': i.get('more_info').get('music'),
            'type' : i.get('type'),
            'year': i.get('year'),
            'language': _helper.capitalize(i.get('language')),
            'songCount':i.get('more_info').get('song_count'),
            'albumUrl': i.get('perma_url'),
            'imageUrls':_helper.makeDifferentQualityImages(i.get('image'),sep='-'),
            'primaryArtists':i.get('more_info').get('artistMap').get('primary_artists'),
            'featuredArtists':i.get('more_info').get('artistMap').get('featured_artists'),
            'artists':i.get('more_info').get('artistMap').get('artists'),
        }for i in  response.get('results')]

def playlistSearch(response:dict):
    return [{
            'id': i.get('id'),
            'title': i.get('title'),
            'type' : i.get('type'),
            'language': _helper.capitalize(i.get('more_info').get('language')),
            'songCount':i.get('more_info').get('song_count'),
            'url': i.get('perma_url'),
            'imageUrls':_helper.makeDifferentQualityImages(i.get('image'),sep='_'),
        }for i in  response.get('results')]

def artistSearch(response:dict):
    return [{
            'id': i.get('id'),
            'name': i.get('name'),
            'role' : i.get('role'),
            'type' : i.get('type'),
            'url': i.get('perma_url'),
            'imageUrls':_helper.makeDifferentQualityImages(i.get('image'),sep='-'),
        }for i in  response.get('results')]



def songId(response:str):
    try:
        try:
            # (response.split('"pid":"'))[1].split('","song_id":"')[0 to 3].split('","')[0]
            return (response.split('"pid":"'))[1].split('","song_id":"')[1].split('","')[0]
        except IndexError:

            return (response.split('"pid":"'))[1].split('","')[0]
    except Exception as e:
        raise _exceptions.InvalidURL(e)

def albumId(response:str):
    try:
        try:
            return response.split('"album_id":"')[1].split('"')[0]
        except IndexError:
            return response.split('"page_id","')[1].split('","')[0]
    except Exception as e:
        raise _exceptions.InvalidURL(e)

def playlistId(response:str):
    try:
        try:
            return response.split('"type":"playlist","id":"')[1].split('"')[0]
        except IndexError:
            return response.split('"page_id","')[1].split('","')[0]
    except Exception as e:
        raise _exceptions.InvalidURL(e)


CORE_FUNCTION = { 
    'song' : song,
    'album' : album,
    'playlist' : playlist,
    # 'artist' : _artistSearchResponse,
    }

SEARCH_FUNCTION = { 
    'song' : search,
    'album' : albumSearch,
    'playlist' : playlistSearch,
    'artist' : artistSearch,
    }

ID_FUNCTION = { 
    'song' : songId,
    'album' : albumId,
    'playlist' : playlistId,
    # 'artist' : _artistSearchResponse,
    }

