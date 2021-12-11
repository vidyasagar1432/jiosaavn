# [JioSaavn](https://github.com/vidyasagar1432/JioSaavn)

#### Search for JioSaavn songs & album. Get song ,album, lyric & playlist information from url or id.

## Installing

```bash
pip3 install jiosaavn
```

## Async and Sync Functions
```python
from jiosaavn.Async import JioSaavn,searchSong,searchAlbum,song,album,playlist,lyrics

from jiosaavn.Sync import JioSaavn,searchSong,searchAlbum,song,album,playlist,lyrics
```
#### Search for only songs

```python
# Async
from jiosaavn.Async import searchSong
search = await searchSong('alone')
print(search)

# Sync
from jiosaavn.Sync import searchSong
search = searchSong('alone')
print(search)
```
<details>
 <summary> Example Result</summary>

```json
[
  {
    "id": "mlOelmXY",
    "songName": "Alone",
    "albumId": "10149322",
    "albumName": "Alone",
    "playCount": "49207056",
    "imagesUrls": {
      "50x50": "http://c.saavncdn.com/522/Alone-English-2017-20180131085202-50x50.jpg",
      "150x150": "http://c.saavncdn.com/522/Alone-English-2017-20180131085202-150x150.jpg",
      "500x500": "http://c.saavncdn.com/522/Alone-English-2017-20180131085202-500x500.jpg"
    },
    "primaryArtists": [
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "primary_artists",
        "image": "https://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker-/wbWcxgUNzyo_"
      }
    ],
    "featuredArtists": [],
    "artists": [
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "music",
        "image": "https://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker-/wbWcxgUNzyo_"
      },
      {
        "id": "822579",
        "name": "Jesper Borgen",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jesper-borgen-/2odnY,ZN-jQ_"
      },
      {
        "id": "1425075",
        "name": "Anders Frøen",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/anders-froen-/Wj4QA5E85tc_"
      },
      {
        "id": "1625408",
        "name": "Gunnar Greve",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/gunnar-greve-/MYLcGokRN0w_"
      },
      {
        "id": "648765",
        "name": "Jonnali Parmenius",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jonnali-parmenius-/C,kojV56,2A_"
      },
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "singer",
        "image": "https://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker-/wbWcxgUNzyo_"
      },
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "lyricist",
        "image": "https://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker-/wbWcxgUNzyo_"
      },
      {
        "id": "822579",
        "name": "Jesper Borgen",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jesper-borgen-/2odnY,ZN-jQ_"
      },
      {
        "id": "1425075",
        "name": "Anders Frøen",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/anders-froen-/Wj4QA5E85tc_"
      },
      {
        "id": "1625408",
        "name": "Gunnar Greve",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/gunnar-greve-/MYLcGokRN0w_"
      },
      {
        "id": "648765",
        "name": "Jonnali Parmenius",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jonnali-parmenius-/C,kojV56,2A_"
      }
    ],
    "description": "Track from Alan Walker from album Alone.",
    "hasLyrics": "false",
    "language": "English",
    "songUrl": "https://www.jiosaavn.com/song/alone/HQQkVBhdb2o",
    "albumUrl": "https://www.jiosaavn.com/album/alone/RGziQ8ScK3g_"
  },
  {
    "id": "HgyjuLNF",
    "songName": "Alone Alone (From &quot;Malli Modalaindi&quot;)",
    "albumId": "29782034",
    "albumName": "Alone Alone (From &quot;Malli Modalaindi&quot;)",
    "playCount": "949200",
    "imagesUrls": {
      "50x50": "http://c.saavncdn.com/156/Alone-Alone-From-Malli-Modalaindi--Telugu-2021-20210920131019-50x50.jpg",
      "150x150": "http://c.saavncdn.com/156/Alone-Alone-From-Malli-Modalaindi--Telugu-2021-20210920131019-150x150.jpg",
      "500x500": "http://c.saavncdn.com/156/Alone-Alone-From-Malli-Modalaindi--Telugu-2021-20210920131019-500x500.jpg"
    },
    "primaryArtists": [
      {
        "id": "689580",
        "name": "Sid Sriram",
        "role": "primary_artists",
        "image": "https://c.saavncdn.com/artists/Sid_Sriram_004_20200321102120_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/sid-sriram-/634AK8t6tAU_"
      },
      {
        "id": "684364",
        "name": "Anup Rubens",
        "role": "primary_artists",
        "image": "https://c.saavncdn.com/artists/Anup_Rubens_002_20190905131837_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/anup-rubens-/JW5jvWu7Qr4_"
      }
    ],
    "featuredArtists": [],
    "artists": [
      {
        "id": "689580",
        "name": "Sid Sriram",
        "role": "singer",
        "image": "https://c.saavncdn.com/artists/Sid_Sriram_004_20200321102120_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/sid-sriram-/634AK8t6tAU_"
      },
      {
        "id": "684364",
        "name": "Anup Rubens",
        "role": "singer",
        "image": "https://c.saavncdn.com/artists/Anup_Rubens_002_20190905131837_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/anup-rubens-/JW5jvWu7Qr4_"
      },
      {
        "id": "455242",
        "name": "Krishna Chaitanya",
        "role": "lyricist",
        "image": "https://c.saavncdn.com/artists/Krishna_Chaitanya_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/krishna-chaitanya-/-hO9iJXocuw_"
      },
      {
        "id": "465174",
        "name": "Sumanth",
        "role": "starring",
        "image": "https://c.saavncdn.com/artists/Sumanth_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/sumanth-/4x,JIbiqKm4_"
      },
      {
        "id": "2529284",
        "name": "Naina Ganguly",
        "role": "starring",
        "image": "https://c.saavncdn.com/artists/Naina_Ganguly_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/naina-ganguly-/qHB7N4SD9Nk_"
      }
    ],
    "description": "Track from Sid Sriram and Anup Rubens from album Alone Alone (From &quot;Malli Modalaindi&quot;).",
    "hasLyrics": "false",
    "language": "Telugu",
    "songUrl": "https://www.jiosaavn.com/song/alone-alone-from-malli-modalaindi/OA8SWwF8eXU",
    "albumUrl": "https://www.jiosaavn.com/album/alone-alone-from-malli-modalaindi/lLQ4oVnaTvM_"
  },
  {
    "id": "t4-oIFZc",
    "songName": "Alone",
    "albumId": "2337820",
    "albumName": "Alone",
    "playCount": "6475644",
    "imagesUrls": {
      "50x50": "http://c.saavncdn.com/638/Alone-English-2016-50x50.jpg",
      "150x150": "http://c.saavncdn.com/638/Alone-English-2016-150x150.jpg",
      "500x500": "http://c.saavncdn.com/638/Alone-English-2016-500x500.jpg"
    },
    "primaryArtists": [
      {
        "id": "862454",
        "name": "Marshmello",
        "role": "primary_artists",
        "image": "http://c.saavncdn.com/artists/Marshmello_20190123065408_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/marshmello/Eevs5FiVgus_"
      }
    ],
    "featuredArtists": [],
    "artists": [
      {
        "id": "862454",
        "name": "Marshmello",
        "role": "singer",
        "image": "http://c.saavncdn.com/artists/Marshmello_20190123065408_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/marshmello/Eevs5FiVgus_"
      }
    ],
    "description": "Track from Marshmello from album Alone.",
    "hasLyrics": "false",
    "language": "English",
    "songUrl": "https://www.jiosaavn.com/song/alone/BFxGXj12bVA",
    "albumUrl": "https://www.jiosaavn.com/album/alone/nUiJOh,-0pY_"
  },
  {
    "id": "JV7dA4mV",
    "songName": "Alone (Instrumental Remix)",
    "albumId": "10149322",
    "albumName": "Alone",
    "playCount": "2937767",
    "imagesUrls": {
      "50x50": "http://c.saavncdn.com/522/Alone-English-2017-20180131085202-50x50.jpg",
      "150x150": "http://c.saavncdn.com/522/Alone-English-2017-20180131085202-150x150.jpg",
      "500x500": "http://c.saavncdn.com/522/Alone-English-2017-20180131085202-500x500.jpg"
    },
    "primaryArtists": [
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "primary_artists",
        "image": "https://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker-/wbWcxgUNzyo_"
      }
    ],
    "featuredArtists": [],
    "artists": [
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "music",
        "image": "https://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker-/wbWcxgUNzyo_"
      },
      {
        "id": "648765",
        "name": "Jonnali Parmenius",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jonnali-parmenius-/C,kojV56,2A_"
      },
      {
        "id": "1425075",
        "name": "Anders Frøen",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/anders-froen-/Wj4QA5E85tc_"
      },
      {
        "id": "822579",
        "name": "Jesper Borgen",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jesper-borgen-/2odnY,ZN-jQ_"
      },
      {
        "id": "1625408",
        "name": "Gunnar Greve",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/gunnar-greve-/MYLcGokRN0w_"
      },
      {
        "id": "755154",
        "name": "Noonie Bao",
        "role": "music",
        "image": "https://c.saavncdn.com/954/Sorry-Not-Sorry-English-2016-150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/noonie-bao-/TlZufM7L6sQ_"
      },
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "singer",
        "image": "https://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker-/wbWcxgUNzyo_"
      },
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "lyricist",
        "image": "https://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker-/wbWcxgUNzyo_"
      },
      {
        "id": "648765",
        "name": "Jonnali Parmenius",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jonnali-parmenius-/C,kojV56,2A_"
      },
      {
        "id": "1425075",
        "name": "Anders Frøen",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/anders-froen-/Wj4QA5E85tc_"
      },
      {
        "id": "822579",
        "name": "Jesper Borgen",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jesper-borgen-/2odnY,ZN-jQ_"
      },
      {
        "id": "1625408",
        "name": "Gunnar Greve",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/gunnar-greve-/MYLcGokRN0w_"
      },
      {
        "id": "755154",
        "name": "Noonie Bao",
        "role": "lyricist",
        "image": "https://c.saavncdn.com/954/Sorry-Not-Sorry-English-2016-150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/noonie-bao-/TlZufM7L6sQ_"
      }
    ],
    "description": "Track from Alan Walker from album Alone.",
    "hasLyrics": "false",
    "language": "Unknown",
    "songUrl": "https://www.jiosaavn.com/song/alone-instrumental-remix/Oj5cVTUEWmU",
    "albumUrl": "https://www.jiosaavn.com/album/alone/RGziQ8ScK3g_"
  },
  {
    "id": "4zBsiDyX",
    "songName": "Alone (Restrung)",
    "albumId": "10149322",
    "albumName": "Alone",
    "playCount": "2290141",
    "imagesUrls": {
      "50x50": "http://c.saavncdn.com/522/Alone-English-2017-20180131085202-50x50.jpg",
      "150x150": "http://c.saavncdn.com/522/Alone-English-2017-20180131085202-150x150.jpg",
      "500x500": "http://c.saavncdn.com/522/Alone-English-2017-20180131085202-500x500.jpg"
    },
    "primaryArtists": [
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "primary_artists",
        "image": "https://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker-/wbWcxgUNzyo_"
      }
    ],
    "featuredArtists": [],
    "artists": [
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "music",
        "image": "https://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker-/wbWcxgUNzyo_"
      },
      {
        "id": "822579",
        "name": "Jesper Borgen",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jesper-borgen-/2odnY,ZN-jQ_"
      },
      {
        "id": "1425075",
        "name": "Anders Frøen",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/anders-froen-/Wj4QA5E85tc_"
      },
      {
        "id": "1625408",
        "name": "Gunnar Greve",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/gunnar-greve-/MYLcGokRN0w_"
      },
      {
        "id": "755154",
        "name": "Noonie Bao",
        "role": "music",
        "image": "https://c.saavncdn.com/954/Sorry-Not-Sorry-English-2016-150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/noonie-bao-/TlZufM7L6sQ_"
      },
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "singer",
        "image": "https://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker-/wbWcxgUNzyo_"
      },
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "lyricist",
        "image": "https://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker-/wbWcxgUNzyo_"
      },
      {
        "id": "822579",
        "name": "Jesper Borgen",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jesper-borgen-/2odnY,ZN-jQ_"
      },
      {
        "id": "1425075",
        "name": "Anders Frøen",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/anders-froen-/Wj4QA5E85tc_"
      },
      {
        "id": "1625408",
        "name": "Gunnar Greve",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/gunnar-greve-/MYLcGokRN0w_"
      },
      {
        "id": "648765",
        "name": "Jonnali Parmenius",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jonnali-parmenius-/C,kojV56,2A_"
      }
    ],
    "description": "Track from Alan Walker from album Alone.",
    "hasLyrics": "false",
    "language": "English",
    "songUrl": "https://www.jiosaavn.com/song/alone-restrung/RBIpQh10Tms",
    "albumUrl": "https://www.jiosaavn.com/album/alone/RGziQ8ScK3g_"
  },
  {
    "id": "8BsyRlFY",
    "songName": "Alone, Pt. II",
    "albumId": "18273908",
    "albumName": "Alone, Pt. II",
    "playCount": "8189590",
    "imagesUrls": {
      "50x50": "http://c.saavncdn.com/574/Alone-Pt-II-English-2019-20191210153050-50x50.jpg",
      "150x150": "http://c.saavncdn.com/574/Alone-Pt-II-English-2019-20191210153050-150x150.jpg",
      "500x500": "http://c.saavncdn.com/574/Alone-Pt-II-English-2019-20191210153050-500x500.jpg"
    },
    "primaryArtists": [
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "primary_artists",
        "image": "https://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker-/wbWcxgUNzyo_"
      },
      {
        "id": "3685366",
        "name": "Ava Max",
        "role": "primary_artists",
        "image": "https://c.saavncdn.com/artists/Ava_Max_20190322070605_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/ava-max-/ExpLP,ur0tw_"
      }
    ],
    "featuredArtists": [],
    "artists": [
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "music",
        "image": "https://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker-/wbWcxgUNzyo_"
      },
      {
        "id": "3333917",
        "name": "Marcus Arnbekk",
        "role": "music",
        "image": "https://c.saavncdn.com/063/Sawarne-Lage-Tropical-House-Mix-From-Mitron--Hindi-2018-20180912142000-150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/marcus-arnbekk-/aAij0Two6rU_"
      },
      {
        "id": "5936693",
        "name": "Alexander Standal Pavelich",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alexander-standal-pavelich-/qilY-eLQNJY_"
      },
      {
        "id": "6003540",
        "name": "Amanda Ava Koci",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/amanda-ava-koci-/6Hu,xwA,2Xs_"
      },
      {
        "id": "820452",
        "name": "Halvor Folstad",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/halvor-folstad-/yjQsAthxb6U_"
      },
      {
        "id": "820451",
        "name": "Dag Holtan-Hartwig",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/dag-holtan-hartwig-/RsQKyyo4z5w_"
      },
      {
        "id": "772800",
        "name": "Erik \r\nSmaaland",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/erik-smaaland-/,kczMl-H-RA_"
      },
      {
        "id": "6092767",
        "name": "Moa Pettersson Hammar",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/moa-pettersson-hammar-/TO9tzxEz1hM_"
      },
      {
        "id": "659013",
        "name": "Carl Hovind",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/carl-hovind-/h1VoDMs3MuI_"
      },
      {
        "id": "1584282",
        "name": "Fredrik Borch Olsen",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/fredrik-borch-olsen-/iq2hSfiwJTE_"
      },
      {
        "id": "1584281",
        "name": "Øyvind Sauvik",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/Oyvind-sauvik-/,PQoc6ZC7ys_"
      },
      {
        "id": "1625408",
        "name": "Gunnar Greve",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/gunnar-greve-/MYLcGokRN0w_"
      },
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "singer",
        "image": "https://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker-/wbWcxgUNzyo_"
      },
      {
        "id": "3685366",
        "name": "Ava Max",
        "role": "singer",
        "image": "https://c.saavncdn.com/artists/Ava_Max_20190322070605_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/ava-max-/ExpLP,ur0tw_"
      },
      {
        "id": "7374795",
        "name": "Alan Walker &amp; Ava Max",
        "role": "singer",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker--ava-max-/pbR4d6hacyk_"
      },
      {
        "id": "5936693",
        "name": "Alexander Standal Pavelich",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alexander-standal-pavelich-/qilY-eLQNJY_"
      },
      {
        "id": "6003540",
        "name": "Amanda \r\nAva Koci",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/amanda-ava-koci-/6Hu,xwA,2Xs_"
      },
      {
        "id": "820452",
        "name": "Halvor Folstad",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/halvor-folstad-/yjQsAthxb6U_"
      },
      {
        "id": "820451",
        "name": "Dag Holtan-Hartwig",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/dag-holtan-hartwig-/RsQKyyo4z5w_"
      },
      {
        "id": "772800",
        "name": "Erik Smaaland",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/erik-smaaland-/,kczMl-H-RA_"
      },
      {
        "id": "6092767",
        "name": "Moa Pettersson Hammar",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/moa-pettersson-hammar-/TO9tzxEz1hM_"
      },
      {
        "id": "1584281",
        "name": "Øyvind Sauvik",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/Oyvind-sauvik-/,PQoc6ZC7ys_"
      }
    ],
    "description": "Track from Alan Walker and Ava Max from album Alone, Pt. II.",
    "hasLyrics": "false",
    "language": "English",
    "songUrl": "https://www.jiosaavn.com/song/alone-pt.-ii/SCoYSCZccWo",
    "albumUrl": "https://www.jiosaavn.com/album/alone-pt.-ii/ZCqviQsE5dI_"
  },
  {
    "id": "rE_g9GJw",
    "songName": "Alone",
    "albumId": "14508997",
    "albumName": "Different World",
    "playCount": "49127064",
    "imagesUrls": {
      "50x50": "http://c.saavncdn.com/562/Different-World-English-2018-20181130144209-50x50.jpg",
      "150x150": "http://c.saavncdn.com/562/Different-World-English-2018-20181130144209-150x150.jpg",
      "500x500": "http://c.saavncdn.com/562/Different-World-English-2018-20181130144209-500x500.jpg"
    },
    "primaryArtists": [
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "primary_artists",
        "image": "http://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker/wbWcxgUNzyo_"
      }
    ],
    "featuredArtists": [],
    "artists": [
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "music",
        "image": "http://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker/wbWcxgUNzyo_"
      },
      {
        "id": "822579",
        "name": "Jesper Borgen",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jesper-borgen/2odnY,ZN-jQ_"
      },
      {
        "id": "1425075",
        "name": "Anders Frøen",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/anders-froen/Wj4QA5E85tc_"
      },
      {
        "id": "1625408",
        "name": "Gunnar Greve",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/gunnar-greve/MYLcGokRN0w_"
      },
      {
        "id": "648765",
        "name": "Jonnali Parmenius",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jonnali-parmenius/C,kojV56,2A_"
      },
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "singer",
        "image": "http://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker/wbWcxgUNzyo_"
      },
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "lyricist",
        "image": "http://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker/wbWcxgUNzyo_"
      },
      {
        "id": "822579",
        "name": "Jesper Borgen",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jesper-borgen/2odnY,ZN-jQ_"
      },
      {
        "id": "1425075",
        "name": "Anders Frøen",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/anders-froen/Wj4QA5E85tc_"
      },
      {
        "id": "1625408",
        "name": "Gunnar Greve",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/gunnar-greve/MYLcGokRN0w_"
      },
      {
        "id": "648765",
        "name": "Jonnali Parmenius",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jonnali-parmenius/C,kojV56,2A_"
      }
    ],
    "description": "Track from Alan Walker from album Different World.",
    "hasLyrics": "false",
    "language": "English",
    "songUrl": "https://www.jiosaavn.com/song/alone/Ai00Vk13fUQ",
    "albumUrl": "https://www.jiosaavn.com/album/different-world/rIQHDwKT5do_"
  },
  {
    "id": "PZZwQkMz",
    "songName": "Alone",
    "albumId": "11624914",
    "albumName": "Alone",
    "playCount": "254125",
    "imagesUrls": {
      "50x50": "http://c.saavncdn.com/229/Alone-English-2017-20171011004751-50x50.jpg",
      "150x150": "http://c.saavncdn.com/229/Alone-English-2017-20171011004751-150x150.jpg",
      "500x500": "http://c.saavncdn.com/229/Alone-English-2017-20171011004751-500x500.jpg"
    },
    "primaryArtists": [
      {
        "id": "733470",
        "name": "The PropheC",
        "role": "primary_artists",
        "image": "http://c.saavncdn.com/artists/The_Prophec_001_20180105065027_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/the-prophec/fgZhf3jAs,w_"
      },
      {
        "id": "4328877",
        "name": "Arjun",
        "role": "primary_artists",
        "image": "http://c.saavncdn.com/309/Tingo-English-2019-20190907032346-150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/arjun/QPoHRfOnxYw_"
      }
    ],
    "featuredArtists": [],
    "artists": [
      {
        "id": "733470",
        "name": "The PropheC",
        "role": "singer",
        "image": "http://c.saavncdn.com/artists/The_Prophec_001_20180105065027_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/the-prophec/fgZhf3jAs,w_"
      },
      {
        "id": "4328877",
        "name": "Arjun",
        "role": "singer",
        "image": "http://c.saavncdn.com/309/Tingo-English-2019-20190907032346-150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/arjun/QPoHRfOnxYw_"
      }
    ],
    "description": "Track from The PropheC and Arjun from album Alone.",
    "hasLyrics": "false",
    "language": "Punjabi",
    "songUrl": "https://www.jiosaavn.com/song/alone/IDIxRiVbekk",
    "albumUrl": "https://www.jiosaavn.com/album/alone/2WJX1MgJeHE_"
  },
  {
    "id": "qj84--vy",
    "songName": "Alone",
    "albumId": "27978399",
    "albumName": "Planet Her",
    "playCount": "14695",
    "imagesUrls": {
      "50x50": "http://c.saavncdn.com/852/Planet-Her-English-2021-20210621224521-50x50.jpg",
      "150x150": "http://c.saavncdn.com/852/Planet-Her-English-2021-20210621224521-150x150.jpg",
      "500x500": "http://c.saavncdn.com/852/Planet-Her-English-2021-20210621224521-500x500.jpg"
    },
    "primaryArtists": [
      {
        "id": "697799",
        "name": "Doja Cat",
        "role": "primary_artists",
        "image": "http://c.saavncdn.com/artists/Doja_Cat_20200218145042_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/doja-cat/GuwOruHLpLk_"
      }
    ],
    "featuredArtists": [],
    "artists": [
      {
        "id": "697800",
        "name": "Amala Zandile Dlamini",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/amala-zandile-dlamini/2vDxJiTJILg_"
      },
      {
        "id": "1369835",
        "name": "David Sprecher",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/david-sprecher/I0riLFoGTFM_"
      },
      {
        "id": "711386",
        "name": "Linden Jay",
        "role": "music",
        "image": "http://c.saavncdn.com/artists/Linden_Jay_20200801080928_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/linden-jay/MayJGMfyFFE_"
      },
      {
        "id": "1612237",
        "name": "Geordan Reid-Campbell",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/geordan-reid-campbell/4DXeN7Rfry0_"
      },
      {
        "id": "1832834",
        "name": "Laura Roy",
        "role": "music",
        "image": "http://c.saavncdn.com/509/Temporary-English-2018-20180628142700-150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/laura-roy/esJI34CKlL4_"
      },
      {
        "id": "572447",
        "name": "Antwoine Collins",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/antwoine-collins/E3ZI75XCjN0_"
      },
      {
        "id": "697799",
        "name": "Doja Cat",
        "role": "singer",
        "image": "http://c.saavncdn.com/artists/Doja_Cat_20200218145042_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/doja-cat/GuwOruHLpLk_"
      },
      {
        "id": "697800",
        "name": "Amala Zandile Dlamini",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/amala-zandile-dlamini/2vDxJiTJILg_"
      },
      {
        "id": "1369835",
        "name": "David Sprecher",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/david-sprecher/I0riLFoGTFM_"
      },
      {
        "id": "711386",
        "name": "Linden Jay",
        "role": "lyricist",
        "image": "http://c.saavncdn.com/artists/Linden_Jay_20200801080928_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/linden-jay/MayJGMfyFFE_"
      },
      {
        "id": "1612237",
        "name": "Geordan Reid-Campbell",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/geordan-reid-campbell/4DXeN7Rfry0_"
      },
      {
        "id": "1832834",
        "name": "Laura Roy",
        "role": "lyricist",
        "image": "http://c.saavncdn.com/509/Temporary-English-2018-20180628142700-150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/laura-roy/esJI34CKlL4_"
      },
      {
        "id": "572447",
        "name": "Antwoine Collins",
        "role": "lyricist",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/antwoine-collins/E3ZI75XCjN0_"
      }
    ],
    "description": "Track from Doja Cat from album Planet Her.",
    "hasLyrics": "false",
    "language": "English",
    "songUrl": "https://www.jiosaavn.com/song/alone/AQJTBVkdQUo",
    "albumUrl": "https://www.jiosaavn.com/album/planet-her/0dhlIg,ymL4_"
  },
  {
    "id": "HGdNS35N",
    "songName": "Alone (Lost Frequencies Remix)",
    "albumId": "10294431",
    "albumName": "Alone (Remixes)",
    "playCount": "120132",
    "imagesUrls": {
      "50x50": "http://c.saavncdn.com/173/Alone-Remixes--English-2017-50x50.jpg",
      "150x150": "http://c.saavncdn.com/173/Alone-Remixes--English-2017-150x150.jpg",
      "500x500": "http://c.saavncdn.com/173/Alone-Remixes--English-2017-500x500.jpg"
    },
    "primaryArtists": [
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "primary_artists",
        "image": "http://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker/wbWcxgUNzyo_"
      }
    ],
    "featuredArtists": [],
    "artists": [
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "music",
        "image": "http://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker/wbWcxgUNzyo_"
      },
      {
        "id": "822579",
        "name": "Jesper Borgen",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/jesper-borgen/2odnY,ZN-jQ_"
      },
      {
        "id": "1425075",
        "name": "Anders Frøen",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/anders-froen/Wj4QA5E85tc_"
      },
      {
        "id": "1625408",
        "name": "Gunnar Greve",
        "role": "music",
        "image": "",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/gunnar-greve/MYLcGokRN0w_"
      },
      {
        "id": "755154",
        "name": "Noonie Bao",
        "role": "music",
        "image": "http://c.saavncdn.com/954/Sorry-Not-Sorry-English-2016-150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/noonie-bao/TlZufM7L6sQ_"
      },
      {
        "id": "1335467",
        "name": "Alan Walker",
        "role": "singer",
        "image": "http://c.saavncdn.com/artists/Alan_Walker_002_20190507112228_150x150.jpg",
        "type": "artist",
        "perma_url": "https://www.jiosaavn.com/artist/alan-walker/wbWcxgUNzyo_"
      }
    ],
    "description": "Track from Alan Walker from album Alone (Remixes).",
    "hasLyrics": "false",
    "language": "English",
    "songUrl": "https://www.jiosaavn.com/song/alone-lost-frequencies-remix/OC8PfycDAn0",
    "albumUrl": "https://www.jiosaavn.com/album/alone-remixes/v6elO30IMmw_"
  }
]
```
</details>

