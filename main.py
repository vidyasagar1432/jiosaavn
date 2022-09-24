from fastapi import FastAPI ,Response,Query
from fastapi.responses import RedirectResponse

# from jiosaavn import _requests, _parse , _helper,_fetch,asyncJioSaavn,syncJioSaavn,test,_validation,_exceptions,_schema
# from jiosaavn._fetch import Type
from jiosaavn.core.fetch import syncGet,asyncGet
from jiosaavn.core import models,exceptions,fetch
from jiosaavn.core import _async

app = FastAPI()


from enum import Enum

class Type(Enum):
    song = 'song'
    album = 'album'
    playlist = 'playlist'
    artist = 'artist'
    lyrics ='lyrics'

@app.get('/',include_in_schema=False)
async def root():
    return RedirectResponse('/docs')
#mPTrDSun
# T6HEwHnO
#903166403
@app.get('/main',tags=['Test'])
async def test(id:str=Query(None),url:str=Query(None),raw:bool=False):
    # song = fetch.Song(id=id,url=url,raw=raw)
    # return await song.async_get()

    response = await _async.searchSong('love',include={'id'})

    return response


# @app.get('/async/search',tags=['Async'])
# async def a_search(query:str=Query(...),type:Type=Query(Type.song),page:int=1,limit:int=10,raw:bool=False):
#     return await asyncJioSaavn.JioSaavn.search(query,type.value,page=page,limit=limit,raw=raw)

# @app.get('/sync/search',tags=['Sync'])
# def s_search(query:str=Query(...),type:Type=Query(Type.song),page:int=1,limit:int=10,raw:bool=False):
#     return syncJioSaavn.JioSaavn.search(query,type.value,page=page,limit=limit,raw=raw)


# @app.get('/async',tags=['Async'])
# async def a_song(id:str=Query(None),url:str=Query(None),type:Type=Query(Type.song),raw:bool=False):
#     response = _fetch.JioSaavn(id, url,type, raw)
#     return await response.a_get()

# @app.get('/sync',tags=['Sync'])
# def s_search(id:str=Query(None),url:str=Query(None),type:Type=Query(Type.song),raw:bool=False):
#     # return syncJioSaavn.JioSaavn.search(query,type.value,page=page,limit=limit,raw=raw)
#     response = _fetch.JioSaavn(id, url,type, raw)
#     return response.s_get()

# @app.get('/async/search',tags=['search'])
# async def async_search(query:str=Query(...),type:Type=Query(Type.song),page:int=1,limit:int=10,raw:bool=False):

#     response = await _requests.asyncGet(url = SEARCH_CONVERTER[type.value]['url']({
#         'query':query,
#         'page':page,
#         'limit':limit
#     }))

#     return response if raw else SEARCH_CONVERTER[type.value]['parse'](response=response)

# @app.get('/sync/search',tags=['search'])
# def sync_search(id:str=Query(None),url:str=Query(None),type:Type=Query(Type.song),raw:bool=False):
#     if id:
#         response = _requests.syncGet(url = INFO_CONVERTER[type.value]['id']['url'](id=id))
#         return response if raw else INFO_CONVERTER[type.value]['id']['parse'](response=response)
#     elif url:
#         INFO_CONVERTER[type.value]['url']['validate'](url=url)
#         response = _requests.syncGet(url = INFO_CONVERTER[type.value]['url']['url'](token = url[url.rindex('/')+1:]))
#         return response if raw else INFO_CONVERTER[type.value]['url']['parse'](response=response)
#     else:
#         raise _exceptions.ValidationError('Please provide a url or id')

@app.get('/async/info',tags=['info'])
async def test(id:str=Query(None),url:str=Query(None),type:Type=Query(Type.song),raw:bool=False):
    if id:
        response = await asyncGet(url = info[type.value]['id']['url'](id=id))
        return response if raw else info[type.value]['id']['parse'](response=response,include_song={'id'})
    elif url:
        info[type.value]['url']['validate'](url=url)
        response = await asyncGet(url = info[type.value]['url']['url'](token = url[url.rindex('/')+1:]))
        return response if raw else info[type.value]['url']['parse'](response=response)
    else:
        raise exceptions.ValidationError('Please provide a url or id')

# @app.get('/sync/info',tags=['info'])
# def test(id:str=Query(None),url:str=Query(None),type:Type=Query(Type.song),raw:bool=False):
#     if id:
#         response = _requests.syncGet(url = INFO_CONVERTER[type.value]['id']['url'](id=id))
#         return response if raw else INFO_CONVERTER[type.value]['id']['parse'](response=response)
#     elif url:
#         INFO_CONVERTER[type.value]['url']['validate'](url=url)
#         response = _requests.syncGet(url = INFO_CONVERTER[type.value]['url']['url'](token = url[url.rindex('/')+1:]))
#         return response if raw else INFO_CONVERTER[type.value]['url']['parse'](response=response)
#     else:
#         raise _exceptions.ValidationError('Please provide a url or id')

# urls =[
#     # 'https://www.jiosaavn.com/api.php?__call=content.getHomepageData&_format=json'
    
#     #getreco pid
#     'https://www.jiosaavn.com/api.php?__call=reco.getreco&api_version=4&_format=json&_marker=0&ctx=web6dot0&pid=57CSXRQs',
#     #getAlbumReco albumid
#     'https://www.jiosaavn.com/api.php?__call=reco.getAlbumReco&api_version=4&_format=json&_marker=0&ctx=web6dot0&albumid=34303918',
    
#     #artistOtherTopSongs artist_ids song_id language
#     'https://www.jiosaavn.com/api.php?__call=search.artistOtherTopSongs&api_version=4&_format=json&_marker=0&ctx=web6dot0&artist_ids=742638&song_id=yCgClm0_&language=punjabi',
#     #topAlbumsoftheYear album_year album_lang
#     'https://www.jiosaavn.com/api.php?__call=search.topAlbumsoftheYear&api_version=4&_format=json&_marker=0&ctx=web6dot0&album_year=2022&album_lang=punjabi',
    
#     #getTrending entity_type entity_language
#     'https://www.jiosaavn.com/api.php?__call=content.getTrending&api_version=4&_format=json&_marker=0&ctx=web6dot0&entity_type=album&entity_language=punjabi',
#     ]

# @app.get('/url',tags=['Test'])
# async def main(id:str=Query(None),token:str=Query(None),type:Type=Query(Type.song),raw:bool=False):
#     url = 'https://www.jiosaavn.com/api.php?__call=search.artistOtherTopSongs&api_version=0&_format=json&_marker=0&ctx=web6dot0&artist_ids=742638&song_id=yCgClm0_&language=punjabi'
#     response = await _requests.asyncGet(url=url)
#     return response

