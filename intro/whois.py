#!/usr/bin/env python
#_*_ coding: utf8 _*_
import requests
from bs4 import BeautifulSoup

def main():
	a = requests.get("https://who.is/whois/reldsce.org")
	soup = BeautifulSoup(a.text, 'html5lib')
	for l in soup.find_all("pre"):
		print(l.get_text())

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()