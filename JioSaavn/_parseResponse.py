
from . import _fetch ,_helper


async def makeSearchResponse(data):
    result =[]
    for i in  data['results']:
        images = _helper.makeDifferentQualityImages(i['image'])
        singers = ', '.join([q['name'] for q in  i['more_info']['artistMap']['primary_artists']])
        data = {
        'id':i['id'],
        'title':i['title'],
        'image':images["150x150"],
        'images':images,
        'album':i['more_info']['album'],
        'description':f"{i['more_info']['album']} - {singers}" if singers else i['more_info']['album'],
        'has_lyrics':i['more_info']['has_lyrics'],
        'singers':singers.split(', '),
        'language':_helper.ucfirst(i['language']),
        'album_id':i['more_info']['album_id'],
        'url':{
            'song':i['perma_url'],
            'album':i['more_info']['album_url'],
            },
        } 
        result.append(data)
    return result

async def makeSongResponse(song,lyrics:bool=False):
    media_urls = _helper.makeDifferentQualityMediaUrls(song['media_preview_url'])
    images = _helper.makeDifferentQualityImages(song['image'])
    return {
    'id': song['id'],
    'song': song['song'],
    'album': song['album'],
    'year': song['year'],
    'primary_artists': (song['primary_artists']).split(', '),
    'singers': (song['singers']).split(', '),
    'image': images["500x500"],
    'images':images,
    'duration': song['duration'],
    'label': song['label'],
    'albumid': song['albumid'],
    'language': _helper.ucfirst(song['language']),
    'copyright_text': song['copyright_text'],
    'has_lyrics': song['has_lyrics'],
    'lyrics': await _fetch.lyrics(song['id']) if song['has_lyrics'] == "true" and lyrics else None,
    'media_url': media_urls["160_KBPS"],
    'media_urls':media_urls,
    'release_date': song['release_date'],
    'url':{
        'song': song['perma_url'],
        'album': song['album_url'],
        },
    }

async def makeAlbumSearchResponse(data):
    result =[]
    for i in  data['albums']['data']:
        images = _helper.makeDifferentQualityImages(i['image'])
        _data = {
            'id': i['id'],
            'title': i['title'],
            'image': images["150x150"],
            'images':images,
            'music': i['music'],
            'description': i['description'],
            'year': i['more_info']['year'],
            'language': _helper.ucfirst(i['more_info']['language']),
            'url': i['url'],
            'song':i['more_info']['song_pids'],
        }
        result.append(_data)
    return result

async def makeAlbumResponse(data):
    return {
        'albumid': data['albumid'],
        'title': data['title'],
        'name': data['name'],
        'year': data['year'],
        'primary_artists': (data['primary_artists']).split(', '),
        'image': data['image'],
        'songs':[await makeSongResponse(song=song) for song in data['songs']],
        'perma_url': data['perma_url'],
        'release_date': data['release_date'],
    }
