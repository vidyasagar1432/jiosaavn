
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


