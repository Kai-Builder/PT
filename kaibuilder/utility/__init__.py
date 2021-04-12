import requests


def sizeof(t):
    return len(t)
def getjson(url):
    return requests.get(url).json()

