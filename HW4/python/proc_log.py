# -*- coding: utf-8 -*-
from collections import OrderedDict

import pandas as pd
import argparse
import json
import re
LINEFORMAT = re.compile(r"""^(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(\d{2}\/[A-Za-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\".*(?P<method>GET|POST|HEAD|PUT) )(?P<url>.+)(HTTP\/1\.[1,0]")) (?P<statuscode>\d{3}) (?P<bytessent>(\d+|-)) ((-|"(.*)")) (["](.*)["]) (["]([^"]*)["])$""")

class LOGGER_PROCESSING():
	def __init__(self, input, output, is_json = False):
		self.data = self.log_to_df(input)

		if self.data is None:
			return

		res = {
			'MethodsCount': self.method_count(),
			'Count': self.all_count(),
			'BiggestQuerys': self.biggest_querys(),
			'ClientErrors': self.most_client_errors(),
			'ServerError': self.biggest_server_errors()
		}

		if is_json:
			self.res_to_json(res, output)
		else:
			self.res_to_file(res, output)
		print('DONE')

	def log_to_df(self, path):
		items = []

		with open(path, 'r') as f:
			for line in f:
				try:
					item = LINEFORMAT.search(line).groupdict()

					item['bytessent'] = int(item['bytessent']) if item['bytessent'] != '-' else -1
					item['statuscode'] = int(item['statuscode'])

					items.append(item)
				except Exception as e:
					print(line)
					print(e)
					return None

		return pd.DataFrame(items)

	def method_count(self):
		### Количество запросов по типу
		res = self.data['method'].value_counts().to_dict()
		return res

	def all_count(self):
		### Общее количество запросов
		return len(self.data)

	def biggest_querys(self):
		### Топ 10 самых больших по размеру запросов, должно быть видно url, код, число запросов
		url_data = self.data[['url', 'statuscode', 'bytessent']]
		url_data = url_data.sort_values('bytessent', ascending=False).head(10)
		return url_data[['statuscode', 'bytessent', 'url']]

	def most_client_errors(self):
		### Топ 10 запросов по количеству, которые завершились клиентской ошибкой, должно быть видно url, статус код, ip адрес
		client_data = self.data[['url', 'statuscode', 'ipaddress']]
		client_data = client_data[(client_data['statuscode'] >= 400) & (client_data['statuscode'] < 500)]
		client_data['agg'] = 1
		client_data = client_data.groupby(['url', 'statuscode', 'ipaddress'], as_index=False)['agg'].agg('count')
		client_data = client_data.sort_values('agg', ascending=False).head(10)
		return client_data[['statuscode', 'ipaddress', 'agg', 'url']]

	def biggest_server_errors(self):
		### Топ 10 запросов серверных ошибок по размеру запроса, должно быть видно url, статус код, ip адрес
		server_error = self.data[['url', 'statuscode', 'ipaddress', 'bytessent']]
		server_error = server_error[server_error['statuscode'] >= 500].sort_values('bytessent', ascending=False).head(10)
		return server_error[['statuscode', 'ipaddress', 'bytessent', 'url']]

	def res_to_json(self, res, output):
		### Cохранять собранные данные в json
		for key in res:
			if type(res[key]) == type(pd.DataFrame()):
				res[key] = res[key].to_dict('records')
				#print(res[key])

		with open(output, 'w', encoding='utf-8') as f:
			f.write(json.dumps(res, indent=4))

	def res_to_file(self, res, output):
		### Cохранять в произвольный файл через любой делимитер
		pd.set_option('display.max_rows', None)
		pd.set_option('display.max_columns', None)
		pd.set_option('display.width', None)
		pd.set_option('display.max_colwidth', -1)

		res_string = ''

		for key in res:
			res_string += '%s\n' % key
			if type(res[key]) == dict:
				for key_2, value in res[key].items():
					res_string += '%s - %s\n' % (key_2, value)
			elif type(res[key]) == type(pd.DataFrame()):
				res_string += res[key].to_string(index=False)
			else:
				res_string += str(res[key])
			res_string += '\n=====\n'

		with open(output, 'w', encoding='utf-8') as f:
			f.write(res_string)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Process log file from nginx.')
	parser.add_argument('input', type=str, help='Path for log file')
	parser.add_argument('-o', '--output', type=str, default='res.txt', help='Path for results')
	parser.add_argument('-j', '--json', default=False, action='store_true', help='Choose to save as json format')

	args = parser.parse_args()
	#print(args)
	LOGGER_PROCESSING(input = args.input,
					   output = args.output,
					   is_json = args.json
					   )