import sys, json, datetime, exporter
from http.server import BaseHTTPRequestHandler, HTTPServer
from pypresence import Presence
from urllib.parse import parse_qs

client_id = "607560852228407326"
export_to_file = True
text_format = "$title by $artist"
last_request = {"title": ""}

RPC = Presence(client_id)
RPC.connect()

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
		if (request != {} and request["title"][0] != last_request["title"]):
			last_request = request = { # 雑がすぎる
				"artist": request["artist"][0],
				"title": request["title"][0],
				"playing": CBool(request["playing"][0]),
				# "start_time": int(request["start_time"][0]),
				# "end_time": request["end_time"][0],
				# "current_time": request["current_time"][0],
				"artwork": request["artwork"][0]
			}

			print(request)

			if (export_to_file):
				exporter.write(text_format.replace("$title", request["title"]).replace("$artist", request["artist"]) )
				if ("50x50" in request["artwork"]):
					exporter.download_file(request["artwork"].replace("50x50", "500x500").replace("url(\"", "").replace("\")", ""))

			if (request["playing"]):
				RPC.update(
					details = request["title"],
					state = "by " + request["artist"],
					large_image = "icon2",
					large_text = "made by dripnyan",
					pid = 10
				)
			else:
				RPC.clear()

		self.wfile.write(json.dumps(request).encode("utf-8"))

def CBool(value):
	if isinstance( value, str ) and value.lower() == "false":
		return False
	return bool(value)

server = HTTPServer(("", 8000), JsonResponseHandler)
server.serve_forever()
