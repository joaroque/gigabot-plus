def get_amount(question_req):

		res = question_req.text
		start = res.find('\"amount\":')
		end = res.find('MB"}')
		amount = res[start+20:end+2]
		if len(amount) > 5:
			amount = res[start+21:end+2]

		print(f"[{amount}]")