#### Search for only albums

```python
# Async
from jiosaavn.Async import searchAlbum
search = await searchAlbum('alone')
print(search)

# Sync
from jiosaavn.Sync import searchAlbum
search = await searchAlbum('alone')
print(search)
```

<details>
 <summary> Example Result</summary>

```json
[
  {
    "id": "10149322",
    "albumName": "Alone",
    "music": "Alan Walker",
    "description": "2016 · English Album · Alan Walker",
    "year": "2016",
    "language": "English",
    "songIds": "mlOelmXY, JV7dA4mV, 4zBsiDyX",
    "albumUrl": "https://www.jiosaavn.com/album/alone/RGziQ8ScK3g_",
    "imagesUrls": {
      "50x50": "http://c.saavncdn.com/522/Alone-English-2017-20180131085202-50x50.jpg",
      "150x150": "http://c.saavncdn.com/522/Alone-English-2017-20180131085202-150x150.jpg",
      "500x500": "http://c.saavncdn.com/522/Alone-English-2017-20180131085202-500x500.jpg"
    }
  },
  {
    "id": "29782034",
    "albumName": "Alone Alone (From &quot;Malli Modalaindi&quot;)",
    "music": "Sid Sriram, Anup Rubens",
    "description": "2021 · Telugu Album · Sid Sriram, Anup Rubens",
    "year": "2021",
    "language": "Telugu",
    "songIds": "HgyjuLNF",
    "albumUrl": "https://www.jiosaavn.com/album/alone-alone-from-malli-modalaindi/lLQ4oVnaTvM_",
    "imagesUrls": {
      "50x50": "http://c.saavncdn.com/156/Alone-Alone-From-Malli-Modalaindi--Telugu-2021-20210920131019-50x50.jpg",
      "150x150": "http://c.saavncdn.com/156/Alone-Alone-From-Malli-Modalaindi--Telugu-2021-20210920131019-150x150.jpg",
      "500x500": "http://c.saavncdn.com/156/Alone-Alone-From-Malli-Modalaindi--Telugu-2021-20210920131019-500x500.jpg"
    }
  },
  {
    "id": "1215558",
    "albumName": "Alone",
    "music": "Ankit Tiwari",
    "description": "2014 · Hindi Film · Ankit Tiwari",
    "year": "2014",
    "language": "Hindi",
    "songIds": "woZT1XKb, BW3ZjaVE, 30LGCvEo, IVnaw30E",
    "albumUrl": "https://www.jiosaavn.com/album/alone/MmI5C7Qd8xU_",
    "imagesUrls": {
      "50x50": "http://c.saavncdn.com/794/Alone-Hindi-2014-50x50.jpg",
      "150x150": "http://c.saavncdn.com/794/Alone-Hindi-2014-150x150.jpg",
      "500x500": "http://c.saavncdn.com/794/Alone-Hindi-2014-500x500.jpg"
    }
  }
]
```

