#!/usr/bin/env python
#_*_ coding: utf8 _*_

import re
import urllib


def parser3():
	cadena = "Ésta es una cadena de la cual vamos a tomar como ejemplo para otra función"
	#función sub()
	cadena1 = re.sub("función","sub",cadena)
	print(cadena1)
	
def main():
	parser3()
	
if __name__ == '__main__':
	main()