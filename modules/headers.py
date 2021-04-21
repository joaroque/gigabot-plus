import random

r = random.randrange(10,99)
device_Id = f"377e{r}21-db19-{r}98-b5d5-648b{r}9{r}3f8"
# Request headers for endpoint: http://giga.unitel.ao/api/game
def game_header():
	game_headers = {
	"apikey": "547324fb-004c-40f4-b0bd-30d034b91a27",
	"device-Id": f"{device_Id}"
	}
	return game_headers

# Request headers for endpoint: http://giga.unitel.ao/api/game/answer
def answer_header(token):
	answer_headers = {
		"token": "{}".format(token),
		"apikey": "547324fb-004c-40f4-b0bd-30d034b91a27",
		"device-Id": f"{device_Id}",
		"Accept": "application/json, text/plain, */*",
		"Content-Type": "application/json;charset=UTF-8"
	}
	return answer_headers

# Request headers for endpoint: http://giga.unitel.ao/api/player
def player_header(token):
	player_headers = {
		"token": "{}".format(token),
		"apikey": "547324fb-004c-40f4-b0bd-30d034b91a27",
		"device-Id": f"{device_Id}"
	}
	return player_headers

