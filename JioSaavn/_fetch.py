
from . import _baseApiUrl,_requests
from . import _parseResponse as parse
from ._helper import getsongID


async def searchSong(query:str,page:int=1,limit:int=10):
    '''Searches for song in JioSaavn.
    Args:
        query (str): Sets the search query.
        page (int, optional): Sets page to the number of page. Defaults to 1.
        limit (int, optional): Sets limit to the number of results. Defaults to 10.
    Examples:
        Calling `searchSong` function gives the search result.
        >>> search = await searchSong('alone')
        >>> print(search)
        [
            {
                "id": "HgyjuLNF",
                "title": "Alone Alone (From &quot;Malli Modalaindi&quot;)",
                "image": "https://c.saavncdn.com/156/Alone-Alone-From-Malli-Modalaindi--Telugu-2021-20210920131019-150x150.jpg",
                "images": {
                    "50x50": "https://c.saavncdn.com/156/Alone-Alone-From-Malli-Modalaindi--Telugu-2021-20210920131019-50x50.jpg",
                    "150x150": "https://c.saavncdn.com/156/Alone-Alone-From-Malli-Modalaindi--Telugu-2021-20210920131019-150x150.jpg",
                    "500x500": "https://c.saavncdn.com/156/Alone-Alone-From-Malli-Modalaindi--Telugu-2021-20210920131019-500x500.jpg"
                },
                "album": "Alone Alone (From &quot;Malli Modalaindi&quot;)",
                "description": "Alone Alone (From &quot;Malli Modalaindi&quot;) - Sid Sriram, Anup Rubens",
                "has_lyrics": "false",
                "singers": [
                    "Sid Sriram",
                    "Anup Rubens"
                ],
                "language": "Telugu",
                "album_id": "29782034",
                "url": {
                    "song": "https://www.jiosaavn.com/song/alone-alone-from-malli-modalaindi/OA8SWwF8eXU",
                    "album": "https://www.jiosaavn.com/album/alone-alone-from-malli-modalaindi/lLQ4oVnaTvM_"
                },
            },
            {
                "id": "veJXEDAz",
                "title": "Alone",
                "image": "https://c.saavncdn.com/743/Alone-Punjabi-2020-20200507184621-150x150.jpg",
                "images": {
                    "50x50": "https://c.saavncdn.com/743/Alone-Punjabi-2020-20200507184621-50x50.jpg",
                    "150x150": "https://c.saavncdn.com/743/Alone-Punjabi-2020-20200507184621-150x150.jpg",
                    "500x500": "https://c.saavncdn.com/743/Alone-Punjabi-2020-20200507184621-500x500.jpg"
                },
                "album": "Alone",
                "description": "Alone - Raashi Sood",
                "has_lyrics": "false",
                "singers": [
                    "Raashi Sood"
                ],
                "language": "Punjabi",
                "album_id": "20256407",
                "url": {
                    "song": "https://www.jiosaavn.com/song/alone/Bg0haTF0dkk",
                    "album": "https://www.jiosaavn.com/album/alone/,kQ0LrBIybc_"
                },
            }
        ]
    
        '''
    return await parse.makeSearchResponse(data=await _requests.get(url=_baseApiUrl.songsearchFromSTRING(query=query,p=page,n=limit)))

