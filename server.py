from http.server import SimpleHTTPRequestHandler, HTTPServer

class IndexHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Boro")

def run_server():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, IndexHandler)
    httpd.serve_forever()
                         