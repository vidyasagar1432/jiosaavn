
import aiohttp


def ucfirst(string:str):
    return string.capitalize()

def makeDifferentQualityMediaUrls(url:str):
    replaced = url.replace("preview.saavncdn.com", "aac.saavncdn.com")
    return {"96_KBPS": replaced.replace("_96_p", "_96"),
            "160_KBPS": replaced.replace("_96_p", "_160"),
            "320_KBPS": replaced.replace("_96_p", "_320"),}

def makeDifferentQualityImages(image:str):
    image = image[:image.rfind('-')] 
    return {"50x50": f'{image}-50x50.jpg',
            "150x150": f'{image}-150x150.jpg',
            "500x500": f'{image}-500x500.jpg',}

async def getsongID(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url,data=[('bitrate', '320')]) as resp:
            res = await resp.text()
            try:
                return res.split('"song":{"type":"')[1].split('","image":')[0].split('"id":"')[-1]
            except IndexError:
                return(res.split('"pid":"'))[1].split('","')[0]

# def generateAPIUrlsFromPids(pids:str):
#     return [f'{APP_URL}/song?id={i}' for i in pids.split(', ')]

