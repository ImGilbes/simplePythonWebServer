from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

#openssl req -new -x509 -keyout servkey.pem -out servcert.pem -days 365 -nodes

text_file = open("./indextls.html", "r")
page = text_file.read()
text_file.close()


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

        message = "Credentials received"
        self.wfile.write(bytes(page + message, "utf8"))


# httpd = HTTPServer(('', 8000), handler)

# httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./server.pem', server_side=True)
# # httpd.socket = ssl

httpd = HTTPServer(('', 4443), handler)

#ubuntu version
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    keyfile='./server.key',
    certfile='./server.pem',
    server_side=True,
    ssl_version=ssl.PROTOCOL_TLSv1_2)

# windows version
# httpd.socket = ssl.wrap_socket(
#     httpd.socket,
#     keyfile='.\server.key',
#     certfile='.\server.pem',
#     server_side=True,
#     ssl_version=ssl.PROTOCOL_TLSv1_2)


httpd.serve_forever()