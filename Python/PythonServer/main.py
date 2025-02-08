from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            with open(self.path[1:], encoding='utf-8') as file:
                file_to_open = file.read()
                self.send_response(200)

        except FileNotFoundError:
            file_to_open = "File not found"
            self.send_response(404)
    
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('192.168.0.115', 3500), Serv)
print('Done!')
httpd.serve_forever()