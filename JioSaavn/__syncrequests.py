import requests

from .__useragent import getHeaders


def getjSON(url:str):
    response = requests.get(url=url,headers=getHeaders())
    assert response.status_code == 200,'ClientResponse 404'
    return response.json()


def getText(url:str,data=None):
    response = requests.get(url=url,headers=getHeaders(),params=data)
    assert response.status_code == 200,'ClientResponse 404'
    return response.text

