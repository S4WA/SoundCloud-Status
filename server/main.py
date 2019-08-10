import json, datetime, exporter, os, settings, atexit
from http.server import BaseHTTPRequestHandler, HTTPServer
from pypresence import Presence
from urllib.parse import parse_qs
from reset import Reset

atexit.register(Reset)

client_id = settings.RPC().getClientID()
last_request = { "title": "" }

RPC = Presence(client_id)
RPC.connect()
RPC.clear()

class JsonResponseHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		content_len = int(self.headers.get("content-length"))
		requestBody = self.rfile.read(content_len).decode("UTF-8")
		request = parse_qs(requestBody)

		self.send_response(200)
		self.send_header("Content-type", "text/json")
		self.send_header("Access-Control-Allow-Origin", "*")
		self.end_headers()

		global last_request
		if (request != {}):
			request = conv(request)

			if (request["title"] != last_request["title"]):
				print(request["title"], "by", request["artist"])
				if (settings.Export().isEnabled()):
					exporter.write(
						settings.Export().getFormat().replace("$title", request["title"]).replace("$artist", request["artist"])
					)
					if ("50x50" in request["artwork"]):
						exporter.download_file(
							request["artwork"].replace("50x50", "500x500").replace("url(\"", "").replace("\")", ""),
							"artwork.jpg"
						)
					elif (os.path.exists("artwork.jpg")):
						os.remove("artwork.jpg")

			last_request = request

			if (settings.RPC().isEnabled() and request["playing"]):
				RPC.update(
					details = request["title"],
					state = "by " + request["artist"],
					large_image = "icon2",
					large_text = "made by dripnyan"
				)
			else:
				RPC.clear()
		self.wfile.write(json.dumps(request).encode("utf-8"))

	def log_message(self, format, *args):
		return

def CBool(value):
	if isinstance( value, str ) and value.lower() == "false":
		return False
	return bool(value)

def conv(request):
	return { # 雑がすぎる
		"artist": request["artist"][0],
		"title": request["title"][0],
		"playing": CBool(request["playing"][0]),
		# "start_time": int(request["start_time"][0]),
		# "end_time": request["end_time"][0],
		# "current_time": request["current_time"][0],
		"artwork": request["artwork"][0]
	}

try:
	server = HTTPServer(("", 8000), JsonResponseHandler)
	server.serve_forever()
except KeyboardInterrupt:
	Reset()
