import json

#load save data from json
with open('data.json','r') as infile:
	data=json.load(infile)



print(data)



#write save data to json
with open('data.json','w') as outfile:
	json.dump(data, outfile, indent=4)