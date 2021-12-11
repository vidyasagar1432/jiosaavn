import asyncio

from JioSaavn.Async import JioSaavn

jiosaavn = JioSaavn()

async def defMain():
    # with print_durations('to call defMain'):
        # data = await jiosaavn.song(id='veJXEDAz',)#response='raw')
        # data =  await jiosaavn.searchSong('alone', )
        # data =  await jiosaavn.searchAlbum('Alone',response='raw' )
        data =  await jiosaavn.playlist(url='https://www.jiosaavn.com/s/playlist/88063878238ad9a391a33c0e628d2b01/90s_Love/OykxHSA0YytFo9wdEAzFBA__')
        
        print(data)

async def main():
    await defMain()
    # print(Response)



loop = asyncio.get_event_loop()
loop.run_until_complete(main())