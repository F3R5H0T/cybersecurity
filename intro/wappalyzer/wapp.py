#!/usr/bin/env python
#_*_ coding: utf8 _*_
from Wappalyzer import WebPage, Wappalyzer

def main():
	wap = Wappalyzer.latest()

	web = WebPage.new_from_url("https://www.udemy.com")
	tecnologias = wap.analyze(web)
	for t in tecnologias:
		print("Tecnología detectada: {}".format(t))
#except:
#		print("ha ocurrido un error")

if __name__== '__main__':
	try: 
		main()
	except KeyboardInterrupt:
		print("Saliendo")
		exit()