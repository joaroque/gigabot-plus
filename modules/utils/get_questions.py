def get_question(question_res):
	question_find = question_res.text
	start = question_find.find('label')
	end = question_find.find('answers')

	question = question_find[start+8:end-3]
	return question

