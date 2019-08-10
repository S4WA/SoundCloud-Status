import urllib.error, urllib.request

def write(text):
	f = open("export.txt", "w", encoding = "utf-8")
	f.write(text)
	f.close()

def download_file(url, name):
	try:
		with urllib.request.urlopen(url) as web_file:
			data = web_file.read()
			with open(name, mode = "wb") as local_file:
				local_file.write(data)
	except urllib.error.URLError as e:
		print(e)
