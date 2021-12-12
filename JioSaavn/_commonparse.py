
from . import __helper

def _makeSongResponse(song):
    return {
    'id': song.get('id'),
    'songName':song.get('song'),
    'albumName':song.get('album'),
    'albumId': song.get('albumid'),
    'playCount': song.get('play_count'),
    'duration': song.get('duration'),
    'label': song.get('label'),
    'primaryArtists': song.get('primary_artists'),
    'primaryArtistsId':song.get('primary_artists_id'),
    'featuredArtists': song.get('featured_artists'),
    'featuredArtistsId':song.get('featured_artists_id'),
    # 'primaryArtists': [{'artist':artist,'id':id} for artist,id in zip((song['primary_artists']).split(', '),(song['primary_artists_id']).split(', '))],
    # 'featuredArtists': [{'artist':artist,'id':id} for artist,id in zip((song['featured_artists']).split(', '),(song['featured_artists_id']).split(', '))],
    'singers': song.get('singers'),
    'starring':song.get('starring'),
    'language': __helper.ucfirst(song.get('language')),
    'copyright': song.get('copyright_text'),
    'hasLyrics' : song.get('has_lyrics'),
    'releaseDate': song.get('release_date'),
    'songUrl':song.get('perma_url'),
    'albumUrl': song.get('album_url'),
    'imagesUrls': __helper.makeDifferentQualityImages(song.get('image')),
    'audioUrls':__helper.makeDifferentQualityMediaUrls(song.get('media_preview_url')),
    'labelUrl':f"https://www.jiosaavn.com{song.get('label_url')}" if song.get('label_url') else None,
    }


def _makeSearchResponse(data):
    return [{
        'id':i.get('id'),
        'songName':i.get('title'),
        'albumId':i.get('more_info').get('album_id'),
        'albumName':i.get('more_info').get('album'),
        'playCount': i.get('play_count'),
        'imagesUrls':__helper.makeDifferentQualityImages(i.get('image')),
        'primaryArtists':i.get('more_info').get('artistMap').get('primary_artists'),
        'featuredArtists':i.get('more_info').get('artistMap').get('featured_artists'),
        'artists':i.get('more_info').get('artistMap').get('artists'),
        'description':i.get('header_desc'),
        'hasLyrics':i.get('more_info').get('has_lyrics'),
        'language':__helper.ucfirst(i.get('language')),
        'songUrl':i.get('perma_url'),
        'albumUrl':i.get('more_info').get('album_url'),
        } for i in  data.get('results')]


def _makeAlbumSearchResponse(data):
    return [{
            'id': i.get('id'),
            'albumName': i.get('title'),
            'music': i.get('music'),
            'description': i.get('description'),
            'year': i.get('more_info').get('year'),
            'language': __helper.ucfirst(i.get('more_info').get('language')),
            'songIds':i.get('more_info').get('song_pids'),
            'albumUrl': i.get('url'),
            'imagesUrls':__helper.makeDifferentQualityImages(i.get('image')),
        }for i in  data.get('albums').get('data')]

def _makeAlbumResponse(data):
    return {
        'albumId': data.get('albumid'),
        'title': data.get('title'),
        'name': data.get('name'),
        'year': data.get('year'),
        'primaryArtists': data.get('primary_artists') if data.get('primary_artists') else '',
        'image': data.get('image'),
        'songUrl': data.get('perma_url'),
        'releaseDate': data.get('release_date'),
    } if data.get('albumid') != '0' else None


def _makePlaylistResponse(data):
    return {
        'id': data.get('listid'),
        'listname': data.get('listname'),
        'username': data.get('username'),
        'listCount': data.get('list_count'),
        'playlistUrl': data.get('perma_url'),
        'image': data.get('image'),
    } if data.get('listid') else None