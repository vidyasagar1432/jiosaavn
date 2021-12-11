
import aiohttp
import json

from .__useragent import getHeaders


async def getjSON(url:str):
    async with aiohttp.ClientSession(headers=getHeaders()) as session:
        async with session.get(url) as response:
            assert response.status == 200,'ClientResponse 404'
            return json.loads(await response.text())


async def getText(url:str,data=None):
    async with aiohttp.ClientSession(headers=getHeaders()) as session:
        async with session.get(url,data=data) as response:
            assert response.status == 200,'ClientResponse 404'
            return await response.text()


async def getSongId(url:str):
    response = await getText(url,data=[('bitrate', '320')])
    try:
        return response.split('"song":{"type":"')[1].split('","image":')[0].split('"id":"')[-1]
    except IndexError:
        return(response.split('"pid":"'))[1].split('","')[0]


async def getAlbumId(url:str):
    response = await getText(url)
    try:
        return response.split('"album_id":"')[1].split('"')[0]
    except IndexError:
        return response.split('"page_id","')[1].split('","')[0]


async def getPlaylistId(url:str):
    response = await getText(url)
    try:
        return response.split('"type":"playlist","id":"')[1].split('"')[0]
    except IndexError:
        return response.split('"page_id","')[1].split('","')[0]

