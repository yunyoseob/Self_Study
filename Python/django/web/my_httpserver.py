from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHander(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response_only(200, 'OK')
        self.send_header('Content-Type', 'text/plain')
        self.wfile.write(b"Hello World")

if __name__ == '__main__':
    server = HTTPServer(('',8088), MyHander)
    print("Started WebServer on port 8088...")
    print("Press ^C to quit WebServer.")
    server.serve_forever()

# Web Server 띄운 뒤, python -m http.server 8088 명령어를 입력하고, 
# http://localhost:8088을 입력하면 현재 디렉토리 구조를 웹 서버에서 볼 수 있다.