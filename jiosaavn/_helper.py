

def capitalize(string:str):
    if string:
        return string.capitalize()

def makeDifferentQualityMediaUrls(url:str):
    if url:
        replaced = url.replace("preview.saavncdn.com", "aac.saavncdn.com")
        return {"96_KBPS": replaced.replace("_96_p", "_96"),
                "160_KBPS": replaced.replace("_96_p", "_160"),
                "320_KBPS": replaced.replace("_96_p", "_320"),}

def makeDifferentQualityImages(image:str,sep:str):
    if image:
        image = image[:image.rfind(sep)] 
        return {"50x50": f'{image}{sep}50x50.jpg',
                "150x150": f'{image}{sep}150x150.jpg',
                "500x500": f'{image}{sep}500x500.jpg',}

