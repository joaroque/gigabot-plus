def get_token(guest):
	raw_token = guest.text
	alfa = raw_token.find("\"token\":")
	omega = raw_token.find("\"operatorId\":")
	token = raw_token[alfa+9:omega-2]
	return token