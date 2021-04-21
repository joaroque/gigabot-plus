import json
import sqlite3
from os import system
from time import sleep
import requests
from requests.auth import HTTPBasicAuth
from modules.banner import logo, menu
from modules.libs.bootstrapy import Strapy
from modules.utils.get_token import get_token
from modules.utils.get_movid import get_movId
from modules.utils.get_amount import get_amount
from modules.utils.get_questions import get_question
from modules.utils.get_index import get_index_by_json
from modules.utils.get_token_logged import get_token_logged
from modules.utils.get_number_wallet import get_number_wallet
from modules.utils.get_correctanswer import get_correct_answer
from modules.headers import game_header
from modules.headers import answer_header
from modules.headers import player_header

class Gigabot():

	def __init__(self):
		self._session = requests.Session()
		self._main = self._session.get("http://giga.unitel.ao")
		self._main.encoding = 'UTF-8'
		
		self._game_headers = game_header()
		# endpoint: guest
		self._guest = self._session.post("http://giga.unitel.ao/api/player/guest", headers=self._game_headers)
		self._token = get_token(self._guest)
		self._player_headers = player_header(self._token)
		self._answer_headers = answer_header(self._token)
		
		system('clear')

	def time(self,t):
		sleep(t)
	
	def clear_Scr(self, t=None):
		if t:
			sleep(t)
		if system('os') == 'windows':
			system('cls')
		else:
			system('clear')

	def verify_in_db(self,question):
		conn = sqlite3.connect('gigabot.db')
		cursor = conn.cursor()
		query = "SELECT * FROM gigabot WHERE question == '{}'".format(question)
		cursor.execute(query)
		for row in cursor:
			if row is not None:
				return True
			else:
				return False 
		conn.commit()
		conn.close()

	def get_db_conn(self):
		conn = sqlite3.connect('gigabot.db')
		return conn

	def payload_send(self, moveId, index=None):
		if index:
			payload = {
				"moveId":int(moveId),
				"index": index,
				"help":None,
				"time": 10,
				"optional": None
			}
			return payload
		else:
			payload = {
				"moveId":int(moveId),
				"index":-1,
				"help":None,
				"time": 10,
				"optional": None
			}
			return payload
			print(Strapy.BAD+"[ERRO]: resposta errada!"+Strapy.END)

	def save_question(self,question,answer):
		print(Strapy.GOOD+"[SUCESSO]: resposta salva!"+Strapy.END)
		conn = self.get_db_conn()
		cursor = conn.cursor()
		cursor.execute('INSERT INTO gigabot(question,answer) VALUES(?,?)',
					(question, answer))
		conn.commit()
		conn.close()
		print(Strapy.GOOD+"[SUCESSO]: resposta salva!"+Strapy.END)

	def game(self,verification,question,question_req,answer_headers_game):
		if verification is True:
			conn = self.get_db_conn()
			cursor = conn.cursor()
			query = "SELECT answer FROM gigabot WHERE question == '{}'".format(question)
			cursor.execute(query)

			for row in cursor:			
				db_answer = row[0]

			# busca o index da pergunta
			answer_index = get_index_by_json(question_req,db_answer)
			# mostra o saldo actual
			get_amount(question_req)
			
			# SALVA A RESPOSTA SE O INDICE FOR INVÁLIDO
			###############################################
			if answer_index is False:
				
				print(Strapy.BAD+"Indice inválido!"+Strapy.END)
				print(Strapy.GOOD+f"Resposta certa: {db_answer}"+Strapy.END)
				
				# apaga a pergunta de índice inválido
				conn = self.get_db_conn()
				cursor = conn.cursor()
				query = "DELETE FROM gigabot WHERE question == '{}'".format(question)
				cursor.execute(query)
				conn.commit()
				conn.close()

				# responde errado
				moveId = get_movId(question_req)
				payload = self.payload_send(moveId)

				# endpoint: answer
				print(Strapy.GOOD+"[SUCESSO]: resposta salva!"+Strapy.END)
				answer_req = self._session.post("http://giga.unitel.ao/api/game/answer", json=payload, headers=answer_headers_game)
				answer = get_correct_answer(answer_req)			
				
				#self.save_question(question,answer)
				# Error msg

				conn = self.get_db_conn()
				cursor = conn.cursor()
				cursor.execute('INSERT INTO gigabot(question,answer) VALUES(?,?)',
					(question, answer))
				conn.commit()
				conn.close()


			###############################################

			else:
				moveId = get_movId(question_req)
				payload = self.payload_send(moveId, answer_index)
				answer_req = self._session.post("http://giga.unitel.ao/api/game/answer", json=payload, headers=answer_headers_game)
				#print(answer_req.text)


			# Mudar os heads para continuar o loop
			###############################################
			if 'CORRECT_FREE_LIMIT' in answer_req.text:

				self.clear_Scr(2)
				logo()
				print("")
				print(Strapy.BGBLUE+Strapy.UNDERLINE +" menu > treino "+Strapy.END)
				print("=======================================================")
				print(Strapy.RUN+"O bot está a treinar..."+Strapy.END)
				print(Strapy.INFO+"O treino ajuda a salvar perguntas e evitar erros."+Strapy.END)
				print("=======================================================")
				self._game_headers = game_header()
				# endpoint: guest
				self._guest = self._session.post("http://giga.unitel.ao/api/player/guest", headers=self._game_headers)
				self._token = get_token(self._guest)
				self._player_headers = player_header(self._token)
				self._answer_headers = answer_header(self._token)
			#################################################
		else:

			moveId = get_movId(question_req)
			payload = self.payload_send(moveId)
			# endpoint: answer
			answer_req = self._session.post("http://giga.unitel.ao/api/game/answer", json=payload, headers=answer_headers_game)
			answer = get_correct_answer(answer_req)			

			#self.save_question(question,answer)
			
			print(Strapy.GOOD+"[SUCESSO]: resposta salva!"+Strapy.END)
			conn = self.get_db_conn()
			cursor = conn.cursor()
			cursor.execute('INSERT INTO gigabot(question,answer) VALUES(?,?)',
				(question, answer))
			conn.commit()
			conn.close()		
			

	def trainning(self):
		##### Endpoints #####
		
		# endpoint: game
		game = self._session.get("http://giga.unitel.ao/api/game", auth=HTTPBasicAuth(self._token,""), headers=self._game_headers)
		
		# endpoint: player
		player = self._session.get("http://giga.unitel.ao/api/player", headers=self._player_headers)
		
		# endpoint: inbox
		inbox = self._session.get("http://giga.unitel.ao/api/inbox", headers=self._player_headers)

		# endpoint: start
		start = self._session.post("http://giga.unitel.ao/api/game/start", headers=self._player_headers)
	
		# endpoint: question
		question_req = self._session.get("http://giga.unitel.ao/api/game/question", headers=self._player_headers)
		question = get_question(question_req)
		
		if "INVALID_TOKEN" in question_req.text:
			print(Strapy.BAD+"Token inválido"+Strapy.END)
			system('exit')
		# verification section
		verification = self.verify_in_db(question)
		
		# para colocar o cabeçalho correcto 
		answer_headers_game = self._answer_headers
		
		#gamming...
		self.game(verification,question,question_req,answer_headers_game)

	def login(self):
		# Login section && endpoints
		payload = {"msisdn":"","operatorId":391,"pin":0}
	
		login = self._session.post("http://giga.unitel.ao/api/player/login", auth=HTTPBasicAuth(self._token,""), json=payload, headers=self._answer_headers)
	
		#get token e player headers
	
		self.token_logged = get_token_logged(login)
	
		self.player_headers_logged = player_header(self.token_logged)

		self.player_logged = self._session.get("http://giga.unitel.ao/api/player", headers=self.player_headers_logged)
		
		return self.player_logged
	
	def gamming(self):
		# endpoints
		game = self._session.get("http://giga.unitel.ao/api/game", auth=HTTPBasicAuth(self.token_logged,""), headers=self._game_headers)
		
		self._session.get("http://giga.unitel.ao/api/player", headers=self.player_headers_logged)
		
		# endpoint: inbox
		inbox = self._session.get("http://giga.unitel.ao/api/inbox", headers=self.player_headers_logged)
		
		# endpoint: start
		self._session.post("http://giga.unitel.ao/api/game/start", headers=self.player_headers_logged)

		# endpoint: question
		question_req = self._session.get("http://giga.unitel.ao/api/game/question", headers=self.player_headers_logged)
		question = get_question(question_req)
		#print(inbox.text)
		#verification section
		#verification = self.verify_in_db(question)
		
		#gamming...
		#self.game(verification,question,question_req)
		
		if "WITHOUT_GAME" in question_req.text:
			print(Strapy.BAD+"Sem jogo disponível!"+Strapy.END)
			return False
		elif "INVALID_TOKEN" in question_req.text:
			print(Strapy.BAD+"Token inválido!"+Strapy.END)
			return False
		elif "QUESTION_TIMEOUT" in question_req.text:
			print(Strapy.BAD+"Tempo expirado!"+Strapy.END)
			return False
		else:
			print(Strapy.INFO+"Jogando...\n"+Strapy.END)
			print(question)
			
			# verificação
			verification = self.verify_in_db(question)
			
			# para colocar o cabeçalho correcto 
			answer_headers_game = answer_header(self.token_logged)

			# gamming...
			self.game(verification,question,question_req,answer_headers_game)
			return True




	def logout(self):
		logout = self._session.get("http://giga.unitel.ao/", headers=self._game_headers)
		# endpoints
		#player = self._session.get("http://giga.unitel.ao/api/player", headers=self._player_headers)
		#print(player.text)
		return logout.text



