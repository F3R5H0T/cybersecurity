#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from bs4 import BeautifulSoup

def main():
	user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
	url = requests.get(url="https://www.msn.com/es-mx/noticias", headers=user_agent)
	if url.status_code == 200:
		datos = BeautifulSoup(url.text, 'html.parser')
		datos1 = datos.find_all('img')
		for n in datos1:
			if n.get('title') is not None:
				print(n.get('title').encode('utf-8'))

if __name__ == '__main__':
	main()