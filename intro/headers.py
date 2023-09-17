#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import argparse
parser= argparse.ArgumentParser(description="Detector de headers")
parser.add_argument("-t","--target",help="Objetivo")
parser=parser.parse_args()
def main():
	if parser.target:
		try:
			url=requests.get(url=parser.target)
			cabeceras=dict(url.headers)
			for h in cabeceras:
				print(h+":"+cabeceras[h])
		except:
			print("No me pude conectar")
	else:
		print("No hay objetivo")
if __name__ == '__main__':
	main()