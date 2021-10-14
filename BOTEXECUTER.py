from main import *
from updatefile import *

uf = File()
m = Main(log = True)
with open('bot.py') as f:
	exec(f.read())
