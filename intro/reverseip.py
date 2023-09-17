#!/usr/bin/env python
#_*_ coding: utf8 _*_
import requests
from bs4 import BeautifulSoup

def main():
	sitio = 'www.cloudflare.com'
	agent = {'User-Agent' : 'Opera'}
	a = requests.get("https://viewdns.info/reverseip/?host=cloudflare.com&t=1", headers=agent)
	b = BeautifulSoup(a.text, 'html5lib')
	c = b.find(id="null")
	d = c.find(border="1")
	for l in d.find_all("tr"):
		print("Sitio encontrado: "+l.td.string)
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()