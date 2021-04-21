def get_movId(question_res):
	moveId_finder = question_res.text
	movstart = moveId_finder.find('moveId')
	movend = moveId_finder.find('stageIndex')
	moveId = moveId_finder[movstart+8:movend-2]
	return moveId