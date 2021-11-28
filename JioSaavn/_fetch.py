from typing import Optional

from . import _baseApiUrl,_requests
from . import _parseResponse as parse
from ._helper import getSongId ,getAlbumId,getPlaylistId
from ._exceptions import ValidationError,InvalidURL
from ._validation import isAlbumUrl,isSongUrl,isPlaylistUrl



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
    return await parse.makeSearchResponse(data=await _requests.getjSON(url=_baseApiUrl.songsearchFromSTRING(query=query,p=page,n=limit)))


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
    return await parse.makeAlbumSearchResponse(data=await _requests.getjSON(_baseApiUrl.albumsearchFromSTRING(query=query)))


async def song(url:Optional[str]=None,id:Optional[str]=None,lyrics:bool=False):
    '''Get song info from JioSaavn.
    Args:
        url (str): Sets the url of song.
        id (str): Sets the id of song.
        lyrics (bool): Sets the lyrics whether to get lyrics. Defaults to False.
    Examples:
        Calling `song` function gives the search result.
        >>> result = await song(id='veJXEDAz')
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
    if not (url or id):
        raise ValidationError('Please provide a url or id of a song')
    if url:
        if not isSongUrl(url=url):
            raise InvalidURL('Please provide a valid jiosaavn song url')
        id = await getSongId(url=url)
    response = await _requests.getjSON(url=_baseApiUrl.songFromID(id=id))
    return await parse.makeSongResponse(song=response[id],lyrics=lyrics)


async def album(url:Optional[str]=None,id:Optional[str]=None,lyrics:bool=False):
    '''Searches for album in JioSaavn.
    Args:
        url (str): Sets the url of album.
        id (str): Sets the id of album.
        lyrics (bool): Sets the lyrics whether to get lyrics. Defaults to False.
    Examples:
        Calling `album` function gives the search result.
        >>> result = await album(id='10496527')
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
    if not (url or id):
        raise ValidationError('Please provide a url or id of an album')
    if url:
        if not isAlbumUrl(url=url):
            raise InvalidURL('Please provide a valid jiosaavn album url')
        id = await getAlbumId(url)
    return await parse.makeAlbumResponse(data=await _requests.getjSON(_baseApiUrl.albumFromID(id=id)),lyrics=lyrics)

