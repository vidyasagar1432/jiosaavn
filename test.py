# import asyncio

# from jiosaavn import Async
# from jiosaavn import Sync

# asyncJioSaavn = Async.JioSaavn()
# syncJioSaavn = Sync.JioSaavn()

async def defMain():
    # data = await asyncJioSaavn.song(id='veJXEDz',)
    # data =  await asyncJioSaavn.searchSong('alone')
    # data =  await asyncJioSaavn.searchAlbum('Alone' )
    # data = await asyncJioSaavn.album(url='https://www.jiosaavn.com/album/Vm5jaOSkM7E_')
    # data =  await asyncJioSaavn.playlist(url='https://www.jiosaavn.com/playlist/88063878238ad9a391a33c0e628d2b01/90s_Love/OykxHSA0YytFo9wdEAzFBA__')
    # data = syncJioSaavn.song(id='veJDA')
    # https://www.jiosaavn.com/song/alone/Bg0haTF0dkk
    # data = syncJioSaavn.song(url='https://www.jiosaavn.com/song/alone/Bg0haT0dkk')
    # data =  syncJioSaavn.searchSong('alone')
    # data = syncJioSaavn.album(id='awdawdawd')
    # data =  syncJioSaavn.searchAlbum('Alone')
    # data =  syncJioSaavn.playlist(url='https://www.jiosaavn.com/playlist/88063878238ad9a391a33c0e628d2b01/90s_Love/OykxHSA0YytFo9wdEAzFBA__')
    # data =  syncJioSaavn.playlist(id='nhhbkhbfdwsdawdawd')
        # 
    # print(data)
    return ''



# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

import requests
import random

# data = open('core/user-agents.txt').read().splitlines()
data = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        ]


def getHeaders():
    return {
        'Host': 'www.jiosaavn.com',
        'accept': 'application/json, text/plain, */*',
        'user-agent': random.choice(data),
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9'
        }

def getjSON(url:str):
    response = requests.get(url=url,headers=getHeaders())
    if response.status_code == 200:
        return response.json()

def songsearchFromSTRING(query:str,p:int=1,n:int=5):
    return f'https://www.jiosaavn.com/api.php?p={p}&_format=json&_marker=0&api_version=4&ctx=wap6dot0&n={n}&__call=search.getResults&q={"+".join(query.split(" "))}&year=2022'
data = getjSON(url='https://www.jiosaavn.com/api.php?p=1&q=love&_format=json&_marker=0&api_version=4&ctx=web6dot0&n=20&__call=search.getResults')
total = data['total']
print(total)
result = data['results']
for song in result:
    print(song['year'])


