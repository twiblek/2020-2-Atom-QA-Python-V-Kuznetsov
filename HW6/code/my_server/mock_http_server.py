import json
import threading
import secrets

from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer


class MockHandleRequests(BaseHTTPRequestHandler):
    data = None
    users = ['Test', 'User', 'Admin']
    tokens = {}

    def _set_headers(self):
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path == '/timeout':
            sleep(4)

        elif self.path == '/test_error':
            self.send_response(501)
            self._set_headers()

        elif self.path == '/auth':
            login = self.headers['Authorization']

            if str(login) in self.users:
                user_token = str(secrets.token_hex(16))
                self.tokens[str(login)] = user_token
                self.send_response(200)
                self.send_header('Authorization', f'{login}')
                self.data = json.dumps({'Token': '{}'.format(user_token)}).encode()
                self._set_headers()

            else:
                self.send_response(401)
                self._set_headers()

        elif self.path == '/users':
            user_token = self.headers['Token']

            if str(user_token) in self.tokens.values():
                self.send_response(200)
                self.data = json.dumps({'users': self.users}).encode()
                self._set_headers()

            else:
                self.send_response(401)
                self._set_headers()

        else:
            self.send_response(200)
            self._set_headers()

        if self.data:
            self.wfile.write(self.data)
        self.data = ''

    def do_POST(self):
        if self.path == '/users':
            user_token = self.headers['Token']

            if str(user_token) in self.tokens.values():
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                new_user = json.loads(post_data.decode())['new_user']
                self.users.append(new_user)
                self.send_response(200)
                self._set_headers()

            else:
                self.send_response(401)
                self._set_headers()
        else:
            self.send_response(200)
            self._set_headers()

            self.data = post_data
            self.send_response(200)
            self._set_headers()
        if self.data:
            self.wfile.write(self.data)
        self.data = ''

    def do_PUT(self):
        self.do_POST()

class MockHTTPServer:
    def __init__(self, host='localhost', port=1050):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = MockHandleRequests
        self.handler.data = None
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        th = threading.Thread(target=self.server.serve_forever, daemon=True)
        th.start()
        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()

    def set_data(self, data):
        self.handler.data = json.dumps(data).encode()    
        
    def set_users(self, users):
        self.handler.users = users