async def songFromURL(url:str,lyrics:bool=False):
    '''Get song info from JioSaavn.
    Args:
        url (str): Sets the url of song.
        lyrics (bool, optional): Sets the lyrics whether to get lyrics. Defaults to False.
    Examples:
        Calling `songFromURL` function gives the search result.
        >>> result = await songFromURL('https://www.jiosaavn.com/song/alone/Bg0haTF0dkk')
        >>> print(result)
        {
            "id": "veJXEDAz",
            "song": "Alone",
            "album": "Alone",
            "year": "2020",
            "primary_artists": [
                "Raashi Sood"
            ],
            "singers": [
                "Raashi Sood"
            ],
            "image": "https://c.saavncdn.com/743/Alone-Punjabi-2020-20200507184621-500x500.jpg",
            "images": {
                "50x50": "https://c.saavncdn.com/743/Alone-Punjabi-2020-20200507184621-50x50.jpg",
                "150x150": "https://c.saavncdn.com/743/Alone-Punjabi-2020-20200507184621-150x150.jpg",
                "500x500": "https://c.saavncdn.com/743/Alone-Punjabi-2020-20200507184621-500x500.jpg"
            },
            "duration": "120",
            "label": "Raashi Sood Music",
            "albumid": "20256407",
            "language": "Punjabi",
            "copyright_text": "© 2020 Raashi Sood Music",
            "has_lyrics": "false",
            "lyrics": null,
            "media_url": "https://aac.saavncdn.com/743/dc78d52426dff2c0bf8e755c4721c398_160.mp4",
            "media_urls": {
                "96_KBPS": "https://aac.saavncdn.com/743/dc78d52426dff2c0bf8e755c4721c398_96.mp4",
                "160_KBPS": "https://aac.saavncdn.com/743/dc78d52426dff2c0bf8e755c4721c398_160.mp4",
                "320_KBPS": "https://aac.saavncdn.com/743/dc78d52426dff2c0bf8e755c4721c398_320.mp4"
            },
            "release_date": "2020-05-07",
            "url": {
                "song": "https://www.jiosaavn.com/song/alone/Bg0haTF0dkk",
                "album": "https://www.jiosaavn.com/album/alone/,kQ0LrBIybc_"
            },
        }
    '''
    return await song(id=await getsongID(url=url),lyrics=lyrics)

async def song(id:str,lyrics:bool=False):
    '''Get song info from JioSaavn.
    Args:
        id (str): Sets the id of song.
        lyrics (bool, optional): Sets the lyrics whether to get lyrics. Defaults to False.
    Examples:
        Calling `songFromID` function gives the search result.
        >>> result = await songFromID('veJXEDAz')
        >>> print(result)
        {
            "id": "veJXEDAz",
            "song": "Alone",
            "album": "Alone",
            "year": "2020",
            "primary_artists": [
                "Raashi Sood"
            ],
            "singers": [
                "Raashi Sood"
            ],
            "image": "https://c.saavncdn.com/743/Alone-Punjabi-2020-20200507184621-500x500.jpg",
            "images": {
                "50x50": "https://c.saavncdn.com/743/Alone-Punjabi-2020-20200507184621-50x50.jpg",
                "150x150": "https://c.saavncdn.com/743/Alone-Punjabi-2020-20200507184621-150x150.jpg",
                "500x500": "https://c.saavncdn.com/743/Alone-Punjabi-2020-20200507184621-500x500.jpg"
            },
            "duration": "120",
            "label": "Raashi Sood Music",
            "albumid": "20256407",
            "language": "Punjabi",
            "copyright_text": "© 2020 Raashi Sood Music",
            "has_lyrics": "false",
            "lyrics": null,
            "media_url": "https://aac.saavncdn.com/743/dc78d52426dff2c0bf8e755c4721c398_160.mp4",
            "media_urls": {
                "96_KBPS": "https://aac.saavncdn.com/743/dc78d52426dff2c0bf8e755c4721c398_96.mp4",
                "160_KBPS": "https://aac.saavncdn.com/743/dc78d52426dff2c0bf8e755c4721c398_160.mp4",
                "320_KBPS": "https://aac.saavncdn.com/743/dc78d52426dff2c0bf8e755c4721c398_320.mp4"
            },
            "release_date": "2020-05-07",
            "url": {
                "song": "https://www.jiosaavn.com/song/alone/Bg0haTF0dkk",
                "album": "https://www.jiosaavn.com/album/alone/,kQ0LrBIybc_"
            },
        }
    '''
    response = await _requests.get(url=_baseApiUrl.songFromID(id=id))
    return await parse.makeSongResponse(song=response[id],lyrics=lyrics)

