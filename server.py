from http.server import HTTPServer, BaseHTTPRequestHandler
class simpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello World!')

if __name__ == '__main__':
    httpd = HTTPServer(("localhost", 8000), simpleHTTPRequestHandler)
    print("Server started on localhost:8000")
    httpd.serve_forever()