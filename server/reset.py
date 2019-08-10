import os

class Reset():
	def __init__(self):
		files = ["artwork.jpg", "export.txt"]
		for name in files:
			if (os.path.exists(name)): os.remove(name)
