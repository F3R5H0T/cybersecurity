#!/usr/bin/env python
#_*_ coding: utf8 _*_
import os

#print("ruta actual: "+os.getcwd())
os.chdir("C:/Users/ferch/Desktop")
print("ruta actual: "+os.getcwd())
#print(os.listdir(os.getcwd()))
#os.rmdir("pruebacursp")
#print(os.listdir(os.getcwd()))
#os.rename('noc','prueba')
#print(os.listdir(os.getcwd()))
print(os.stat("prueba"))
os.system("ping www.google.com")