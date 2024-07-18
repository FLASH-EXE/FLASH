import os, platform, time, sys
os.system('xdg-open https://chat.whatsapp.com/He0dyho5y0NLO1d0O4G5WP')
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")

print(' \u001b[37m\x1b[38;5;196m>> \033[1;97mChecking For Update...')
os.system('git pull --quiet ')
bit = platform.architecture()[0]
if bit == "64bit":
 print( '\u001b[37m\x1b[38;5;196m>>\033[1;97m64Bit Found')
 from flash import login
 login()
 
 
 
if bit == "32bit":
 print( '\u001b[37m\x1b[38;5;196m>> \033[1;97m32Bit Found')
 from flash import login
 login()
