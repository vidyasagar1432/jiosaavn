
from ._requests import getText

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
