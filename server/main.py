import sys, json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pypresence import Presence
from urllib.parse import parse_qs

client_id = "607560852228407326"
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

		if (request != {}):
			request = { "artist": request["artist"][0], "title": request["title"][0], "playing": CBool(request["playing"][0]) } # 雑がすぎる
			# print(request)
			if (request["playing"]):
				RPC.update(state = "by " + request["artist"], details = request["title"], large_image = "icon", large_text = "made by dripnyan")
			else:
				RPC.clear()

		self.wfile.write(json.dumps({}).encode("utf-8"))

def CBool( value ):
	if isinstance( value, str ) and value.lower() == "false":
		return False
	return bool( value )

server = HTTPServer(("", 8000), JsonResponseHandler)
server.serve_forever()
