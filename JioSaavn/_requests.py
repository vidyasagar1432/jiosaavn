
import aiohttp
import json

from ._useragent import getHeaders


async def getjSON(url:str):
    async with aiohttp.ClientSession(headers=getHeaders()) as session:
        async with session.get(url) as response:
            if not response.status == 404:
                return json.loads(await response.text())
            return None

async def getText(url:str,data=None):
    async with aiohttp.ClientSession(headers=getHeaders()) as session:
        async with session.get(url,data=data) as response:
            if not response.status == 404:
                return await response.text()
            return None