</details>

#### Get Album from url or id

```python
# Async
from jiosaavn.Async import album
# result = await album(id='10496527')
result = await album(url='https://www.jiosaavn.com/album/baahubali-2---the-conclusion/Vm5jaOSkM7E_')
print(result)

# Sync
from jiosaavn.Sync import album
# result = album(id='10496527')
result = album(url='https://www.jiosaavn.com/album/baahubali-2---the-conclusion/Vm5jaOSkM7E_')
print(result)
```

<details>
 <summary> Example Result</summary>

```json
{
  "albumId": "10496527",
  "title": "Baahubali 2 - The Conclusion",
  "name": "Baahubali 2 - The Conclusion",
  "year": "2017",
  "primaryArtists": [
    "M. M. Keeravani"
  ],
  "image": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-150x150.jpg",
  "songs": [
    {
      "id": "blMuXL1P",
      "songName": "Saahore Baahubali",
      "albumName": "Baahubali 2 - The Conclusion",
      "albumId": "10496527",
      "playCount": "8446610",
      "duration": "203",
      "label": "Lahari Music",
      "primaryArtists": "Daler Mehndi, M. M. Keeravani, Mounima Ch",
      "primaryArtistsId": "455652, 813721, 2632973",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Daler Mehndi, M. M. Keeravani, Mounima Ch",
      "starring": "Prabhas, Anushka Shetty, Tamannaah Bhatia, Rana Daggubati, Sathyaraj, Nassar, Ramya Krishna, Subbaraju",
      "language": "Telugu",
      "copyright": "©  2017 Lahari Music",
      "hasLyrics": "true",
      "lyrics": null,
      "releaseDate": "2017-03-26",
      "songUrl": "https://www.jiosaavn.com/song/saahore-baahubali/EgQmRCx8BmM",
      "albumUrl": "https://www.jiosaavn.com/album/baahubali-2---the-conclusion/Vm5jaOSkM7E_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-50x50.jpg",
        "150x150": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-150x150.jpg",
        "500x500": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/271/22dda6f74d38544c0b0d27d65ddddac1_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/271/22dda6f74d38544c0b0d27d65ddddac1_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/271/22dda6f74d38544c0b0d27d65ddddac1_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/lahari-music-albums/L899GJu3hlQ_"
    },
    {
      "id": "XvwEmXL_",
      "songName": "Hamsa Naava",
      "albumName": "Baahubali 2 - The Conclusion",
      "albumId": "10496527",
      "playCount": "8985568",
      "duration": "204",
      "label": "Lahari Music",
      "primaryArtists": "Sony, Deepu",
      "primaryArtistsId": "593945, 455239",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Sony, Deepu",
      "starring": "Prabhas, Anushka Shetty, Tamannaah Bhatia, Rana Daggubati, Sathyaraj, Nassar, Ramya Krishna, Subbaraju",
      "language": "Telugu",
      "copyright": "©  2017 Lahari Music",
      "hasLyrics": "true",
      "lyrics": null,
      "releaseDate": "2017-03-26",
      "songUrl": "https://www.jiosaavn.com/song/hamsa-naava/KB4cdBloe2w",
      "albumUrl": "https://www.jiosaavn.com/album/baahubali-2---the-conclusion/Vm5jaOSkM7E_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-50x50.jpg",
        "150x150": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-150x150.jpg",
        "500x500": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/271/5d651eeaa54b93af16a7c39999615f2d_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/271/5d651eeaa54b93af16a7c39999615f2d_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/271/5d651eeaa54b93af16a7c39999615f2d_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/lahari-music-albums/L899GJu3hlQ_"
    },
    {
      "id": "M3D7qn6T",
      "songName": "Kannaa Nidurinchara",
      "albumName": "Baahubali 2 - The Conclusion",
      "albumId": "10496527",
      "playCount": "4455028",
      "duration": "291",
      "label": "Lahari Music",
      "primaryArtists": "Sreenidhi Tirumala, V. Srisoumya",
      "primaryArtistsId": "5523265, 3112246",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Sreenidhi Tirumala, V. Srisoumya",
      "starring": "Prabhas, Anushka Shetty, Tamannaah Bhatia, Rana Daggubati, Sathyaraj, Nassar, Ramya Krishna, Subbaraju",
      "language": "Telugu",
      "copyright": "©  2017 Lahari Music",
      "hasLyrics": "true",
      "lyrics": null,
      "releaseDate": "2017-03-26",
      "songUrl": "https://www.jiosaavn.com/song/kannaa-nidurinchara/PVsvBgVeAWc",
      "albumUrl": "https://www.jiosaavn.com/album/baahubali-2---the-conclusion/Vm5jaOSkM7E_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-50x50.jpg",
        "150x150": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-150x150.jpg",
        "500x500": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/271/5e4fe5350641ff6c285d79676a483222_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/271/5e4fe5350641ff6c285d79676a483222_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/271/5e4fe5350641ff6c285d79676a483222_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/lahari-music-albums/L899GJu3hlQ_"
    },
    {
      "id": "VclbtPav",
      "songName": "Dandaalayyaa",
      "albumName": "Baahubali 2 - The Conclusion",
      "albumId": "10496527",
      "playCount": "7810471",
      "duration": "210",
      "label": "Lahari Music",
      "primaryArtists": "Kaala Bhairava",
      "primaryArtistsId": "1941508",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Kaala Bhairava",
      "starring": "Prabhas, Anushka Shetty, Tamannaah Bhatia, Rana Daggubati, Sathyaraj, Nassar, Ramya Krishna, Subbaraju",
      "language": "Telugu",
      "copyright": "©  2017 Lahari Music",
      "hasLyrics": "true",
      "lyrics": null,
      "releaseDate": "2017-03-26",
      "songUrl": "https://www.jiosaavn.com/song/dandaalayyaa/JgsHUwBgVkU",
      "albumUrl": "https://www.jiosaavn.com/album/baahubali-2---the-conclusion/Vm5jaOSkM7E_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-50x50.jpg",
        "150x150": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-150x150.jpg",
        "500x500": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/271/2faba1a6f1efc5eacffb400b903018fa_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/271/2faba1a6f1efc5eacffb400b903018fa_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/271/2faba1a6f1efc5eacffb400b903018fa_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/lahari-music-albums/L899GJu3hlQ_"
    },
    {
      "id": "TqF9_GIG",
      "songName": "Oka Praanam",
      "albumName": "Baahubali 2 - The Conclusion",
      "albumId": "10496527",
      "playCount": "4905658",
      "duration": "173",
      "label": "Lahari Music",
      "primaryArtists": "Kaala Bhairava",
      "primaryArtistsId": "1941508",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Kaala Bhairava",
      "starring": "Prabhas, Anushka Shetty, Tamannaah Bhatia, Rana Daggubati, Sathyaraj, Nassar, Ramya Krishna, Subbaraju",
      "language": "Telugu",
      "copyright": "©  2017 Lahari Music",
      "hasLyrics": "true",
      "lyrics": null,
      "releaseDate": "2017-03-26",
      "songUrl": "https://www.jiosaavn.com/song/oka-praanam/JBktCCt3fnQ",
      "albumUrl": "https://www.jiosaavn.com/album/baahubali-2---the-conclusion/Vm5jaOSkM7E_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-50x50.jpg",
        "150x150": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-150x150.jpg",
        "500x500": "https://c.saavncdn.com/271/Baahubali-2-The-Conclusion-Telugu-2017-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/271/02e7896ac6dee9a2b49c45b96d5583cf_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/271/02e7896ac6dee9a2b49c45b96d5583cf_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/271/02e7896ac6dee9a2b49c45b96d5583cf_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/lahari-music-albums/L899GJu3hlQ_"
    }
  ],
  "songUrl": "https://www.jiosaavn.com/album/baahubali-2---the-conclusion/Vm5jaOSkM7E_",
  "releaseDate": "2017-03-26"
}
```

