import json

#load save data from json
with open('save.json','r') as infile:
	save=json.load(infile)



print(save)
save["player"]["food"]=2
print(save)




#write save data to json
with open('save.json','w') as outfile:
	json.dump(save, outfile, indent=4)