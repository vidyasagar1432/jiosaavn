
from . import __helper
from . import _asyncFetch

async def makeSongResponse(song,lyrics:bool=False):
    return {
    'id': song['id'],
    'songName':song['song'],
    'albumName':song['album'],
    'albumId': song['albumid'],
    'playCount': song['play_count'],
    'duration': song['duration'],
    'label': song['label'],
    'primaryArtists': song['primary_artists'],
    'primaryArtistsId':song['primary_artists_id'],
    'featuredArtists': song['featured_artists'],
    'featuredArtistsId':song['featured_artists_id'],
    # 'primaryArtists': [{'artist':artist,'id':id} for artist,id in zip((song['primary_artists']).split(', '),(song['primary_artists_id']).split(', '))],
    # 'featuredArtists': [{'artist':artist,'id':id} for artist,id in zip((song['featured_artists']).split(', '),(song['featured_artists_id']).split(', '))],
    'singers': song['singers'],
    'starring':song['starring'],
    'language': __helper.ucfirst(song['language']),
    'copyright': song['copyright_text'],
    'hasLyrics' : song['has_lyrics'],
    'lyrics': await _asyncFetch.lyrics(song['id']) if song['has_lyrics'] == "true" and lyrics else None,
    'releaseDate': song['release_date'],
    'songUrl':song['perma_url'],
    'albumUrl': song['album_url'],
    'imagesUrls': __helper.makeDifferentQualityImages(song['image']),
    'audioUrls':__helper.makeDifferentQualityMediaUrls(song['media_preview_url']),
    'labelUrl':f"https://www.jiosaavn.com{song['label_url']}",
    }


async def makeSearchResponse(data):
    return [{
        'id':i['id'],
        'songName':i['title'],
        'albumId':i['more_info']['album_id'],
        'albumName':i['more_info']['album'],
        'playCount': i['play_count'],
        'imagesUrls':__helper.makeDifferentQualityImages(i['image']),
        'primaryArtists':i['more_info']['artistMap']['primary_artists'],
        'featuredArtists':i['more_info']['artistMap']['featured_artists'],
        'artists':i['more_info']['artistMap']['artists'],
        'description':i['header_desc'],
        'hasLyrics':i['more_info']['has_lyrics'],
        'language':__helper.ucfirst(i['language']),
        'songUrl':i['perma_url'],
        'albumUrl':i['more_info']['album_url'],
        } for i in  data['results']]



async def makeAlbumSearchResponse(data):
    return [{
            'id': i['id'],
            'albumName': i['title'],
            'music': i['music'],
            'description': i['description'],
            'year': i['more_info']['year'],
            'language': __helper.ucfirst(i['more_info']['language']),
            'songIds':i['more_info']['song_pids'],
            'albumUrl': i['url'],
            'imagesUrls':__helper.makeDifferentQualityImages(i['image']),
        }for i in  data['albums']['data']]

async def makeAlbumResponse(data,lyrics:bool=False):
    return {
        'albumId': data['albumid'],
        'title': data['title'],
        'name': data['name'],
        'year': data['year'],
        'primaryArtists': (data['primary_artists']).split(', '),
        'image': data['image'],
        'songs':[await makeSongResponse(song=song,lyrics=lyrics) for song in data['songs']],
        'songUrl': data['perma_url'],
        'releaseDate': data['release_date'],
    }

async def makePlaylistResponse(data,lyrics:bool=False):
    return {
        'id': data['listid'],
        'listname': data['listname'],
        'username': data['username'],
        'listCount': data['list_count'],
        'playlistUrl': data['perma_url'],
        'image': data['image'],
        'songs':[await makeSongResponse(song=song,lyrics=lyrics) for song in data['songs']],
    }