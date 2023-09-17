#CONSEGUIR INFORMACION DE TABLAS ONLINE
import requests	
import re
from bs4 import BeautifulSoup
data=requests.get('https://www.umggaming.com/leaderboards')
soup=BeautifulSoup(data.text, 'html.parser')
table=soup.find('table',{'id':'leaderboard-table'})
tbody=table.find('tbody')
for tr in tbody.find_all('tr'):
	place=tr.find_all('td')[0].text.strip()
	print(place)
	'''td=tr.find_all('td')[1]
	for a in td.find_all('a')[1]:
		print(a)'''