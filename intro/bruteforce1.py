#!/usr/bin/env python
#_*_ coding: utf8 _*_

import hashlib
from urllib import urlopen

def main():
	hashpass = str(raw_input("hash: "))
	passwordlist = urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").read()
	for p in passwordlist.split("\n"):
		z = hashlib.md5(p).hexdigest()
		if z == hashpass:
			print("Password: {}\nHash: {}".format(p,z))

if __name__ == '__main__':
	main()