
def ucfirst(string:str):
    if string:
        return string.capitalize()

def makeDifferentQualityMediaUrls(url:str):
    if url:
        replaced = url.replace("preview.saavncdn.com", "aac.saavncdn.com")
        return {"96_KBPS": replaced.replace("_96_p", "_96"),
                "160_KBPS": replaced.replace("_96_p", "_160"),
                "320_KBPS": replaced.replace("_96_p", "_320"),}

def makeDifferentQualityImages(image:str):
    if image:
        image = image[:image.rfind('-')] 
        return {"50x50": f'{image}-50x50.jpg',
                "150x150": f'{image}-150x150.jpg',
                "500x500": f'{image}-500x500.jpg',}


def getSongId(response:str):
    try:
        try:
            return response.split('"song":{"type":"')[1].split('","image":')[0].split('"id":"')[-1]
        except IndexError:
            return(response.split('"pid":"'))[1].split('","')[0]
    except:
        return None


def getAlbumId(response:str):
    try:
        try:
            return response.split('"album_id":"')[1].split('"')[0]
        except IndexError:
            return response.split('"page_id","')[1].split('","')[0]
    except:
        return None


def getPlaylistId(response:str):
    try:
        try:
            return response.split('"type":"playlist","id":"')[1].split('"')[0]
        except IndexError:
            return response.split('"page_id","')[1].split('","')[0]
    except:
        return None

