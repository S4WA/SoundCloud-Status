import configparser

inifile = configparser.ConfigParser()
inifile.read("./config.ini", "UTF-8")

class Export():
	def isEnabled(self):
		return inifile.getboolean("export", "enable")

	def getFormat(self):
		return inifile.get("export", "format")

class RPC():
	def isEnabled(self):
		return inifile.getboolean("rpc", "enable")

	def getClientID(self):
		return int(inifile.get("rpc", "client_id"))
