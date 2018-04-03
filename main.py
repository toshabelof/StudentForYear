import requests


group_token = "25e4b62e76e29d2f67a26d27bf43046f74654d030dc85a2b9535b63177da5301a82e53d30e9de24caa805"




def sendMessage(user_id, message):
	response = call_vk_api("messages.send", {'user_id': user_id, 'message':message})
	return response

def getLongPollServer():
	response = call_vk_api('groups.getLongPollServer', {'group_id':117644300})
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
				sendMessage(event['object']['user_id'], "ddd")

		print(result)
	except Exception as e:
		print(e)
		

