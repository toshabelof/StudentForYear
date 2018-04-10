import time
import datetime
import random
import json

import requests

members = []

members.append({'id': 0, 'surname': 'Удалова', 'str': 'Удалов'})
members.append({'id': 1, 'surname': 'Дробинина', 'str': 'Дробинин'})
members.append({'id': 2, 'surname': 'Марков', 'str': 'Марков'})
members.append({'id': 3, 'surname': 'Бутурлакин', 'str': 'Бутурлакин'})
members.append({'id': 4, 'surname': 'Левичев', 'str': 'Левиче'})
members.append({'id': 5, 'surname': 'Шумилова', 'str': 'Шумилов'})
members.append({'id': 6, 'surname': 'Боднарюк', 'str': 'Боднарюк'})
members.append({'id': 7, 'surname': 'Киселёва', 'str': 'Киселёв'})

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
<<<<<<< HEAD
    return result


# функция парсит сообщение и возвращает id  участника или none
def getMemberByMessage(message):
    message = message.lower()
    for m in members:
        if message.find(m['str'].lower()) != -1:
            return m
=======
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
>>>>>>> b0ac09f60e18356ba2ec709a2719bfea5821fa91

    return None

<<<<<<< HEAD
=======
def sendMessage(user_id, message):
	response = call_vk_api("messages.send", {'user_id': user_id, 'message': message})
	return response
>>>>>>> b0ac09f60e18356ba2ec709a2719bfea5821fa91

def getSurnameById(member_id):
    result = None
    f = open('votes')
    for m in members:
        if m['id'] == member_id:
            result = m['surname']
            break
    f.close()
    return result

<<<<<<< HEAD
=======
def getLongPollServer():
	response = call_vk_api('groups.getLongPollServer', {'group_id': 117644300})
	return response
>>>>>>> b0ac09f60e18356ba2ec709a2719bfea5821fa91

params = getLongPollServer()

<<<<<<< HEAD
=======
def getLongPollEvents(server, key, ts):
	response = requests.post("%s?act=a_check&key=%s&ts=%s&wait=25" % (server, key, ts))
	return response.json()
>>>>>>> b0ac09f60e18356ba2ec709a2719bfea5821fa91

def calculate():
    str = ""
    map = dict()

<<<<<<< HEAD
    f = open('votes')
    for line in f:
        obj = json.loads(line)

        member_id = obj['member_id']
=======
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


# функция парсит сообщение и возвращает id  участника или none
def getMemberByMessage(message):
	message = message.lower()
	for m in members:
		if message.find(m['str'].lower()) != -1:
			return m

	return None

def getSurnameById(member_id):
	result = None
	f = open('votes')
	for m in members:
		if m['id'] == member_id:
			result = m['surname']
			break
	f.close()
	return result
>>>>>>> b0ac09f60e18356ba2ec709a2719bfea5821fa91

        if not member_id in map:
            map[member_id] = []

<<<<<<< HEAD
        map[member_id].append(obj)

    for key, value in map.items():
        str += "%s : %d \n" % (getSurnameById(key), len(value))

    return str
=======
def calculate():
	str = ""
	map = dict()

	f = open('votes')
	for line in f:
		obj = json.loads(line)

		member_id = obj['member_id']

		if not member_id in map:
			map[member_id] = []

		map[member_id].append(obj)

	for key, value in map.items():
		str += "%s : %d \n" % (getSurnameById(key), len(value))
>>>>>>> b0ac09f60e18356ba2ec709a2719bfea5821fa91

	return str

while (True):
<<<<<<< HEAD
    try:

        result = getLongPollEvents(params['server'], params['key'], params['ts'])
=======
	try:

		result = getLongPollEvents(params['server'], params['key'], params['ts'])

		params['ts'] = result['ts']

		events = result['updates']
>>>>>>> b0ac09f60e18356ba2ec709a2719bfea5821fa91

		for event in events:
			if event['type'] == 'message_new':
				user_id = event['object']['user_id']
				body = event['object']['body']

				if(body == 'result'):
					result = calculate()
					sendMessage(user_id, result)
				elif (is_vote(user_id)):
					sendMessage(user_id, 'Вы уже головали')
				else:
					member = getMemberByMessage(body)

<<<<<<< HEAD
        for event in events:
            if event['type'] == 'message_new':
                user_id = event['object']['user_id']
                body = event['object']['body']

                if (body == 'result'):
                    result = calculate()
                    sendMessage(user_id, result)
                elif (is_vote(user_id)):
                    sendMessage(user_id, 'Вы уже головали.')
                else:
                    member = getMemberByMessage(body)

                    if member:
                        save_vote(user_id, member['id'])
                        sendMessage(user_id, 'Ваш голос принят!')

                    else:
                        sendMessage(user_id, 'Отправьте фамилию участника за которого хотели бы проголовать.')

    except Exception as e:
        print(e)
=======
					if member:
						save_vote(user_id, member['id'])
						sendMessage(user_id, 'Ваш голос принят')

					else:
						sendMessage(user_id, 'Отправьте фамилию участника за которого хотели бы проголовать')

	except Exception as e:
		print(e)
>>>>>>> b0ac09f60e18356ba2ec709a2719bfea5821fa91
