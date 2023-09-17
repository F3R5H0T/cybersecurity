import urllib.request

def main():
	
	#petición sin proxy

	p = urllib.request.urlopen('https://ifconfig.me')
	print("IP sin proxy: {}".format(p.read()))

	#configuramos el proxy

	urllib.request.install_opener(
		urllib.request.build_opener(
			urllib.request.ProxyHandler(
				{
					'http':'http://83.96.237.121:80',
					'https':'http://83.96.237.121:80'				
				}

			)
		)
	)

	peticion = urllib.request.urlopen("https://ifconfig.me")

	print("IP con proxy: {}".format(peticion.read()))

if __name__ == '__main__':
	main()