import json
from shack import shack
import os
from funcs import *

#load save data from json
#with open('data.json','r') as infile:
#	data=json.load(infile)

#write save data to json
#with open('data.json','w') as outfile:
#	json.dump(data, outfile, indent=4)

while True:
  
	print("start m'lord?")
	
	if command() == "yes":
		clear()
		print("very well m'lord.")
		delay()
		shack()