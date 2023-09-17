import subprocess
import re
import unicodedata
command_output=subprocess.run(['netsh','wlan','show','profiles'],capture_output=True).stdout.decode("iso8859")
profile_names=re.findall("Perfil de todos los usuarios     : (.*)\r", command_output)
wifi_list=[]

if len(profile_names) !=0:
	for red in profile_names:
		wifi_profile={}
		profile_info=subprocess.run(['netsh','wlan','show','profiles',red], capture_output=True).stdout.decode("iso8859")

		if re.search("Clave de seguridad                         : no está presente", profile_info):
			continue
		else:
			wifi_profile["ssid"]=red 
			profile_info_pass=subprocess.run(["netsh","wlan","show","profile",red,"key=clear"], capture_output=True).stdout.decode("iso8859")
			password=re.search("Contenido de la clave  :(.*)\r",profile_info_pass)

			if password==None:
				wifi_profile["password"]=None
			else:
				wifi_profile["password"]=password[1]
			wifi_list.append(wifi_profile)
for x in range(len(wifi_list)):
	print(wifi_list[x])
exit()