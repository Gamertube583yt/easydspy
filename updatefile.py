import urllib
import os
import stat
import requests

class File:
	def __init__(self):
		path = 'main.py'
		url_ = "https://github.com/Gamertube583yt/easydspy/blob/main/main.py"
		url = "https://raw.githubusercontent.com/Gamertube583yt/easydspy/main/main.py"
		
		try:
			os.chmod(path, stat.S_IWRITE )
			os.unlink(path)
			os.remove(path)
			print('File deleted!')
		except:
			pass
		
		r = requests.get(url, allow_redirects=True)
		open(path, 'wb').write(r.content)
