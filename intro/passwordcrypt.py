#!/usr/bin/env python
#_*_ coding: utf8 _*_
import hashlib

def main():
	password=str(input("Palabra: "))

	md5pass = hashlib.md5(password.encode('utf-8')).hexdigest()
	print("md5: "+md5pass+"\n")

	sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
	print("sha1: "+sha1pass+"\n")

	sha224pass = hashlib.sha224(password.encode('utf-8')).hexdigest()
	print("sha224: "+sha224pass+"\n")

	sha256pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
	print("sha256: "+sha256pass+"\n")

	sha384pass = hashlib.sha384(password.encode('utf-8')).hexdigest()
	print("sha384: "+sha384pass+"\n")

	sha512pass = hashlib.sha512(password.encode('utf-8')).hexdigest()
	print("sha512: "+sha512pass+"\n")

if __name__ == '__main__':
	main()