#!/usr/bin/env python
#_*_ coding: utf8 _*_
#enumeracion de usuarios de un sitio por json
 
import json
import requests
 
def main():
    url = requests.get("https://curso--python-0-pruebas1.000webhostapp.com/wp-json/wp/v2/users").json()
    user = url['slug']
    print(user)
 
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")
        exit()