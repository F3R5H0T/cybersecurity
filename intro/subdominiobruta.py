#!/usr/bin/env python
#_*_ coding: utf8 _*_
import dns.resolver
from os import path

def main():
	if path.exists('original.txt'):
		wordlist = open('original.txt','r')
		wordlist = wordlist.read().split('\n')
		lista = []
		for s in wordlist:
			try:
				a = dns.resolver.query('{}.google.com'.format(s),'A')
				lista.append('{}.google.com'.format(s))
			except:
				pass
		if len(lista) > 0:
			print('Número de subdominios posibles: {}'.format(len(lista)))
			for e in lista:
				print(e)
		else:
			print("no se encontraron subdominios")
	else:
		print("no existe el archivo")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()