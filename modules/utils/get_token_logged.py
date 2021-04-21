def get_token_logged(login_res):

# get token from: http://giga.unitel.ao/api/player/login
	token = login_res.text
	alfa = token.find("\"token\":")
	omega = token.find("\"msisdn\":")
	token_logged = token[alfa+9:omega-2]
	return token_logged