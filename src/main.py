import json
import random

#load save data from json
with open('data.json','r') as infile:
	data=json.load(infile)



print(data)
data["player"]["food"]=2
print(data)


def eventOutcome(eventName):

  eventSet=[]
  for i in data["random"][eventName]:
    for o in range(i):
      eventSet.append(data["random"][eventName][i])
  
  chosenEvent=eventSet[random.randint(0, len(eventSet))]
	return chosenEvent

chosenEvent=eventOutcome("exploration")

if chosenEvent=="parade":
  import parade
elif 

print(random("exploration"))

#can easily have a specific thingo in the dict and then add one to the specific monster
#for example each time they kill it
#data["kills"]["chosenEvent or whatever"]+=1
#get score value then divide it by lives and the final score can be a score per life

#write save data to json
with open('data.json','w') as outfile:
	json.dump(data, outfile, indent=4)