import threading
import settings
import requests

from flask import Flask, request, jsonify
from urllib.parse import urljoin

app = Flask(__name__)
DATA = {}

def run_app(host, port):
    server = threading.Thread(target=app.run, kwargs={
        'host': host,
        'port': port
    })

    server.start()
    return server

def shutdown_app():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_app()


@app.route('/auth')
def auth():
    if request.headers.get('Authorization'):
        mock_response = requests.get( urljoin(settings.MOCK_URL, 'auth'),
                                     headers={'Authorization': f'{request.headers["Authorization"]}'})
        if mock_response.status_code == 200:
            return jsonify({'auth': True, 'token': mock_response.json()['Token']}), 200
        elif mock_response.status_code == 401:
            return jsonify({'auth': False}), 401
    else:
        return jsonify({'Error': 'Method not supported'}), 400
    
@app.route('/users', methods=['GET'])
def get_users():
    if request.headers.get('Token'):
        mock_response = requests.get( urljoin(settings.MOCK_URL, 'users'),
                                     headers={'Token': f'{request.headers["Token"]}'})
        if mock_response.status_code == 200:
            return jsonify({'users': mock_response.json()['users']}), 200
        elif mock_response.status_code == 401:
            return jsonify({'User': 'Not authorized'}), 401
    else:
        return jsonify({'Error': 'Method not supported'}), 400    

@app.route('/users', methods=['POST'])
def add_users():
    if request.headers.get('Token'):
        mock_response = requests.post( urljoin(settings.MOCK_URL, 'users'),
                                     headers={'Token': f'{request.headers["Token"]}',
                                              'Content-Length': f'{request.headers["Content-Length"]}'
                                              },
                                     data=request.data)
        if mock_response.status_code == 200:
            return jsonify({'Status': 'Success'}), 200
        elif mock_response.status_code == 401:
            return jsonify({'User': 'Not authorized'}), 401
    else:
        return jsonify({'Error': 'Method not supported'}), 400


@app.route('/mock_off')
def fake_mock():
    mock_response = requests.get( urljoin(settings.FAKE_MOCK_URL, '/mock_off' ) )


@app.route('/test_error')
def error():
    mock_response = requests.get( urljoin(settings.MOCK_URL, '/test_error') )
    if mock_response.status_code == 501:
        return jsonify({'Error': True}), 501
    else:
        return jsonify({'Error': False}), 500

@app.route('/timeout')
def timeout():
    return requests.get( urljoin(settings.MOCK_URL, '/timeout') )


if __name__ == '__main__':
    run_app(settings.APP_HOST, settings.APP_PORT)