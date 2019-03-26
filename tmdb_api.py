import requests
import json

api_key = 'fe83785c0487b3a9e237fa84b62eef57'

class ServerError(Exception): pass

def getToken(api_key):

    url = "https://api.themoviedb.org/3/authentication/token/new?api_key={}".format(api_key)

    payload = "{}"
    response = requests.request("GET", url, data=payload)
    if not response.ok:
        raise ServerError(response.text)

    response = response.json()
    return response["request_token"]

def getSession(api_key, token):
    url = "https://api.themoviedb.org/3/authentication/session/new?api_key={}".format(api_key)

    payload = {"request_token": token}
    #payload = "{\"request_token\":\"{}\"}".format(token)
    headers = {"content-type": "application/json"}

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

token = getToken(api_key)
getSession(api_key, token)