import json
import logging

from model.entity import PreData
import requests

login_url = ''


# get authorization, cookie, x-csrf-token
def login(name, password):
    response = requests.post(login_url, '')
    response.close()

    if response.status_code != 200:
        logging.error("login failed")
        return

    data = json.loads(response.content)
    # TODO build PreData...





    return PreData('', '', '', '')