</details>


#### Get song from url or id

```python
# Async
from jiosaavn.Async import song
# result = await song(id='veJXEDAz')
result = await song(url='https://www.jiosaavn.com/song/alone/Bg0haTF0dkk')
print(result)

# Sync
from jiosaavn.Sync import song
# result = song(id='veJXEDAz')
result = song(url='https://www.jiosaavn.com/song/alone/Bg0haTF0dkk')
print(result)
```

<details>
 <summary> Example Result</summary>

```json
{
  "id": "veJXEDAz",
  "songName": "Alone",
  "albumName": "Alone",
  "albumId": "20256407",
  "playCount": 102546,
  "duration": "120",
  "label": "Raashi Sood Music",
  "primaryArtists": "Raashi Sood",
  "primaryArtistsId": "758310",
  "featuredArtists": "",
  "featuredArtistsId": "",
  "singers": "Raashi Sood",
  "starring": "",
  "language": "Punjabi",
  "copyright": "© 2020 Raashi Sood Music",
  "hasLyrics": "false",
  "lyrics": null,
  "releaseDate": "2020-05-07",
  "songUrl": "https://www.jiosaavn.com/song/alone/Bg0haTF0dkk",
  "albumUrl": "https://www.jiosaavn.com/album/alone/,kQ0LrBIybc_",
  "imagesUrls": {
    "50x50": "https://c.saavncdn.com/743/Alone-Punjabi-2020-20200507184621-50x50.jpg",
    "150x150": "https://c.saavncdn.com/743/Alone-Punjabi-2020-20200507184621-150x150.jpg",
    "500x500": "https://c.saavncdn.com/743/Alone-Punjabi-2020-20200507184621-500x500.jpg"
  },
  "audioUrls": {
    "96_KBPS": "https://aac.saavncdn.com/743/dc78d52426dff2c0bf8e755c4721c398_96.mp4",
    "160_KBPS": "https://aac.saavncdn.com/743/dc78d52426dff2c0bf8e755c4721c398_160.mp4",
    "320_KBPS": "https://aac.saavncdn.com/743/dc78d52426dff2c0bf8e755c4721c398_320.mp4"
  },
  "labelUrl": "https://www.jiosaavn.com/label/raashi-sood-music-albums/P4Ln5V7QgIA_"
}
```

