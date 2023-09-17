#!/usr/bin/env python
#_*_ coding: utf8 _*_
import requests

def main():
	word = "cloudflare"
	url = requests.get("https://www.cloudflare.com/es-es/")
	cabeceras = dict(url.headers)
	verify = False
	print(cabeceras)
	for c in cabeceras:
		if cabeceras[c].lower():
			verify = True
			break
	if verify == True:
		print("Cloudflare presente")
	else:
		print("no hay cloudflare")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()