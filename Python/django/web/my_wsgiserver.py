from wsgiref.simple_server import make_server

def my_app(environ, start_response):
    status='200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)

    response = [b"This is a sample WSGI Application"]

    return response

if __name__ == '__main__':
    print("Start WSGI Server on port 9090")
    server = make_server('', 9090, my_app)
    server.serve_forever()