def main():
	system('clear')
	print(Strapy.RUN+"Aguarde enquanto o programa conecta..."+Strapy.END)
	gb = Gigabot()
	logo()
	menu()
	
	opt = int(input(">>> "))
	try:
		# TREINAR
		if opt == 1:

			gb.clear_Scr(1)
			logo()
			print("")
			print(Strapy.BGBLUE+Strapy.UNDERLINE +" menu > treino "+Strapy.END)	
			print("=======================================================")
			print(Strapy.RUN+"O bot está a treinar..."+Strapy.END)
			print(Strapy.INFO+"O treino ajuda a salvar perguntas e evitar erros..."+Strapy.END)
			print("=======================================================")
			while True:
				gb.time(1)
				gb.trainning()

		# JOGO NORNAL
		elif opt == 2:
			logo()
			gb.time(1)
			print("\n")
			print(Strapy.BGBLUE+Strapy.UNDERLINE +" menu > jogo "+Strapy.END)
			
			player = gb.login()
			data = get_number_wallet(player)
			number = data[0]
			wallet = data[1]
			print("======================================================")
			print(Strapy.CYAN + "Entrou com: "+Strapy.END + f"{number}")
			print(Strapy.CYAN + "Saldo actual: "+Strapy.END + f"{wallet}")
			print("=======================================================\n")
			
			while True:
				gb.gamming()
			"""
			go = 0
			while go < 14:
				go += 1
				if gb.gamming() is False:
					break
				else:
					gb.gamming()
			"""

			# Terminar sessão
			gb.logout()
			#print(logout)
			print(Strapy.INFO+"Saindo..."+Strapy.END)		
			gb.time(1)
			system('exit')	

		# Preparar jogo
		elif opt == 3:
			logo()
			print("\n")
			print(Strapy.BGBLUE+Strapy.UNDERLINE +" menu > preparar jogo "+Strapy.END)
			print("=======================================================\n")
			go = 0
			while go < 2:
				go += 1
				gb.trainning()
			gb.login()
			
			print(Strapy.INFO+"Tem 3 MB"+Strapy.END)
			print(Strapy.INFO+"Abre 4 terminal e clica em jogo normal :) em cada que jogar basta fechar :v"+Strapy.END)
			print(Strapy.INFO+"Saindo..."+Strapy.END)
			gb.time(1)
			system('exit')

		# JOGO EXTRA
		elif opt == 4:
			logo()
			print("\n")
			print(Strapy.BGBLUE+Strapy.UNDERLINE + " menu > jogo extra "+Strapy.END)
			print("=======================================================")

			bg.one_shot()
		
		# RESGATE
		elif opt == 5:
			logo()
			print("\n")
			print(Strapy.BGBLUE+Strapy.UNDERLINE +" menu > resgate "+Strapy.END)
			print("=======================================================")

			bg.guet_prizze()
		

		# SAIR 
		elif opt == 0:
			print("Saindo...")
			system('exit')
		else:
			system('exit')
		
	except ValueError:
		system('exit')
	

if __name__ == '__main__':
	main()