async def lyricsFromURL(url:str):
    '''Get lyrics of a song from url (If Available)
    Args:
        url (str): Sets the url of song.
    Examples:
        Calling `lyrics` function gives the search result.
        >>> result = await lyrics('blMuXL1P')
        >>> print(result)
        {
        "lyrics": "bhali bhali bhalira bhali<br>sahore bahubali<br>bhali bhali bhalira bhali<br>sahore bahubali<br>jayaarti nike pattali pattali<br>bhuvanalanni jai kottali<br>gaganale chhatra pattali<br><br>haiss rudrass haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br><br>aa janani deeksha achalam<br>i koduke kavachan<br>ippuda ammaki amm ainanduka<br>pulkarinchindiga i kshana<br><br>aduulu guttal mittal gaminch<br>pidikit pidugul patti minch<br>arikul vargal durgal jayinch<br>avaniki swarganne dinch<br><br>ant maha baludina amm ori pasiwade<br>shivudaina bhavudaina ammaku sat kadantade<br><br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass haisarbhadra samudrass<br>haiss rudrass  haiss rudrass<br>haisarbhadra samudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br><br>bhali bhali bhalira bhali<br>sahore bahubali<br>jayaarti nike pattali<br>bhali bhali bhalira bhali<br>sahore bahubali<br>jayaarti nike pattali pattali<br>bhuvanalanni jai kottali<br>gaganale chhatra pattali",
        "lyrics_copyright": "Writer(s): M. M. Keeravaani, Shiva Shakthi Datta, K. Ramakrishna Lyrics powered by www.musixmatch.com",
        "snippet": "haiss rudrass  haisarbhadra samudrass"
        }
    '''
    data = await _requests.get(_baseApiUrl.lyricsFromID(id=await getsongID(url=url)))
    if data.get('status' ) == "failure":
        return {'status': f'{id} Has No Lyric'}
    return {'lyrics':data.get('lyrics'),
            'lyrics_copyright':data.get('lyrics_copyright'),
            'snippet':data.get('snippet')
            }

async def lyrics(id:str):
    '''Get lyrics of a song from id (If Available)
    Args:
        id (str): Sets the id of song.
    Examples:
        Calling `lyrics` function gives the search result.
        >>> result = await lyrics('blMuXL1P')
        >>> print(result)
        {
        "lyrics": "bhali bhali bhalira bhali<br>sahore bahubali<br>bhali bhali bhalira bhali<br>sahore bahubali<br>jayaarti nike pattali pattali<br>bhuvanalanni jai kottali<br>gaganale chhatra pattali<br><br>haiss rudrass haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br><br>aa janani deeksha achalam<br>i koduke kavachan<br>ippuda ammaki amm ainanduka<br>pulkarinchindiga i kshana<br><br>aduulu guttal mittal gaminch<br>pidikit pidugul patti minch<br>arikul vargal durgal jayinch<br>avaniki swarganne dinch<br><br>ant maha baludina amm ori pasiwade<br>shivudaina bhavudaina ammaku sat kadantade<br><br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass haisarbhadra samudrass<br>haiss rudrass  haiss rudrass<br>haisarbhadra samudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br><br>bhali bhali bhalira bhali<br>sahore bahubali<br>jayaarti nike pattali<br>bhali bhali bhalira bhali<br>sahore bahubali<br>jayaarti nike pattali pattali<br>bhuvanalanni jai kottali<br>gaganale chhatra pattali",
        "lyrics_copyright": "Writer(s): M. M. Keeravaani, Shiva Shakthi Datta, K. Ramakrishna Lyrics powered by www.musixmatch.com",
        "snippet": "haiss rudrass  haisarbhadra samudrass"
        }
    '''
    data = await _requests.get(_baseApiUrl.lyricsFromID(id=id))
    if data.get('status' ) == "failure":
        return {'status': f'{id} Has No Lyric'}
    return {'lyrics':data.get('lyrics'),
            'lyrics_copyright':data.get('lyrics_copyright'),
            'snippet':data.get('snippet')
            }