</details>

#### Get lyric from url or id

```python
# Async
from jiosaavn.Async import lyrics
# result = await lyrics(id='blMuXL1P')
result = await lyrics(url='https://www.jiosaavn.com/song/alone/Bg0haTF0dkk')
print(result)

# Sync
from jiosaavn.Sync import lyrics
# result = lyrics(id='blMuXL1P')
result = lyrics(url='https://www.jiosaavn.com/song/alone/Bg0haTF0dkk')
print(result)
```

<details>
 <summary> Example Result</summary>

```json
{
  "lyrics": "bhali bhali bhalira bhali<br>sahore bahubali<br>bhali bhali bhalira bhali<br>sahore bahubali<br>jayaarti nike pattali pattali<br>bhuvanalanni jai kottali<br>gaganale chhatra pattali<br><br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br><br>aa janani deeksha achalam<br>i koduke kavachan<br>ippuda ammaki amm ainanduka<br>pulkarinchindiga i kshana<br><br>aduulu guttal mittal gaminch<br>pidikit pidugul patti minch<br>arikul vargal durgal jayinch<br>avaniki swarganne dinch<br><br>ant maha baludina amm ori pasiwade<br>shivudaina bhavudaina ammaku sat kadantade<br><br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haiss rudrass<br>haisarbhadra samudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br>haiss rudrass  haisarbhadra samudrass<br><br>bhali bhali bhalira bhali<br>sahore bahubali<br>jayaarti nike pattali<br>bhali bhali bhalira bhali<br>sahore bahubali<br>jayaarti nike pattali pattali<br>bhuvanalanni jai kottali<br>gaganale chhatra pattali",
  "lyrics_copyright": "Writer(s): M. M. Keeravaani, Shiva Shakthi Datta, K. Ramakrishna\nLyrics powered by www.musixmatch.com",
  "snippet": "haiss rudrass  haisarbhadra samudrass"
}
```

</details>

#### Get playlist from url or id

```python
# Async
from jiosaavn.Async import playlist
# result = await playlist(id='268477478')
result = await playlist(url='https://www.jiosaavn.com/s/playlist/88063878238ad9a391a33c0e628d2b01/90s_Love/OykxHSA0YytFo9wdEAzFBA__')
print(result)

# Sync
from jiosaavn.Sync import playlist
# result = playlist(id='268477478')
result = playlist(url='https://www.jiosaavn.com/s/playlist/88063878238ad9a391a33c0e628d2b01/90s_Love/OykxHSA0YytFo9wdEAzFBA__')
print(result)
```

<details>
 <summary> Example Result</summary>

