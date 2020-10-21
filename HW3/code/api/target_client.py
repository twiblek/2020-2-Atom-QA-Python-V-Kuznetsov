import requests
import json

from urllib.parse import urljoin
from requests.cookies import cookiejar_from_dict

class ApiClient:

	def __init__(self, user, password):
		self.base_url = 'https://target.my.com'

		self.session = requests.Session()

		self.csrf_token = ''

		self.user = user
		self.password = password

		self._login()

	def _request(self, method, location, status_code=200, headers=None, params=None, data=None, json=True):
		
		if headers is None:
			headers = {
				'Content-Type': 'application/json',
				'X-Requested-With': 'XMLHttpRequest',
				'X-CSRFToken': self.csrf_token,
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.271'
			}

		url = urljoin(self.base_url, location)
		response = self.session.request(method, url, headers=headers, params=params, data=data)

		return response

	def _login(self):
		data = {
			'email': self.user,
			'password': self.password,
			'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
			'failure': 'https://account.my.com/login/'
		}

		headers = {
			"Content-Type": "application/x-www-form-urlencoded",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.271",
			"Origin": "https://target.my.com",
			"Referer": "https://target.my.com/",
		}

		auth_url = 'https://auth-ac.my.com/auth'
		auth_resp = requests.post(auth_url, data = data, headers = headers)

		self.session.cookies = auth_resp.history[0].cookies

		self.csrf_token = self._request('GET', 'csrf').cookies.get("csrftoken")

	def get_all_segments(self):
		resp = self._request('GET', 'api/v2/remarketing/segments.json')
		return resp

		
	def get_segment_by_id(self, id):
		resp = self._request('GET', 'api/v2/remarketing/segments/{}.json'.format(id))
		return resp

	def create_segment(self, name):

		data = {
			"name": name,
			"pass_condition": 1,
			"relations": [
				{
					"object_type": "remarketing_player",
					"params": {
						"type": "positive",
						"left": 365,
						"right": 0
					}
				}
			],
			"logicType": "or"
		}
		data = json.dumps(data)

		resp = self._request('POST', 'api/v2/remarketing/segments.json', data = data)

		return resp

	def delete_segment(self, id):
		resp = self._request('DELETE', 'api/v2/remarketing/segments/{}.json'.format(id))
