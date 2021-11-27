
import aiohttp
import json

from ._useragent import getRandomUserAgent


async def get(url:str):
    async with aiohttp.ClientSession(headers=getRandomUserAgent()) as session:
        async with session.get(url) as response:
            if not response.status == 404:
                return json.loads(await response.text())
            return None


# async def FetchHttpbin():
#     return await get(url='http://httpbin.org/headers')