async def searchAlbum(query:str):
    '''Searches for album in JioSaavn.
    Args:
        query (str): Sets the search query.
    Examples:
        Calling `searchAlbum` function gives the search result.
        >>> search = await searchAlbum('Alone')
        >>> print(search)
        [
            {
                "id": "29782034",
                "title": "Alone Alone (From &quot;Malli Modalaindi&quot;)",
                "image": "https://c.saavncdn.com/156/Alone-Alone-From-Malli-Modalaindi--Telugu-2021-20210920131019-150x150.jpg",
                "images": {
                    "50x50": "https://c.saavncdn.com/156/Alone-Alone-From-Malli-Modalaindi--Telugu-2021-20210920131019-50x50.jpg",
                    "150x150": "https://c.saavncdn.com/156/Alone-Alone-From-Malli-Modalaindi--Telugu-2021-20210920131019-150x150.jpg",
                    "500x500": "https://c.saavncdn.com/156/Alone-Alone-From-Malli-Modalaindi--Telugu-2021-20210920131019-500x500.jpg"
                },
                "music": "Sid Sriram, Anup Rubens",
                "description": "2021 · Telugu Album · Sid Sriram, Anup Rubens",
                "year": "2021",
                "language": "Telugu",
                "url": "https://www.jiosaavn.com/album/alone-alone-from-malli-modalaindi/lLQ4oVnaTvM_",
                "song": "HgyjuLNF",
            },
            {
                "id": "1215558",
                "title": "Alone",
                "image": "https://c.saavncdn.com/794/Alone-Hindi-2014-150x150.jpg",
                "images": {
                    "50x50": "https://c.saavncdn.com/794/Alone-Hindi-2014-50x50.jpg",
                    "150x150": "https://c.saavncdn.com/794/Alone-Hindi-2014-150x150.jpg",
                    "500x500": "https://c.saavncdn.com/794/Alone-Hindi-2014-500x500.jpg"
                },
                "music": "Ankit Tiwari",
                "description": "2014 · Hindi Film · Ankit Tiwari",
                "year": "2014",
                "language": "Hindi",
                "url": "https://www.jiosaavn.com/album/alone/MmI5C7Qd8xU_",
                "song": "woZT1XKb, BW3ZjaVE, 30LGCvEo, IVnaw30E",
            },
        ]
    '''
    return await parse.makeAlbumSearchResponse(data=await _requests.get(_baseApiUrl.albumsearchFromSTRING(query=query)))

