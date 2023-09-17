#!/usr/bin/env python
#_*_ coding: utf8 _*_

import os
import subprocess

a = open(os.devnull, "w")
p = subprocess.call(['ping','1.1.1.1'],stdout=a,stderr=subprocess.STDOUT)

if p == 0:
	print("El comando se ejecutó correctamente")
else:
	print("Falló la ejecución")