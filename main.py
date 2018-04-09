import time
import datetime
import random
import json

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

members = []

members.append({'id': 0, 'surname': 'Осюков', 'str': 'Осюков'})

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


# сохраняет голос в файл
def save_vote(user_id, member_id):
	f = open('votes', 'a')
	f.write(json.dumps({'user_id': user_id, 'member_id': member_id, 'date': int(time.time())}) + '\n')
	f.close()


# функция проверяет головал ли пользователь ранее
def is_vote(user_id):
	result = False
	f = open('votes')
	for line in f:
		obj = json.loads(line)
		if obj['user_id'] == user_id:
			result = True
			break
	f.close()
	return result

	f.write(json.dumps({'user_id': user_id, 'member_id': member_id, 'date': time.time()}) + '\n')
	f.close()

# функция парсит сообщение и возвращает id  участника или none
def getMemberByMessage(message):
	message = message.lower()
	for m in members:
		if message.find(m['str'].lower()) != -1:
			return m

	return None





params = getLongPollServer()





while (True):
	try:

		result = getLongPollEvents(params['server'], params['key'], params['ts'])

		params['ts'] = result['ts']

		events = result['updates']

		for event in events:
			if event['type'] == 'message_new':
				user_id = event['object']['user_id']
				body = event['object']['body']

				if (is_vote(user_id)):
					sendMessage(user_id, 'Вы уже головали')
				else:
					member = getMemberByMessage(body)

					if member:
						save_vote(user_id, member['id'])
						sendMessage(user_id, 'Ваш голос принят')

					else:
						sendMessage(user_id, 'Отправьте фамилию участника за которого хотели бы проголовать')

	except Exception as e:
		print(e)
