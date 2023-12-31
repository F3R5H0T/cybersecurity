#!/usr/bin/env python
#_*_ coding: utf8 _*_
import requests
from bs4 import BeautifulSoup

def main():
	url = "https://curso--python-0-pruebas1.000webhostapp.com"
	cabecera = {'User-Agent' : 'Opera'}
	peticion = requests.get(url=url,headers=cabecera)
	soup= BeautifulSoup(peticion.text, 'html5lib')
	for v in soup.find_all('meta'):
		if v.get('name') == 'generator':
			version= v.get('content')
			print(version)
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("saliendo")
		exit()