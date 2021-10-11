import requests
response = requests.get("https://raw.githubusercontent.com/Gamertube583yt/easydspy/main/main.py")

with open('main.py', 'r+') as f:
	f.truncate(0)
	f.write(str(response.content).split('"')[1].split('"')[0].replace(r'\n', '\n').replace(r'\t', '	'))