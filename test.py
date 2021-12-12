import asyncio

from jiosaavn import Async
from jiosaavn import Sync

asyncJioSaavn = Async.JioSaavn()
syncJioSaavn = Sync.JioSaavn()

async def defMain():
    # data = await asyncJioSaavn.song(id='veJXEDz',)
    # data =  await asyncJioSaavn.searchSong('alone')
    # data =  await asyncJioSaavn.searchAlbum('Alone' )
    # data = await asyncJioSaavn.album(id='104d')
    # data =  await asyncJioSaavn.playlist(url='https://www.jiosaavn.com/playlist/88063878238ad9a391a33c0e628d2b01/90s_Love/OykxHSA0YytFo9wdEAzFBA__')
    # data = syncJioSaavn.song(id='veJDA')
    # https://www.jiosaavn.com/song/alone/Bg0haTF0dkk
    # data = syncJioSaavn.song(url='https://www.jiosaavn.com/song/alone/Bg0haT0dkk')
    # data =  syncJioSaavn.searchSong('alone')
    # data = syncJioSaavn.album(id='10sa')
    # data =  syncJioSaavn.searchAlbum('Alone')
    # data =  syncJioSaavn.playlist(url='https://www.jiosaavn.com/playlist/88063878238ad9a391a33c0e628d2b01/90s_Love/OykxHSA0YytFo9wdEAzFBA__')
        
    # print(data)
    return ''

async def main():
    await defMain()



loop = asyncio.get_event_loop()
loop.run_until_complete(main())