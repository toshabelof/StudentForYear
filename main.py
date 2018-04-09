import datetime
import random

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

user_id = random.randint(1, 10)
print("Твой ID: " + str(user_id))


# список в словарь
def fileUpdateList(i):
    while True:
        try:
            listStudent.update({file[i]: int(file[i + 1])})
            i += 2
        except:
            break


def newUserID(user_id):
    userID_odl = False
    for l in listUser_id:
        if user_id == int(l):
            userID_odl = True
            break
    if userID_odl:
        return True
    else:
        return False


# Обработка голоса юзера
def update(Golos):
    for l in listStudent:
        if Golos == l:
            if newUserID(user_id) == False:
                listUser_id.append(str(user_id))
                other = listStudent.get(l) + 1
                listStudent.update({l: other})

                # Пишев в файл результаты
                with open('list.txt', 'w') as csv_file:
                    for item in listStudent:
                        csv_file.write("%s\n%s\n" % (item, listStudent.get(item)))
                    f.close()

                with open('user_id.txt', 'w') as csv_file:
                    for item in listUser_id:
                        csv_file.write("%s\n" % (item))
                    f.close()
                return True
                break
            else:
                print('Вы уже голосовали!!')
                break
    return False


# считываем из файла
with open("list.txt", "r") as f:
    file = f.read().splitlines()
    f.close()

listStudent = {}
i = 0
fileUpdateList(i)
print(listStudent)

with open("user_id.txt", "r") as f:
    listUser_id = f.read().splitlines()
    f.close()
print(listUser_id)

print('Напиши за кого ты голосуешь!')
golos = input()

# обновляем словарь с учётом нашего голоса
user_golos = update(golos)
if user_golos:
    print('Ваш голос принят!')
else:
    print("Увы, такого участника нет :(")

print(listStudent)
print(listUser_id)
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


# список в словарь
def fileUpdateList(i):
    while True:
        try:
            listStudent.update({file[i]: int(file[i + 1])})
            i += 2
        except:
            break


def newUserID(user_id):
    userID_odl = False
    for l in listUser_id:
        if user_id == int(l):
            userID_odl = True
            break
    if userID_odl:
        return True
    else:
        return False

other_bot = ''

# Обработка голоса юзера
def update(Golos):
    global other_bot
    for l in listStudent:
        if Golos == l:
            if newUserID(event['object']['user_id']) == False:
                listUser_id.append(str(event['object']['user_id']))
                other = listStudent.get(l) + 1
                listStudent.update({l: other})

                # Пишев в файл результаты
                with open('list.txt', 'w') as csv_file:
                    for item in listStudent:
                        csv_file.write("%s\n%s\n" % (item, listStudent.get(item)))
                    f.close()

                with open('user_id.txt', 'w') as csv_file:
                    for item in listUser_id:
                        csv_file.write("%s\n" % (item))
                    f.close()

                sendMessage(event['object']['user_id'], "Ваш голос принят!!")  # отправка сообщения
                other_bot = 'Ваш голос принят!'
                return True
                break
            else:
                sendMessage(event['object']['user_id'], "Вы уже голосовали!!")  # отправка сообщения
                other_bot = 'Вы уже голосовали!!'
                return True
                break
    return False



while (True):
    try:
        # считываем из файла
        with open("list.txt", "r") as f:
            file = f.read().splitlines()
            f.close()

        listStudent = {}
        i = 0
        fileUpdateList(i)
        print(listStudent)

        with open("user_id.txt", "r") as f:
            listUser_id = f.read().splitlines()
            f.close()
        print(listUser_id)

        result = getLongPollEvents(params['server'], params['key'], params['ts'])
        if str(result['updates']) == '':
            break

        params['ts'] = result['ts']

        events = result['updates']

        for event in events:
            if event['type'] == 'message_new':
                if str(event['object']['body']).lower() == "привет":
                    sendMessage(event['object']['user_id'], "Привет! Твоя задача написать мне фамилию того студента, который по твоему мнению заслуживает приз зрительских симпатий:\n"+
                                                            "1. Павел Табунов\n" +
                                                            "2. Никита Иванов\n" +
                                                            "3. Дарья Филатьева\n" +
                                                            "4. Екатерина Блинова")
                    print('\n' + str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')) + ' Пишет: ' + str(event['object']['user_id']) + ' "' + str(event['object']['body']) + '"\n')

                else:
                    user_golos = update(event['object']['body'])

                    if user_golos != True:
                        sendMessage(event['object']['user_id'], "Увы, такого участника нет!!")  # отправка сообщения
                        other_bot = "Увы, такого участника нет!!"

                    print('\n' + str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')) + ' Проголосовал: ' + str(event['object']['user_id']) + ' за '
                              + str( event['object']['body']) + '. Бот ответил: "' + other_bot + '"\n')

    except Exception as e:
        print(e)