async def playlist(url:Optional[str]=None,id:Optional[str]=None,lyrics:bool=False):
    '''Searches for album in JioSaavn.
    Args:
        url (str): Sets the url of playlist.
        id (str): Sets the id of playlist.
        lyrics (bool): Sets the lyrics whether to get lyrics. Defaults to False.
    Examples:
        Calling `playlist` function gives the search result.
        >>> result = await playlist(url='https://www.jiosaavn.com/s/playlist/88063878238ad9a391a33c0e628d2b01/90s_Love/OykxHSA0YytFo9wdEAzFBA__')
        >>> print(result)
        {
        "listid": "268477478",
        "title": "90's Love",
        "username": "",
        "list_count": "17",
        "uid": "88063878238ad9a391a33c0e628d2b01",
        "perma_url": "https://www.jiosaavn.com/s/playlist/88063878238ad9a391a33c0e628d2b01/90s_Love/OykxHSA0YytFo9wdEAzFBA__",
        "image": "https://pli.saavncdn.com/74/78/268477478.jpg?bch=1555760417",
        "songs": [
            {
                "id": "2XLkr2Gd",
                "song": "Kal Ho Naa Ho",
                "album": "Kal Ho Naa Ho (Original Motion Picture Soundtrack)",
                "year": "2003",
                "primary_artists": [
                    "Shankar-Ehsaan-Loy",
                    "Sonu Nigam"
                ],
                "singers": [
                    "Shankar-Ehsaan-Loy",
                    "Sonu Nigam"
                ],
                "image": "https://c.saavncdn.com/909/Kal-Ho-Naa-Ho-Hindi-2003-500x500.jpg",
                "images": {
                    "50x50": "https://c.saavncdn.com/909/Kal-Ho-Naa-Ho-Hindi-2003-50x50.jpg",
                    "150x150": "https://c.saavncdn.com/909/Kal-Ho-Naa-Ho-Hindi-2003-150x150.jpg",
                    "500x500": "https://c.saavncdn.com/909/Kal-Ho-Naa-Ho-Hindi-2003-500x500.jpg"
                },
                "duration": "321",
                "label": "Sony Music Entertainment India Pvt. Ltd.",
                "albumid": "1208084",
                "language": "Hindi",
                "copyright_text": "(P) 2003 Sony Music Entertainment India Pvt. Ltd.",
                "has_lyrics": "false",
                "lyrics": null,
                "media_url": "https://aac.saavncdn.com/909/b34c95486eb42ede300a549da19a38ad_160.mp4",
                "media_urls": {
                    "96_KBPS": "https://aac.saavncdn.com/909/b34c95486eb42ede300a549da19a38ad_96.mp4",
                    "160_KBPS": "https://aac.saavncdn.com/909/b34c95486eb42ede300a549da19a38ad_160.mp4",
                    "320_KBPS": "https://aac.saavncdn.com/909/b34c95486eb42ede300a549da19a38ad_320.mp4"
                },
                "release_date": "2003-09-20",
                "url": {
                    "song": "https://www.jiosaavn.com/song/kal-ho-naa-ho/QjAnWgYCcFc",
                    "album": "https://www.jiosaavn.com/album/kal-ho-naa-ho-original-motion-picture-soundtrack/wxleSiR74Dg_"
                }
            },
            {
                "id": "lULDgPcz",
                "song": "Main Hoon Na",
                "album": "Main Hoon Na",
                "year": "2004",
                "primary_artists": [
                    "Sonu Nigam",
                    "Shreya Ghoshal"
                ],
                "singers": [
                    "Sonu Nigam",
                    "Shreya Ghoshal"
                ],
                "image": "https://c.saavncdn.com/388/Main-Hoon-Na-Hindi-2004-500x500.jpg",
                "images": {
                    "50x50": "https://c.saavncdn.com/388/Main-Hoon-Na-Hindi-2004-50x50.jpg",
                    "150x150": "https://c.saavncdn.com/388/Main-Hoon-Na-Hindi-2004-150x150.jpg",
                    "500x500": "https://c.saavncdn.com/388/Main-Hoon-Na-Hindi-2004-500x500.jpg"
                },
                "duration": "361",
                "label": "",
                "albumid": "1037222",
                "language": "Hindi",
                "copyright_text": "©  2004 ",
                "has_lyrics": "true",
                "lyrics": null,
                "media_url": "https://aac.saavncdn.com/388/348841a9282b5b362526a8098a7f4491_160.mp4",
                "media_urls": {
                    "96_KBPS": "https://aac.saavncdn.com/388/348841a9282b5b362526a8098a7f4491_96.mp4",
                    "160_KBPS": "https://aac.saavncdn.com/388/348841a9282b5b362526a8098a7f4491_160.mp4",
                    "320_KBPS": "https://aac.saavncdn.com/388/348841a9282b5b362526a8098a7f4491_320.mp4"
                },
                "release_date": "2004-02-27",
                "url": {
                    "song": "https://www.jiosaavn.com/song/main-hoon-na/HD0ndRNgVEk",
                    "album": "https://www.jiosaavn.com/album/main-hoon-na/Gf2uDkAyAkg_"
                }
            },
            {
                "id": "jFerJMnc",
                "song": "Koi Mil Gaya",
                "album": "Kuch Kuch Hota Hai (Original Motion Picture Soundtrack)",
                "year": "1998",
                "primary_artists": [
                    "Jatin-Lalit",
                    "Kavita Krishnamurthy",
                    "Udit Narayan",
                    "Alka Yagnik"
                ],
                "singers": [
                    "Jatin-Lalit",
                    "Kavita Krishnamurthy",
                    "Udit Narayan",
                    "Alka Yagnik"
                ],
                "image": "https://c.saavncdn.com/907/Kuch-Kuch-Hota-Hai-Hindi-1998-20190516130035-500x500.jpg",
                "images": {
                    "50x50": "https://c.saavncdn.com/907/Kuch-Kuch-Hota-Hai-Hindi-1998-20190516130035-50x50.jpg",
                    "150x150": "https://c.saavncdn.com/907/Kuch-Kuch-Hota-Hai-Hindi-1998-20190516130035-150x150.jpg",
                    "500x500": "https://c.saavncdn.com/907/Kuch-Kuch-Hota-Hai-Hindi-1998-20190516130035-500x500.jpg"
                },
                "duration": "437",
                "label": "Sony Music Entertainment India Pvt. Ltd.",
                "albumid": "1035265",
                "language": "Hindi",
                "copyright_text": "(P) 1998 Sony Music Entertainment India Pvt. Ltd.",
                "has_lyrics": "false",
                "lyrics": null,
                "media_url": "https://aac.saavncdn.com/907/2d22f49ec5435c9d606742ae2648a5a2_160.mp4",
                "media_urls": {
                    "96_KBPS": "https://aac.saavncdn.com/907/2d22f49ec5435c9d606742ae2648a5a2_96.mp4",
                    "160_KBPS": "https://aac.saavncdn.com/907/2d22f49ec5435c9d606742ae2648a5a2_160.mp4",
                    "320_KBPS": "https://aac.saavncdn.com/907/2d22f49ec5435c9d606742ae2648a5a2_320.mp4"
                },
                "release_date": "1998-08-19",
                "url": {
                    "song": "https://www.jiosaavn.com/song/koi-mil-gaya/Gi4OQz59WVA",
                    "album": "https://www.jiosaavn.com/album/kuch-kuch-hota-hai-original-motion-picture-soundtrack/zvqnBMKjQeM_"
                }
            },
        ]
    }
    '''
    if not (url or id):
        raise ValidationError('Please provide a url or id of playlist')
    if url:
        if not isPlaylistUrl(url=url):
            raise InvalidURL('Please provide a valid jiosaavn playlist url')
        id = await getPlaylistId(url)
    return await parse.makePlaylistResponse(data= await _requests.getjSON(url=_baseApiUrl.playlistFromID(id=id)),lyrics=lyrics)


