def get_correct_answer(answer_res):
	answer_res.encoding = 'UTF-8'
	answer = answer_res.text
	answer_start = answer.find("\"correctAnswer\":")
	answer_end = answer.find("\"isHiddenOnHelp\"")
	correct_answer = answer[answer_start+36:answer_end-2]
	return correct_answer
