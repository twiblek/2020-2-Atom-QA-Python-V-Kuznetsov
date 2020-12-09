from urllib.parse import urljoin

APP_HOST, APP_PORT = '127.0.0.1', 5000
APP_URL = f'http://{APP_HOST}:{APP_PORT}'

APP_SHUTDOWN_URL = urljoin(APP_URL, 'shutdown')

MOCK_HOST, MOCK_PORT = '127.0.0.1', 5001
MOCK_URL = f'http://{MOCK_HOST}:{MOCK_PORT}'

MOCK_VALID_URL = urljoin(MOCK_URL, 'valid')
MOCK_SHUTDOWN_URL = urljoin(MOCK_URL, 'shutdown')
MOCK_SET_USERS = urljoin(MOCK_URL, 'set_valid_users')

FAKE_MOCK_HOST, FAKE_MOCK_PORT = '127.0.0.1', 5002
FAKE_MOCK_URL = f'http://{FAKE_MOCK_HOST}:{FAKE_MOCK_PORT}'