async def lyrics(url:Optional[str]=None,id:Optional[str]=None):
    '''Get lyrics of a song from id (If Available)
    Args:
        url (str): Sets the url of playlist.
        id (str): Sets the id of song.
    Examples:
        Calling `lyrics` function gives the search result.
        >>> result = await lyrics(id='blMuXL1P')
        >>> print(result)
        {
        "lyrics": "bhali bhali bhalira bhali<br>sahore bahubali<br>bhali bhali bhalira bhali<br>sahore bahubali<br>jayaarti nike pattali pattali<br>bhuvanalanni jai kottali<br>gaganale chhatra pattali<br><br>haiss rudrass haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br><br>aa janani deeksha achalam<br>i koduke kavachan<br>ippuda ammaki amm ainanduka<br>pulkarinchindiga i kshana<br><br>aduulu guttal mittal gaminch<br>pidikit pidugul patti minch<br>arikul vargal durgal jayinch<br>avaniki swarganne dinch<br><br>ant maha baludina amm ori pasiwade<br>shivudaina bhavudaina ammaku sat kadantade<br><br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass haisarbhadra samudrass<br>haiss rudrass  haiss rudrass<br>haisarbhadra samudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br><br>bhali bhali bhalira bhali<br>sahore bahubali<br>jayaarti nike pattali<br>bhali bhali bhalira bhali<br>sahore bahubali<br>jayaarti nike pattali pattali<br>bhuvanalanni jai kottali<br>gaganale chhatra pattali",
        "lyrics_copyright": "Writer(s): M. M. Keeravaani, Shiva Shakthi Datta, K. Ramakrishna Lyrics powered by www.musixmatch.com",
        "snippet": "haiss rudrass  haisarbhadra samudrass"
        }
    '''
    if not (url or id):
        raise ValidationError('Please provide a url or id of a song')
    if url:
        if not isSongUrl(url=url):
            raise InvalidURL('Please provide a valid jiosaavn song url')
        id = await getSongId(url=url)
    data = await _requests.getjSON(_baseApiUrl.lyricsFromID(id=id))
    if data.get('status' ) == "failure":
        return {'status': f'no lyric'}
    return {'lyrics':data.get('lyrics'),
            'lyrics_copyright':data.get('lyrics_copyright'),
            'snippet':data.get('snippet')
            }