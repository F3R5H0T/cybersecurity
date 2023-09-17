#!/usr/bin/env python
#_*_ coding: utf8 _*_

def title():
	files = open('web.html','r')
	inicio = "<title>"
	final = "</title>"
	for l in files.readlines():
		if inicio in l:
			p = l.find(inicio)
			print(l[p+len(inicio):- len(final)-1])

def main():
	title()

if __name__ == '__main__':
	main()