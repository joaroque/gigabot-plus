from .libs.bootstrapy import Strapy
def logo():
	logo = Strapy.BOLD + """
  ______   __                      _______               __
 /      \ /  |                    /       \             /  |
/$$$$$$  |$$/   ______    ______  $$$$$$$  |  ______   _$$ |_
$$ | _$$/ /  | /      \  /      \ $$ |__$$ | /      \ / $$   |
$$ |/    |$$ |/$$$$$$  | $$$$$$  |$$    $$< /$$$$$$  |$$$$$$/
$$ |$$$$ |$$ |$$ |  $$ | /    $$ |$$$$$$$  |$$ |  $$ |  $$ | __
$$ \__$$ |$$ |$$ \__$$ |/$$$$$$$ |$$ |__$$ |$$ \__$$ |  $$ |/  |
$$    $$/ $$ |$$    $$ |$$    $$ |$$    $$/ $$    $$/   $$  $$/
 $$$$$$/  $$/  $$$$$$$ | $$$$$$$/ $$$$$$$/   $$$$$$/     $$$$/
              /  \__$$ | """+ Strapy.WHITE +"""Gigas sem limite | v.0.0.2"""+ Strapy.END+ """ 
              $$    $$/
               $$$$$$/  

"""+Strapy.BGCYAN + Strapy.BOLD + """ Created by """+Strapy.END+""" ~ @joaroque ||  """+Strapy.BGCYAN + Strapy.BOLD+ """ Props to """+Strapy.END+""" ~ @renetexeira""" + Strapy.END
	print(logo)
def menu():
	menu = Strapy.WHITE + Strapy.BOLD + """
	[1] ~ Treinar
	[2] ~ Jogar
	[3] ~ Preparar [3MB]
	[4] ~ Jogo extra
	[5] ~ Resgatar
	[0] ~ Sair

	""" + Strapy.END

	print(menu)