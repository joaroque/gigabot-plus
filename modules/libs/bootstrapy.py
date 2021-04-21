###############################################
#                                             # 
#                                             #
#  Bootstrapy is a tool for colored terminal  #
#                                             #
#  author: Joa Roque                          #
#  twitter: catumua_                          #
#  github: joaroque                           #
#  email: haguacomh@gmail.com                 #
#                                             #
#                                             # 
###############################################
import ctypes
import platform
import random


if platform.system() == 'Windows':
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

class Strapy:
    #COLORS
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    GREY = '\033[37m'    
    YELLOW = '\033[93m'
    WHITE = '\033[97m'
    LRED = '\033[91m'
    LGREEN = '\033[92m'
    LBLUE = '\033[94m'
    LPURPLE = '\033[95m'
    LCYAN = '\033[96m'
    
    #BACKGROUNDS
    BGBLACK = '\033[40m' 
    BGRED = '\033[41m'
    BGGREEN = '\033[42m'
    BGORANGE = '\033[43m'
    BGBLUE = '\033[44m'
    BGPURPLE = '\033[45m'
    BGCYAN = '\033[46m'
    BGGRAY = '\033[47m'
    
    #STYLES
    BOLD = '\033[1m' 
    LIGHT = '\033[2m' 
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'  
    PISCA = '\033[5m' 
    INVERTED = '\033[7m' 
    STRIKE = '\033[9m' 
    
    #LABLES
    INFO = '\033[33m' + '[!] '
    QUE = '\033[34m' + '[?] '
    BAD = '\033[31m' + '[-] '
    GOOD = '\033[32m' + '[+] '
    RUN = '\033[97m' + '[~] '
    
    
    #END
    END = '\033[0m'
