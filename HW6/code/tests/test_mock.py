import json
import pytest
import requests
import socket

from time import sleep
from urllib.parse import urljoin
from application.app_server import run_app, shutdown_app
from my_client.socket_client import SocketClient
from my_server.mock_http_server import MockHTTPServer
from settings import APP_HOST, APP_PORT, APP_URL, MOCK_HOST, MOCK_PORT, MOCK_URL, MOCK_SHUTDOWN_URL, MOCK_SET_USERS



class TestMock:
    users = ['Test', 'User', 'Admin']

    @pytest.fixture(scope='session')
    def up_mock(self):
        self.mock_http = MockHTTPServer(MOCK_HOST, MOCK_PORT)
        self.mock_http.set_users(self.users)
        self.mock_http.start()
        yield
        self.mock_http.stop()

    @pytest.fixture(scope='session')
    def up_app(self):
        run_app(APP_HOST, APP_PORT)
        yield
        requests.get(urljoin(APP_URL, 'shutdown'))

    @pytest.fixture(autouse=True)
    def run_client(self, up_app, up_mock):
        self.client = SocketClient(APP_HOST, APP_PORT)
        yield
        self.client.stop()

    def test_mock_off(self):
        data = self.client.get('/mock_off')
        assert data['status_code'] == 500
    
    def test_mock_timeout(self):
        data = self.client.get('/timeout')
        assert data['status_code'] == 408
    
    def test_mock_error(self):
        data = self.client.get('/test_error')
        assert data['status_code'] == 501 
    
    def test_success_auth(self):
        data = self.client.get('/auth', headers={'Authorization': 'Test'})
        assert data['status_code'] == 200

    def test_failed_auth(self):
        data = self.client.get('/auth', headers={'Authorization': 'NoTest'})
        assert data['status_code'] == 401

    def test_auth_without_header(self):
        data = self.client.get('/auth')
        assert data['status_code'] == 400

    def test_get_users_without_token(self):
        data = self.client.get('/users')
        assert data['status_code'] == 400    
    
    def test_get_users_with_token(self):
        data = self.client.get('/auth', headers={'Authorization': 'Test'})
        data = self.client.get('/users', headers={'Token': data['data']['token']})
        assert data['status_code'] == 200
        assert data['data']['users'] == self.users
    
    def test_get_users_with_wrong_token(self):
        data = self.client.get('/users', headers={'Token': 'Test'})
        assert data['status_code'] == 401
    
    def test_add_user_with_wrong_token(self):
        new_user = 'NewUser'

        post_data = json.dumps({'new_user': new_user})

        data = self.client.post('/users', headers={'Token': 'simple_token', 'Content-Length': len(post_data.encode())}, 
                                data=post_data)

        assert data['status_code'] == 401
    
    def test_add_user_with_token(self):
        new_user = 'NewUser'
        data = self.client.get('/auth', headers={'Authorization': 'Test'})

        post_data = json.dumps({'new_user': new_user})

        self.client.post('/users', 
                         headers={'Token': data['data']['token'], 'Content-Length': len(post_data.encode())}, 
                         data=post_data)

        data = self.client.get('/users', headers={'Token': data['data']['token']})
        assert data['status_code'] == 200
        assert new_user in data['data']['users']