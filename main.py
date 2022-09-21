from fastapi import FastAPI ,Response,Query
from fastapi.responses import RedirectResponse

from jiosaavn import _requests, _parse , _helper,_fetch,asyncJioSaavn,syncJioSaavn

app = FastAPI()


from enum import Enum

class Type(Enum):
    song = 'song'
    album = 'album'
    playlist = 'playlist'
    artist = 'artist'

@app.get('/',include_in_schema=False)
async def root():
    return RedirectResponse('/docs')


@app.get('/async/search',tags=['Async'])
async def a_search(query:str=Query(...),type:Type=Query(Type.song),page:int=1,limit:int=10,raw:bool=False):
    return await asyncJioSaavn.JioSaavn.search(query,type.value,page=page,limit=limit,raw=raw)

@app.get('/sync/search',tags=['Sync'])
def s_search(query:str=Query(...),type:Type=Query(Type.song),page:int=1,limit:int=10,raw:bool=False):
    return syncJioSaavn.JioSaavn.search(query,type.value,page=page,limit=limit,raw=raw)


@app.get('/async',tags=['Async'])
async def a_song(id:str=Query(None),url:str=Query(None),type:Type=Query(Type.song),raw:bool=False):
    response = _fetch.JioSaavn(id, url,type, raw)
    return await response.a_get()


@app.get('/sync',tags=['Sync'])
def s_search(id:str=Query(None),url:str=Query(None),type:Type=Query(Type.song),raw:bool=False):
    # return syncJioSaavn.JioSaavn.search(query,type.value,page=page,limit=limit,raw=raw)
    response = _fetch.JioSaavn(id, url,type, raw)
    return response.s_get()

# @app.get('/test',tags=['Test'])
# async def test(id:str=Query(None),url:str=Query(None),type:Type=Query(Type.song),raw:bool=False):
#     # return syncJioSaavn.JioSaavn.search(query,type.value,page=page,limit=limit,raw=raw)
#     response = _fetch.JioSaavn(id, url,type, raw)
#     return await response.a_get()

urls =[
    #getreco pid
    'https://www.jiosaavn.com/api.php?__call=reco.getreco&api_version=4&_format=json&_marker=0&ctx=web6dot0&pid=57CSXRQs',
    #lyrics id
    'https://www.jiosaavn.com/api.php?__call=lyrics.getLyrics&lyrics_id=yCgClm0_&ctx=web6dot0&api_version=4&_format=json&_marker=0',
    #topAlbumsoftheYear album_year album_lang
    'https://www.jiosaavn.com/api.php?__call=search.topAlbumsoftheYear&api_version=4&_format=json&_marker=0&ctx=web6dot0&album_year=2022&album_lang=punjabi',
    #getTrending entity_type
    'https://www.jiosaavn.com/api.php?__call=content.getTrending&api_version=4&_format=json&_marker=0&ctx=web6dot0&entity_type=album&entity_language=punjabi',
    #artistOtherTopSongs artist_ids song_id language
    'https://www.jiosaavn.com/api.php?__call=search.artistOtherTopSongs&api_version=4&_format=json&_marker=0&ctx=web6dot0&artist_ids=742638&song_id=yCgClm0_&language=punjabi',
    #getAlbumReco albumid
    'https://www.jiosaavn.com/api.php?__call=reco.getAlbumReco&api_version=4&_format=json&_marker=0&ctx=web6dot0&albumid=34303918',

    ]

@app.get('/main',tags=['Test'])
async def main(num:int=Query(0)):
    # return syncJioSaavn.JioSaavn.search(query,type.value,page=page,limit=limit,raw=raw)
    response = await _requests.asyncGet(urls[num])

    return response