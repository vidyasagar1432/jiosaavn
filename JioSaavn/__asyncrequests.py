
import aiohttp
import json

from .__useragent import getHeaders


async def getjSON(url:str):
    async with aiohttp.ClientSession(headers=getHeaders()) as session:
        async with session.get(url) as response:
            if response.status == 200:
                return json.loads(await response.text())



async def getText(url:str,data=None):
    async with aiohttp.ClientSession(headers=getHeaders()) as session:
        async with session.get(url,data=data) as response:
            if response.status == 200:
                return await response.text()


