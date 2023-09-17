import requests

def main():
	a = requests.get('https://ifconfig.me')
	print("IP sin proxy: {}".format(a.text))

	proxy = {
		'http':'http://83.96.237.121:80',
		'https':'http://83.96.237.121:80'
	}

	b = requests.get('https://ifconfig.me', proxies=proxy)

	print("IP con proxy: {}".format(b.text))
if __name__ == '__main__':
	main()