```json
{
  "id": "268477478",
  "listname": "90's Love",
  "username": "",
  "listCount": "17",
  "playlistUrl": "https://www.jiosaavn.com/s/playlist/88063878238ad9a391a33c0e628d2b01/90s_Love/OykxHSA0YytFo9wdEAzFBA__",
  "image": "https://pli.saavncdn.com/74/78/268477478.jpg?bch=1555760417",
  "songs": [
    {
      "id": "2XLkr2Gd",
      "songName": "Kal Ho Naa Ho",
      "albumName": "Kal Ho Naa Ho (Original Motion Picture Soundtrack)",
      "albumId": "1208084",
      "playCount": "22559746",
      "duration": "321",
      "label": "Sony Music Entertainment India Pvt. Ltd.",
      "primaryArtists": "Shankar-Ehsaan-Loy, Sonu Nigam",
      "primaryArtistsId": "455280, 455125",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Shankar-Ehsaan-Loy, Sonu Nigam",
      "starring": "Shah Rukh Khan, Preity Zinta, Saif Ali Khan, Jaya Bachchan",
      "language": "Hindi",
      "copyright": "(P) 2003 Sony Music Entertainment India Pvt. Ltd.",
      "hasLyrics": "false",
      "lyrics": null,
      "releaseDate": "2003-09-20",
      "songUrl": "https://www.jiosaavn.com/song/kal-ho-naa-ho/QjAnWgYCcFc",
      "albumUrl": "https://www.jiosaavn.com/album/kal-ho-naa-ho-original-motion-picture-soundtrack/wxleSiR74Dg_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/909/Kal-Ho-Naa-Ho-Hindi-2003-50x50.jpg",
        "150x150": "https://c.saavncdn.com/909/Kal-Ho-Naa-Ho-Hindi-2003-150x150.jpg",
        "500x500": "https://c.saavncdn.com/909/Kal-Ho-Naa-Ho-Hindi-2003-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/909/b34c95486eb42ede300a549da19a38ad_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/909/b34c95486eb42ede300a549da19a38ad_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/909/b34c95486eb42ede300a549da19a38ad_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/sony-music-entertainment-india-pvt.-ltd.-albums/LaFAA6h1q2U_"
    },
    {
      "id": "lULDgPcz",
      "songName": "Main Hoon Na",
      "albumName": "Main Hoon Na",
      "albumId": "1037222",
      "playCount": "12003605",
      "duration": "361",
      "label": "",
      "primaryArtists": "Sonu Nigam, Shreya Ghoshal",
      "primaryArtistsId": "455125, 455130",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Sonu Nigam, Shreya Ghoshal",
      "starring": "Shah Rukh Khan, Suniel Shetty, Susmit Sen, Zayed Khan, Amrita Rao",
      "language": "Hindi",
      "copyright": "©  2004 ",
      "hasLyrics": "true",
      "lyrics": null,
      "releaseDate": "2004-02-27",
      "songUrl": "https://www.jiosaavn.com/song/main-hoon-na/HD0ndRNgVEk",
      "albumUrl": "https://www.jiosaavn.com/album/main-hoon-na/Gf2uDkAyAkg_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/388/Main-Hoon-Na-Hindi-2004-50x50.jpg",
        "150x150": "https://c.saavncdn.com/388/Main-Hoon-Na-Hindi-2004-150x150.jpg",
        "500x500": "https://c.saavncdn.com/388/Main-Hoon-Na-Hindi-2004-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/388/348841a9282b5b362526a8098a7f4491_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/388/348841a9282b5b362526a8098a7f4491_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/388/348841a9282b5b362526a8098a7f4491_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/-albums/6DLuXO3VoTo_"
    },
    {
      "id": "jFerJMnc",
      "songName": "Koi Mil Gaya",
      "albumName": "Kuch Kuch Hota Hai (Original Motion Picture Soundtrack)",
      "albumId": "1035265",
      "playCount": "15982751",
      "duration": "437",
      "label": "Sony Music Entertainment India Pvt. Ltd.",
      "primaryArtists": "Jatin-Lalit, Kavita Krishnamurti Subramaniam, Udit Narayan, Alka Yagnik",
      "primaryArtistsId": "455534, 455158, 455127, 455120",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Jatin-Lalit, Kavita Krishnamurti Subramaniam, Udit Narayan, Alka Yagnik",
      "starring": "Shah Rukh Khan, Kajol, Rani Mukerji, Salman Khan",
      "language": "Hindi",
      "copyright": "(P) 1998 Sony Music Entertainment India Pvt. Ltd.",
      "hasLyrics": "false",
      "lyrics": null,
      "releaseDate": "1998-08-19",
      "songUrl": "https://www.jiosaavn.com/song/koi-mil-gaya/Gi4OQz59WVA",
      "albumUrl": "https://www.jiosaavn.com/album/kuch-kuch-hota-hai-original-motion-picture-soundtrack/zvqnBMKjQeM_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/907/Kuch-Kuch-Hota-Hai-Hindi-1998-20190516130035-50x50.jpg",
        "150x150": "https://c.saavncdn.com/907/Kuch-Kuch-Hota-Hai-Hindi-1998-20190516130035-150x150.jpg",
        "500x500": "https://c.saavncdn.com/907/Kuch-Kuch-Hota-Hai-Hindi-1998-20190516130035-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/907/2d22f49ec5435c9d606742ae2648a5a2_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/907/2d22f49ec5435c9d606742ae2648a5a2_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/907/2d22f49ec5435c9d606742ae2648a5a2_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/sony-music-entertainment-india-pvt.-ltd.-albums/LaFAA6h1q2U_"
    },
    {
      "id": "U3wEEo6F",
      "songName": "Tujhe Dekha To",
      "albumName": "Dilwale Dulhania Le Jayenge",
      "albumId": "1120992",
      "playCount": "101871236",
      "duration": "303",
      "label": "Saregama",
      "primaryArtists": "Lata Mangeshkar, Kumar Sanu",
      "primaryArtistsId": "455109, 455142",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Lata Mangeshkar, Kumar Sanu",
      "starring": "Shah Rukh Khan, Kajol, Anupam Kher, Amrish Puri, Farida Jalal, Satish Shah, Achala Sachdev, Mandira Bedi, Karan Johar",
      "language": "Hindi",
      "copyright": "©  1995 Saregama",
      "hasLyrics": "true",
      "lyrics": null,
      "releaseDate": "1995-10-20",
      "songUrl": "https://www.jiosaavn.com/song/tujhe-dekha-to/JVscdDFfAXU",
      "albumUrl": "https://www.jiosaavn.com/album/dilwale-dulhania-le-jayenge/IL9HglkwPtk_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/588/Dilwale-Dulhania-Le-Jayenge-Hindi-1995-20171114-50x50.jpg",
        "150x150": "https://c.saavncdn.com/588/Dilwale-Dulhania-Le-Jayenge-Hindi-1995-20171114-150x150.jpg",
        "500x500": "https://c.saavncdn.com/588/Dilwale-Dulhania-Le-Jayenge-Hindi-1995-20171114-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/588/1915cd0934f79eeb646ffebde384e59d_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/588/1915cd0934f79eeb646ffebde384e59d_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/588/1915cd0934f79eeb646ffebde384e59d_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/saregama-albums/MNccah3udrQ_"
    },
    {
      "id": "rtdvmBBB",
      "songName": "Kuch Kuch Hota Hai",
      "albumName": "Kuch Kuch Hota Hai (Original Motion Picture Soundtrack)",
      "albumId": "1035265",
      "playCount": "37765129",
      "duration": "297",
      "label": "Sony Music Entertainment India Pvt. Ltd.",
      "primaryArtists": "Jatin-Lalit, Udit Narayan",
      "primaryArtistsId": "455534, 455127",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Jatin-Lalit, Udit Narayan, Alka Yagnik",
      "starring": "Shah Rukh Khan, Kajol, Rani Mukerji, Salman Khan",
      "language": "Hindi",
      "copyright": "(P) 1998 Sony Music Entertainment India Pvt. Ltd.",
      "hasLyrics": "false",
      "lyrics": null,
      "releaseDate": "1998-08-19",
      "songUrl": "https://www.jiosaavn.com/song/kuch-kuch-hota-hai/AhwPRxlydXE",
      "albumUrl": "https://www.jiosaavn.com/album/kuch-kuch-hota-hai-original-motion-picture-soundtrack/zvqnBMKjQeM_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/907/Kuch-Kuch-Hota-Hai-Hindi-1998-20190516130035-50x50.jpg",
        "150x150": "https://c.saavncdn.com/907/Kuch-Kuch-Hota-Hai-Hindi-1998-20190516130035-150x150.jpg",
        "500x500": "https://c.saavncdn.com/907/Kuch-Kuch-Hota-Hai-Hindi-1998-20190516130035-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/907/f7bbb1a1ce5af61c560fc4795d2beec9_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/907/f7bbb1a1ce5af61c560fc4795d2beec9_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/907/f7bbb1a1ce5af61c560fc4795d2beec9_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/sony-music-entertainment-india-pvt.-ltd.-albums/LaFAA6h1q2U_"
    },
    {
      "id": "WdqMxZ6u",
      "songName": "Chand Sifarish",
      "albumName": "Fanaa",
      "albumId": "1027146",
      "playCount": "21457062",
      "duration": "275",
      "label": "YRF Music",
      "primaryArtists": "Shaan, Kailash Kher, Jatin-Lalit, Prasoon Joshi",
      "primaryArtistsId": "455135, 455425, 455534, 456278",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Shaan, Kailash Kher",
      "starring": "Aamir Khan, Kajol, Rishi Kapoor, Kirron Kher, Sharat Saxena, Tabu",
      "language": "Hindi",
      "copyright": "© 2006 YRF Music",
      "hasLyrics": "true",
      "lyrics": null,
      "releaseDate": "2006-05-26",
      "songUrl": "https://www.jiosaavn.com/song/chand-sifarish/JwwafAxqAUY",
      "albumUrl": "https://www.jiosaavn.com/album/fanaa/k,TIgv1ORbc_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/146/Fanaa-Hindi-2006-20190329181154-50x50.jpg",
        "150x150": "https://c.saavncdn.com/146/Fanaa-Hindi-2006-20190329181154-150x150.jpg",
        "500x500": "https://c.saavncdn.com/146/Fanaa-Hindi-2006-20190329181154-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/146/53c9ccea6717dc94d957d1f1f5163723_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/146/53c9ccea6717dc94d957d1f1f5163723_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/146/53c9ccea6717dc94d957d1f1f5163723_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/yrf-music-albums/XqFShgT4cps_"
    },
    {
      "id": "nrt-2lCH",
      "songName": "Kaho Naa Pyar Hai - Happy",
      "albumName": "Kaho Naa Pyar Hai",
      "albumId": "1065819",
      "playCount": "22156513",
      "duration": "424",
      "label": "Saregama",
      "primaryArtists": "Udit Narayan, Alka Yagnik",
      "primaryArtistsId": "455127, 455120",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "",
      "starring": "",
      "language": "Hindi",
      "copyright": "℗ 2000 Saregama India Ltd",
      "hasLyrics": "true",
      "lyrics": null,
      "releaseDate": "2000-01-14",
      "songUrl": "https://www.jiosaavn.com/song/kaho-naa-pyar-hai---happy/HhofHEZcdHs",
      "albumUrl": "https://www.jiosaavn.com/album/kaho-naa-pyar-hai/Ubn5MgPXop0_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/446/Kaho-Naa-Pyar-Hai-Hindi-2000-20200901153916-50x50.jpg",
        "150x150": "https://c.saavncdn.com/446/Kaho-Naa-Pyar-Hai-Hindi-2000-20200901153916-150x150.jpg",
        "500x500": "https://c.saavncdn.com/446/Kaho-Naa-Pyar-Hai-Hindi-2000-20200901153916-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/446/b9e40ccc02bc6003d19cbeea7b94f999_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/446/b9e40ccc02bc6003d19cbeea7b94f999_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/446/b9e40ccc02bc6003d19cbeea7b94f999_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/saregama-albums/MNccah3udrQ_"
    },
    {
      "id": "XoM84Oe0",
      "songName": "Na Tum Jano Na Hum",
      "albumName": "Kaho Naa Pyar Hai",
      "albumId": "1065819",
      "playCount": "8870487",
      "duration": "383",
      "label": "Saregama",
      "primaryArtists": "Lucky Ali, Ramya NSK, Ramya",
      "primaryArtistsId": "458663, 489109, 8558530",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Ramya NSK",
      "starring": "",
      "language": "Hindi",
      "copyright": "℗ 2000 Saregama India Ltd",
      "hasLyrics": "true",
      "lyrics": null,
      "releaseDate": "2000-01-14",
      "songUrl": "https://www.jiosaavn.com/song/na-tum-jano-na-hum/KAcmCUB-UgM",
      "albumUrl": "https://www.jiosaavn.com/album/kaho-naa-pyar-hai/Ubn5MgPXop0_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/446/Kaho-Naa-Pyar-Hai-Hindi-2000-20200901153916-50x50.jpg",
        "150x150": "https://c.saavncdn.com/446/Kaho-Naa-Pyar-Hai-Hindi-2000-20200901153916-150x150.jpg",
        "500x500": "https://c.saavncdn.com/446/Kaho-Naa-Pyar-Hai-Hindi-2000-20200901153916-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/446/aa1ccf11169c840b47b2fcff5965cb9b_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/446/aa1ccf11169c840b47b2fcff5965cb9b_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/446/aa1ccf11169c840b47b2fcff5965cb9b_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/saregama-albums/MNccah3udrQ_"
    },
    {
      "id": "NTBW-riy",
      "songName": "Ek Ladki Ko Dekha",
      "albumName": "1942 A Love Story",
      "albumId": "2616633",
      "playCount": "47818632",
      "duration": "275",
      "label": "Saregama",
      "primaryArtists": "Kumar Sanu",
      "primaryArtistsId": "455142",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "",
      "starring": "",
      "language": "Hindi",
      "copyright": "℗ 1994 Saregama India Ltd",
      "hasLyrics": "false",
      "lyrics": null,
      "releaseDate": "1994-12-31",
      "songUrl": "https://www.jiosaavn.com/song/ek-ladki-ko-dekha/PjwpZllCXko",
      "albumUrl": "https://www.jiosaavn.com/album/1942-a-love-story/QzB7uLA5Nc8_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/767/1942-A-Love-Story-Bengali-1994-20200904083912-50x50.jpg",
        "150x150": "https://c.saavncdn.com/767/1942-A-Love-Story-Bengali-1994-20200904083912-150x150.jpg",
        "500x500": "https://c.saavncdn.com/767/1942-A-Love-Story-Bengali-1994-20200904083912-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/023/3e92eef0ab01146c3aadc64dc1f367e3_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/023/3e92eef0ab01146c3aadc64dc1f367e3_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/023/3e92eef0ab01146c3aadc64dc1f367e3_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/saregama-albums/MNccah3udrQ_"
    },
    {
      "id": "kaO__nHs",
      "songName": "Ek Pal Ka Jeena",
      "albumName": "Kaho Naa Pyar Hai",
      "albumId": "1065819",
      "playCount": "7032530",
      "duration": "397",
      "label": "Saregama",
      "primaryArtists": "Lucky Ali",
      "primaryArtistsId": "458663",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "",
      "starring": "",
      "language": "Hindi",
      "copyright": "℗ 2000 Saregama India Ltd",
      "hasLyrics": "false",
      "lyrics": null,
      "releaseDate": "2000-01-14",
      "songUrl": "https://www.jiosaavn.com/song/ek-pal-ka-jeena/Gwkkbitef0A",
      "albumUrl": "https://www.jiosaavn.com/album/kaho-naa-pyar-hai/Ubn5MgPXop0_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/446/Kaho-Naa-Pyar-Hai-Hindi-2000-20200901153916-50x50.jpg",
        "150x150": "https://c.saavncdn.com/446/Kaho-Naa-Pyar-Hai-Hindi-2000-20200901153916-150x150.jpg",
        "500x500": "https://c.saavncdn.com/446/Kaho-Naa-Pyar-Hai-Hindi-2000-20200901153916-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/446/3842602eecfe24f9b5ac07b893d6ebde_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/446/3842602eecfe24f9b5ac07b893d6ebde_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/446/3842602eecfe24f9b5ac07b893d6ebde_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/saregama-albums/MNccah3udrQ_"
    },
    {
      "id": "oGwjH99j",
      "songName": "Urvashi Urvashi",
      "albumName": "Hum Se Hai Muqabala - Kadalan",
      "albumId": "1030440",
      "playCount": "4022380",
      "duration": "381",
      "label": "Ishtar Music Pvt. Ltd.",
      "primaryArtists": "A.R. Rahman, Shankar Mahadevan, Noel James",
      "primaryArtistsId": "456269, 455275, 465106",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "A.R. Rahman, Shankar Mahadevan, Noel James",
      "starring": "",
      "language": "Hindi",
      "copyright": "©  1995 Ishtar Music Pvt. Ltd.",
      "hasLyrics": "true",
      "lyrics": null,
      "releaseDate": "1995-03-01",
      "songUrl": "https://www.jiosaavn.com/song/urvashi-urvashi/Hy8cWzwJDlk",
      "albumUrl": "https://www.jiosaavn.com/album/hum-se-hai-muqabala---kadalan/6ERJ58loulU_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/081/Hum-Se-Hai-Muqabala-Kadalan-Hindi-1995-20211126170542-50x50.jpg",
        "150x150": "https://c.saavncdn.com/081/Hum-Se-Hai-Muqabala-Kadalan-Hindi-1995-20211126170542-150x150.jpg",
        "500x500": "https://c.saavncdn.com/081/Hum-Se-Hai-Muqabala-Kadalan-Hindi-1995-20211126170542-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/440/bdbc73d95d132ca02fb3ca37ee79a7ab_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/440/bdbc73d95d132ca02fb3ca37ee79a7ab_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/440/bdbc73d95d132ca02fb3ca37ee79a7ab_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/ishtar-music-pvt.-ltd.-albums/zUyefLXpY-M_"
    },
    {
      "id": "qFSo3L4m",
      "songName": "Aati Kya Khandala",
      "albumName": "Ghulam",
      "albumId": "1028040",
      "playCount": "4569000",
      "duration": "252",
      "label": "Tips Music",
      "primaryArtists": "Aamir Khan, Alka Yagnik",
      "primaryArtistsId": "455463, 455120",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Aamir Khan, Alka Yagnik",
      "starring": "Aamir Khan, Rani Mukerji",
      "language": "Hindi",
      "copyright": "© 1998 Tips Industries Ltd.",
      "hasLyrics": "true",
      "lyrics": null,
      "releaseDate": "1998-03-08",
      "songUrl": "https://www.jiosaavn.com/song/aati-kya-khandala/AS44Xkd8A14",
      "albumUrl": "https://www.jiosaavn.com/album/ghulam/jdczLfCD0ec_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/599/Ghulam-Hindi-1998-20190816135120-50x50.jpg",
        "150x150": "https://c.saavncdn.com/599/Ghulam-Hindi-1998-20190816135120-150x150.jpg",
        "500x500": "https://c.saavncdn.com/599/Ghulam-Hindi-1998-20190816135120-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/599/191e10a590f1eaaa69ca5d947410b84d_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/599/191e10a590f1eaaa69ca5d947410b84d_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/599/191e10a590f1eaaa69ca5d947410b84d_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/tips-music-albums/WyMes45YplY_"
    },
    {
      "id": "TX73Q0ZS",
      "songName": "Pehla Nasha",
      "albumName": "Jo Jeeta Wohi Sikandar",
      "albumId": "2616666",
      "playCount": "47200441",
      "duration": "293",
      "label": "Saregama",
      "primaryArtists": "Udit Narayan, Sadhana Sargam",
      "primaryArtistsId": "455127, 455324",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Udit Narayan, Sadhana Sargam",
      "starring": "Aamir Khan, Ayesha Jhulka",
      "language": "Hindi",
      "copyright": "©  1992 Saregama",
      "hasLyrics": "true",
      "lyrics": null,
      "releaseDate": "1992-05-22",
      "songUrl": "https://www.jiosaavn.com/song/pehla-nasha/JDBcAiUAbWA",
      "albumUrl": "https://www.jiosaavn.com/album/jo-jeeta-wohi-sikandar/CFif-rUStSc_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/852/Jo-Jeeta-Wohi-Sikandar-Hindi-1992-50x50.jpg",
        "150x150": "https://c.saavncdn.com/852/Jo-Jeeta-Wohi-Sikandar-Hindi-1992-150x150.jpg",
        "500x500": "https://c.saavncdn.com/852/Jo-Jeeta-Wohi-Sikandar-Hindi-1992-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/852/9d335ee08b26f171a3d65e11f8819d52_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/852/9d335ee08b26f171a3d65e11f8819d52_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/852/9d335ee08b26f171a3d65e11f8819d52_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/saregama-albums/MNccah3udrQ_"
    },
    {
      "id": "uzpge8Vj",
      "songName": "O O Jaane Jaana",
      "albumName": "Pyaar Kiya To Darna Kya",
      "albumId": "1043832",
      "playCount": "8633896",
      "duration": "345",
      "label": "",
      "primaryArtists": "Kamaal Khan",
      "primaryArtistsId": "455141",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Kamaal Khan",
      "starring": "",
      "language": "Hindi",
      "copyright": "© 1998 Super Cassettes Industries Private Limited",
      "hasLyrics": "true",
      "lyrics": null,
      "releaseDate": "1998-03-10",
      "songUrl": "https://www.jiosaavn.com/song/o-o-jaane-jaana/BRIbVhEIYVk",
      "albumUrl": "https://www.jiosaavn.com/album/pyaar-kiya-to-darna-kya/m7i93n2FxtE_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/832/Pyaar-Kiya-To-Darna-Kya-1998-50x50.jpg",
        "150x150": "https://c.saavncdn.com/832/Pyaar-Kiya-To-Darna-Kya-1998-150x150.jpg",
        "500x500": "https://c.saavncdn.com/832/Pyaar-Kiya-To-Darna-Kya-1998-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/832/18f1ee631cedaeea614c43ef4f48a3c2_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/832/18f1ee631cedaeea614c43ef4f48a3c2_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/832/18f1ee631cedaeea614c43ef4f48a3c2_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/-albums/6DLuXO3VoTo_"
    },
    {
      "id": "FOn06quY",
      "songName": "Ladki Badi Anjani Hai",
      "albumName": "Kuch Kuch Hota Hai (Original Motion Picture Soundtrack)",
      "albumId": "1035265",
      "playCount": "23709319",
      "duration": "381",
      "label": "Sony Music Entertainment India Pvt. Ltd.",
      "primaryArtists": "Jatin-Lalit, Kumar Sanu, Alka Yagnik",
      "primaryArtistsId": "455534, 455142, 455120",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Jatin-Lalit, Kumar Sanu, Alka Yagnik",
      "starring": "Shah Rukh Khan, Kajol, Rani Mukerji, Salman Khan",
      "language": "Hindi",
      "copyright": "(P) 1998 Sony Music Entertainment India Pvt. Ltd. .",
      "hasLyrics": "false",
      "lyrics": null,
      "releaseDate": "1998-08-19",
      "songUrl": "https://www.jiosaavn.com/song/ladki-badi-anjani-hai/NicFAUJBQmo",
      "albumUrl": "https://www.jiosaavn.com/album/kuch-kuch-hota-hai-original-motion-picture-soundtrack/zvqnBMKjQeM_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/907/Kuch-Kuch-Hota-Hai-Hindi-1998-20190516130035-50x50.jpg",
        "150x150": "https://c.saavncdn.com/907/Kuch-Kuch-Hota-Hai-Hindi-1998-20190516130035-150x150.jpg",
        "500x500": "https://c.saavncdn.com/907/Kuch-Kuch-Hota-Hai-Hindi-1998-20190516130035-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/907/08a005b0d0d1a09b5532b4547b3e9fe3_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/907/08a005b0d0d1a09b5532b4547b3e9fe3_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/907/08a005b0d0d1a09b5532b4547b3e9fe3_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/sony-music-entertainment-india-pvt.-ltd.-albums/LaFAA6h1q2U_"
    },
    {
      "id": "Hr3D2hLT",
      "songName": "Do Dil \r\nMil Rahe Hai",
      "albumName": "Pardes",
      "albumId": "1042394",
      "playCount": "30964642",
      "duration": "400",
      "label": "Tips Music",
      "primaryArtists": "Kumar Sanu",
      "primaryArtistsId": "455142",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "Kumar Sanu",
      "starring": "Shah Rukh Khan, Mahima Chaudhry",
      "language": "Hindi",
      "copyright": "© 1997 Tips Industries Ltd.",
      "hasLyrics": "true",
      "lyrics": null,
      "releaseDate": "1997-08-08",
      "songUrl": "https://www.jiosaavn.com/song/do-dil-mil-rahe-hai/OBpYdUZYe2c",
      "albumUrl": "https://www.jiosaavn.com/album/pardes/aT,ino5A3f8_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/386/Pardes-Hindi-1997-20200116121055-50x50.jpg",
        "150x150": "https://c.saavncdn.com/386/Pardes-Hindi-1997-20200116121055-150x150.jpg",
        "500x500": "https://c.saavncdn.com/386/Pardes-Hindi-1997-20200116121055-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/386/64f60d5bbf97767026dd2f027a1088a3_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/386/64f60d5bbf97767026dd2f027a1088a3_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/386/64f60d5bbf97767026dd2f027a1088a3_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/tips-music-albums/WyMes45YplY_"
    },
    {
      "id": "dV6hFKL0",
      "songName": "Chand Sitare",
      "albumName": "Kaho Naa Pyar Hai",
      "albumId": "1065819",
      "playCount": "10571852",
      "duration": "398",
      "label": "Saregama",
      "primaryArtists": "Kumar Sanu",
      "primaryArtistsId": "455142",
      "featuredArtists": "",
      "featuredArtistsId": "",
      "singers": "",
      "starring": "",
      "language": "Hindi",
      "copyright": "℗ 2000 Saregama India Ltd",
      "hasLyrics": "false",
      "lyrics": null,
      "releaseDate": "2000-01-14",
      "songUrl": "https://www.jiosaavn.com/song/chand-sitare/FD5dWTJ7ewM",
      "albumUrl": "https://www.jiosaavn.com/album/kaho-naa-pyar-hai/Ubn5MgPXop0_",
      "imagesUrls": {
        "50x50": "https://c.saavncdn.com/446/Kaho-Naa-Pyar-Hai-Hindi-2000-20200901153916-50x50.jpg",
        "150x150": "https://c.saavncdn.com/446/Kaho-Naa-Pyar-Hai-Hindi-2000-20200901153916-150x150.jpg",
        "500x500": "https://c.saavncdn.com/446/Kaho-Naa-Pyar-Hai-Hindi-2000-20200901153916-500x500.jpg"
      },
      "audioUrls": {
        "96_KBPS": "https://aac.saavncdn.com/446/bf3ab64cfa250f2e1ba1f2a3c3c9d127_96.mp4",
        "160_KBPS": "https://aac.saavncdn.com/446/bf3ab64cfa250f2e1ba1f2a3c3c9d127_160.mp4",
        "320_KBPS": "https://aac.saavncdn.com/446/bf3ab64cfa250f2e1ba1f2a3c3c9d127_320.mp4"
      },
      "labelUrl": "https://www.jiosaavn.com/label/saregama-albums/MNccah3udrQ_"
    }
  ]
}
```

</details>

## License

MIT License

Copyright (c) 2021 [Vidya Sagar](https://github.com/vidyasagar1432)