async def album(id:str):
    '''Searches for album in JioSaavn.
    Args:
        id (str): Sets thr id of album.
    Examples:
        Calling `album` function gives the search result.
        >>> result = await album('1215558')
        >>> print(result)
        {
        "albumid": "10496527",
        "title": "Baahubali 2 - The Conclusion",
        "name": "Baahubali 2 - The Conclusion",
        "year": "2017",
        "primary_artists": [
            "M. M. Keeravani"
        ],
        "image": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-150x150.jpg",
        "songs": [
            {
                "id": "blMuXL1P",
                "song": "Saahore Baahubali",
                "album": "Baahubali 2 - The Conclusion",
                "year": "2017",
                "primary_artists": [
                    "Daler Mehndi",
                    "M. M. Keeravani",
                    "Mounima Ch"
                ],
                "singers": [
                    "Daler Mehndi",
                    "M. M. Keeravani",
                    "Mounima Ch"
                ],
                "image": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-500x500.jpg",
                "images": {
                    "50x50": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-50x50.jpg",
                    "150x150": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-150x150.jpg",
                    "500x500": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-500x500.jpg"
                },
                "duration": "203",
                "label": "Lahari Music",
                "albumid": "10496527",
                "language": "Telugu",
                "copyright_text": "©  2017 Lahari Music",
                "has_lyrics": "true",
                "lyrics": null,
                "media_url": "https://aac.saavncdn.com/271/22dda6f74d38544c0b0d27d65ddddac1_160.mp4",
                "media_urls": {
                    "96_KBPS": "https://aac.saavncdn.com/271/22dda6f74d38544c0b0d27d65ddddac1_96.mp4",
                    "160_KBPS": "https://aac.saavncdn.com/271/22dda6f74d38544c0b0d27d65ddddac1_160.mp4",
                    "320_KBPS": "https://aac.saavncdn.com/271/22dda6f74d38544c0b0d27d65ddddac1_320.mp4"
                },
                "release_date": "2017-03-26",
                "url": {
                    "song": "https://www.jiosaavn.com/song/saahore-baahubali/EgQmRCx8BmM",
                    "album": "https://www.jiosaavn.com/album/baahubali-2---the-conclusion/Vm5jaOSkM7E_"
                },
            },
            {
                "id": "XvwEmXL_",
                "song": "Hamsa Naava",
                "album": "Baahubali 2 - The Conclusion",
                "year": "2017",
                "primary_artists": [
                    "Sony",
                    "Deepu"
                ],
                "singers": [
                    "Sony",
                    "Deepu"
                ],
                "image": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-500x500.jpg",
                "images": {
                    "50x50": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-50x50.jpg",
                    "150x150": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-150x150.jpg",
                    "500x500": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-500x500.jpg"
                },
                "duration": "204",
                "label": "Lahari Music",
                "albumid": "10496527",
                "language": "Telugu",
                "copyright_text": "©  2017 Lahari Music",
                "has_lyrics": "true",
                "lyrics": null,
                "media_url": "https://aac.saavncdn.com/271/5d651eeaa54b93af16a7c39999615f2d_160.mp4",
                "media_urls": {
                    "96_KBPS": "https://aac.saavncdn.com/271/5d651eeaa54b93af16a7c39999615f2d_96.mp4",
                    "160_KBPS": "https://aac.saavncdn.com/271/5d651eeaa54b93af16a7c39999615f2d_160.mp4",
                    "320_KBPS": "https://aac.saavncdn.com/271/5d651eeaa54b93af16a7c39999615f2d_320.mp4"
                },
                "release_date": "2017-03-26",
                "url": {
                    "song": "https://www.jiosaavn.com/song/hamsa-naava/KB4cdBloe2w",
                    "album": "https://www.jiosaavn.com/album/baahubali-2---the-conclusion/Vm5jaOSkM7E_"
                },
            },
            {
                "id": "M3D7qn6T",
                "song": "Kannaa Nidurinchara",
                "album": "Baahubali 2 - The Conclusion",
                "year": "2017",
                "primary_artists": [
                    "Sreenidhi Tirumala",
                    "V. Srisoumya"
                ],
                "singers": [
                    "Sreenidhi Tirumala",
                    "V. Srisoumya"
                ],
                "image": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-500x500.jpg",
                "images": {
                    "50x50": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-50x50.jpg",
                    "150x150": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-150x150.jpg",
                    "500x500": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-500x500.jpg"
                },
                "duration": "291",
                "label": "Lahari Music",
                "albumid": "10496527",
                "language": "Telugu",
                "copyright_text": "©  2017 Lahari Music",
                "has_lyrics": "true",
                "lyrics": null,
                "media_url": "https://aac.saavncdn.com/271/5e4fe5350641ff6c285d79676a483222_160.mp4",
                "media_urls": {
                    "96_KBPS": "https://aac.saavncdn.com/271/5e4fe5350641ff6c285d79676a483222_96.mp4",
                    "160_KBPS": "https://aac.saavncdn.com/271/5e4fe5350641ff6c285d79676a483222_160.mp4",
                    "320_KBPS": "https://aac.saavncdn.com/271/5e4fe5350641ff6c285d79676a483222_320.mp4"
                },
                "release_date": "2017-03-26",
                "url": {
                    "song": "https://www.jiosaavn.com/song/kannaa-nidurinchara/PVsvBgVeAWc",
                    "album": "https://www.jiosaavn.com/album/baahubali-2---the-conclusion/Vm5jaOSkM7E_"
                },
            },
        ],
        "perma_url": "https://www.jiosaavn.com/album/baahubali-2---the-conclusion/Vm5jaOSkM7E_",
        "release_date": "2017-03-26"
        }
    '''
    return await parse.makeAlbumResponse(data=await _requests.get(_baseApiUrl.albumFromID(id=id)))
