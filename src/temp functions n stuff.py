
def eventOutcome(eventName):

  eventSet=[]
  for i in data["random"][eventName]:
    for o in range(i):
      eventSet.append(data["random"][eventName][i])
  
  chosenEvent=eventSet[random.randint(0, len(eventSet))]
	return chosenEvent