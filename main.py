import vk_api
import time
import requests

"""
vk = vk_api.VkApi(token='169428aad53f73252e0b465e1f2f899c10df80e9024e4f80aa8f9783c5d5a860effa0a20292618fa50c54')
vk._auth_token()

values = {'out': 0, 'count': 100, 'time_offset': 60}


def write_message(user_id, text):
    vk.method('messages.send', {'user_id': user_id, 'message': text})

while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
        write_message(item['user_id'], 'Привет, кем бы ты не был :)')
        time.sleep(1)

"""


def getUser(url, data=None):
    request = requests.get(url, params=data)
    response = request.json()
    return response


response = getUser("https://api.vk.com/method/users.get", {'user_id': '47433761', 'v': '5.74'})
print(response)


def getLongPollServer(url, data=None):
    request = requests.get(url, params=data)
    response = request.json()
    return response

response = getUser("https://api.vk.com/method/groups.getLongPollServer", {'group_id': '117644300'})
print(response)