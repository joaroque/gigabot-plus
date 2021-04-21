import json
def get_index_by_json(response,db_answer):

	response = response.text 

	#data = json.dumps(response)
	parse = json.loads(response)

	answers = parse.get('responseData').get('answers')

	index_0 = answers[0]
	index_1 = answers[1]
	index_2 = answers[2]
	index_3 = answers[3]

	if db_answer in index_0['label']:
		return index_0['index']
	elif db_answer in index_1['label']:
		return index_1['index']
	elif db_answer in index_2['label']:
		return index_2['index']
	elif db_answer in index_3['label']:
		return index_3['index']
	else:
		return False
