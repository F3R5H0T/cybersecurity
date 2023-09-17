#!/usr/bin/env python
#_*_ coding: utf8 _*_

import hashlib

def main():
	hashpass = str(raw_input("hash: "))
	passfile=open("original.txt","r")

	for p in passfile.readlines():
		n=p.strip("\n")
		n=hashlib.md5(n).hexdigest()
		if n == hashpass:
			print("Password: {} \nHash: {}".format(p,n))
			break

if __name__ == '__main__':
	main()