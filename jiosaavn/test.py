
# from . import _helper, _exceptions, _validation


BASE_URL = 'https://www.jiosaavn.com/api.php?__call='
CTX = '&ctx=wap6dot0'
META_TAGS = '&includeMetaTags=0'
FORMAT = '&_format=json'
MAKER = '&_marker=0'
VERSION = lambda num: f'&api_version={num}'



def parseSearch(response:dict):
    return [parseSong(i,_internal=True) for i in  response.get('results')]

def parseAlbumSearch(response:dict):
    return [{
            'id': i.get('id'),
            'title': i.get('title'),
            'music': i.get('more_info').get('music'),
            # 'type' : i.get('type'),
            'year': i.get('year'),
            'language': _helper.capitalize(i.get('language')),
            'songCount':i.get('more_info').get('song_count'),
            'albumUrl': i.get('perma_url'),
            'imageUrls':_helper.makeDifferentQualityImages(i.get('image'),sep='-'),
            'primaryArtists':i.get('more_info').get('artistMap').get('primary_artists'),
            'featuredArtists':i.get('more_info').get('artistMap').get('featured_artists'),
            'artists':i.get('more_info').get('artistMap').get('artists'),
        }for i in  response.get('results')]

def parsePlaylistSearch(response:dict):
    return [{
            'id': i.get('listid'),
            'title': i.get('listname'),
            'type' : i.get('entity_type'),
            'language': _helper.capitalize(i.get('language')),
            'songCount':i.get('count'),
            'url': i.get('perma_url'),
            'imageUrls':_helper.makeDifferentQualityImages(i.get('image'),sep='_'),
        }for i in  response.get('results')]

def parseArtistSearch(response:dict):
    return [{
            'id': i.get('id'),
            'name': i.get('name'),
            'role' : i.get('role'),
            'type' : i.get('type'),
            'url': i.get('perma_url'),
            'imageUrls':_helper.makeDifferentQualityImages(i.get('image'),sep='-'),
        }for i in  response.get('results')]

SEARCH_CONVERTER = {

    "song": {
        'url': lambda params: f'{BASE_URL}search.getResults&p={params["page"]}&n={params["limit"]}&q={"+".join(params["query"].split(" "))}{FORMAT}{MAKER}{VERSION(0)}{CTX}',
        'parse' : parseSearch,
    },
    #version 4
    "album": {
        'url': lambda params: f'{BASE_URL}search.getAlbumResults&p={params["page"]}&n={params["limit"]}&q={"+".join(params["query"].split(" "))}{FORMAT}{MAKER}{VERSION(4)}{CTX}',
        'parse' : parseAlbumSearch,
    },

    "playlist": {
        'url': lambda params: f'{BASE_URL}search.getPlaylistResults&p={params["page"]}&n={params["limit"]}&q={"+".join(params["query"].split(" "))}{FORMAT}{MAKER}{VERSION(0)}{CTX}',
        'parse' : parsePlaylistSearch,
    },

    "artist": {
        'url': lambda params: f'{BASE_URL}search.getArtistResults&p={params["page"]}&n={params["limit"]}&q={"+".join(params["query"].split(" "))}{FORMAT}{MAKER}{VERSION(0)}{CTX}',
        'parse' : parseArtistSearch,
    },
}

