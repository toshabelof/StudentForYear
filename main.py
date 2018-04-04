"""
vk = vk_api.VkApi(token='169428aad53f73252e0b465e1f2f899c10df80e9024e4f80aa8f9783c5d5a860effa0a20292618fa50c54')

token SG 25e4b62e76e29d2f67a26d27bf43046f74654d030dc85a2b9535b63177da5301a82e53d30e9de24caa805
group id 117644300
"""

"""
import requests

group_token = "25e4b62e76e29d2f67a26d27bf43046f74654d030dc85a2b9535b63177da5301a82e53d30e9de24caa805"


def sendMessage(user_id, message):
    response = call_vk_api("messages.send", {'user_id': user_id, 'message': message})
    return response


def getLongPollServer():
    response = call_vk_api('groups.getLongPollServer', {'group_id': 117644300})
    return response


def getLongPollEvents(server, key, ts):
    response = requests.post("%s?act=a_check&key=%s&ts=%s&wait=25" % (server, key, ts))
    return response.json()


def call_vk_api(method, params):
    method = "https://api.vk.com/method/%s" % (method)
    params['access_token'] = group_token
    params['v'] = '5.74'
    response = requests.post(method, params).json()['response']
    return response


params = getLongPollServer()

while (True):
    try:
        result = getLongPollEvents(params['server'], params['key'], params['ts'])

        params['ts'] = result['ts']

        events = result['updates']

        for event in events:
            if event['type'] == 'message_new':
                sendMessage(event['object']['user_id'], "ddd")  # отправка сообщения

        print(result)


    except Exception as e:
        print(e)
"""


# список в словарь
def fileUpdateList(i):
    while True:
       try:
           list.update({file[i]: int(file[i + 1])})
           i += 2
       except:
           break


# Обработка голоса юзера
def update(Golos):
    userTrue = False
    for l in list:
        if Golos == l:
            other = list.get(l) + 1
            list.update({l: other})
            userTrue = True
            break
    if userTrue:
        return True
    else: False


# считываем из файла
with open("list.txt", "r") as f:
    file = f.read().splitlines()
print(file)

list = {}
i = 0
fileUpdateList(i)

# выводим словарь, полученный из файла
print(list)


print('Напиши за кого ты голосуешь!')
golos = input()


# обновляем словарь с учётом нашего голоса
user_golos = update(golos)

if user_golos == True:
    print('Ваш голос принят!')
else:
    print("Увы, такого участника нет :(")

print(list)

# Пишев в файл результаты
with open('list.txt', 'w') as csv_file:
    for item in list:
        csv_file.write("%s\n%s\n" % (item, list.get(item)))


