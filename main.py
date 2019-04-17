import time
import json
import requests

members = []


members.append({'id': 0, 'surname': 'Тенигина', 'str': 'Тенигин'})
members.append({'id': 1, 'surname': 'Сушинский', 'str': 'Сушинск'})
members.append({'id': 2, 'surname': 'Соболев', 'str': 'Соболев'})
members.append({'id': 3, 'surname': 'Сафаров', 'str': 'Сафаров'})
members.append({'id': 4, 'surname': 'Савинов', 'str': 'Савинов'})
members.append({'id': 5, 'surname': 'Мазурова', 'str': 'Мазуров'})
members.append({'id': 6, 'surname': 'Иванова Е', 'str': 'Иванова E'})
members.append({'id': 7, 'surname': 'Иванова М', 'str': 'Иванова М'})
members.append({'id': 8, 'surname': 'Григорьев', 'str': 'Григорьев'})
members.append({'id': 9, 'surname': 'Боиштяну', 'str': 'Боиштяну'})


group_token = "25e4b62e76e29d2f67a26d27bf43046f74654d030dc85a2b9535b63177da5301a82e53d30e9de24caa805"


def sendMessage(user_id, message):
	response = call_vk_api("messages.send", {'user_id': user_id, 'message': message})
	return response


def getLongPollServer():
	response = call_vk_api('groups.getLongPollServer', {'group_id': 117644300})
	return response


def getLongPollEvents(server, key, ts):
	response = requests.post("%s?act=a_check&key=%s&ts=%s&wait=25" % (server, key, ts))
	print(response)
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


def getSurnameById(member_id):
	result = None
	f = open('votes')
	for m in members:
		if m['id'] == member_id:
			result = m['surname']
			break
	f.close()
	return result


# функция парсит сообщение и возвращает id  участника или none
def getMemberByMessage(message):
	message = message.lower()
	for m in members:
		if message.find(m['str'].lower()) != -1:
			return m


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

	return str


params = getLongPollServer()

while (True):

	try:

		result = getLongPollEvents(params['server'], params['key'], params['ts'])

		if 'failed' in result and result['failed'] == 2:
			res = getLongPollServer()
			params['key'] = res['key']

		elif 'failed' in result and result['failed'] == 3:
			res = getLongPollServer()
			params['key'] = res['key']
			params['ts'] = res['ts']

		else:
			params['ts'] = result['ts']
			events = result['updates']

			for event in events:
				if event['type'] == 'message_new':
					user_id = event['object']['user_id']
					body = event['object']['body']

					if (body == 'result'):
						result = calculate()
						sendMessage(user_id, result)
					elif (is_vote(user_id)):
						sendMessage(user_id, 'Вы уже проголосовали.')
					else:
						member = getMemberByMessage(body)

						if member:
							save_vote(user_id, member['id'])
							sendMessage(user_id, 'Ваш голос принят!')
						else:
							sendMessage(user_id, 'Отправьте фамилию участника за которого хотели бы проголовать:\nОльга Боднарюк\nАндрей Бутурлакин\nНаталия Дробинина\nЛада Киселёва\nЕвгений Левичев\nСтепан Марков\nАнастасия Удалова\nЭльвира Шумилова')

	except Exception as e:
		# params = getLongPollServer()
		print(e)
