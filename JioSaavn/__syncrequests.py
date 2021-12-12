import requests

from .__useragent import getHeaders


def getjSON(url:str):
    response = requests.get(url=url,headers=getHeaders())
    if response.status_code == 200:
        return response.json()


def getText(url:str,data=None):
    response = requests.get(url=url,headers=getHeaders(),params=data)
    if response.status_code == 200:
        return response.text

