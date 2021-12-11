import requests

from .__useragent import getHeaders


def getjSON(url:str):
    response = requests.get(url=url,headers=getHeaders()).json()
    assert response.status == 200,'ClientResponse 404'
    return response


def getText(url:str,data=None):
    response = requests.get(url=url,headers=getHeaders(),params=data).text
    assert response.status == 200,'ClientResponse 404'
    return response


def getSongId(url:str):
    response = getText(url,data=[('bitrate', '320')])
    try:
        return response.split('"song":{"type":"')[1].split('","image":')[0].split('"id":"')[-1]
    except IndexError:
        return(response.split('"pid":"'))[1].split('","')[0]


def getAlbumId(url:str):
    response = getText(url)
    try:
        return response.split('"album_id":"')[1].split('"')[0]
    except IndexError:
        return response.split('"page_id","')[1].split('","')[0]


def getPlaylistId(url:str):
    response = getText(url)
    try:
        return response.split('"type":"playlist","id":"')[1].split('"')[0]
    except IndexError:
        return response.split('"page_id","')[1].split('","')[0]

