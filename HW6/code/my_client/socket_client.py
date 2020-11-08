import json
import socket

class SocketClient():
    def __init__(self, target_host = '127.0.0.1', target_port = 1050):
        self.target_host = target_host
        self.target_port = target_port

    def _send(self, request):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(3)
        self.client.connect((self.target_host, self.target_port))
        self.client.send(request.encode())

        total_data = []

        try:
            while True:
                data = self.client.recv(4096)
                if data:
                    total_data.append(data.decode())
                else:
                    break

            data = ''.join(total_data).splitlines()
            code = data[0].split()[1]

            self.client.close()

            if code == '200':
                return {'status_code': 200, 'headers': data[:-1],
                                'data': json.loads(data[-1])}
            else:
                return {'status_code': int(code), 'headers': data[:-1], 'data': None}
        except socket.timeout:
            self.client.close()
            return {'status_code': 408}

    def post(self, path, data, headers=None):
        if headers:
            headers = '\r\n'.join('{}: {}'.format(key, value) for key, value in headers.items())
            request = f'POST {path} HTTP/1.1\r\nContent-Type: application/json\r\n{headers}\r\nHost:{self.target_host}\r\n\r\n{data}'
        else:
            request = f'POST {path} HTTP/1.1\r\nContent-Type: application/json\r\nHost:{self.target_host}\r\n\r\n{data}'
        return self._send(request)


    def get(self, path, headers=None):
        if headers:
            headers = '\r\n'.join('{}: {}'.format(key, value) for key, value in headers.items())
            request = f'GET {path} HTTP/1.1\r\n{headers}\r\nHost:{self.target_host}\r\n\r\n'
        else:
            request = f'GET {path} HTTP/1.1\r\nHost:{self.target_host}\r\n\r\n'
        return self._send(request)

    def stop(self):
        self.client.close()