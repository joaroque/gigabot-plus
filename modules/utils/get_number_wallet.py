import json

def get_number_wallet(response):
	p = response.text
	#response = response.text 

	#data = json.dumps(p)
	parse = json.loads(p)

	number = parse.get('responseData').get('msisdn')
	saldo = parse.get('responseData').get('wallet').get('counters')[3]['label']

	return [number,saldo]

