import os
import json

#player input (!!!UNDER CONSTRUCTION!!!)
#def command(x):
  
 # try:

   # x="a"
   # command=input("What would you like to do?").lower()
  #  return(command)
		
#	try:

  #  x="b"
 #   command=input("Where would you like to go?").lower()
 #   return(command)

#  except ValueError:
  
 #   command=input().lower()
 #   return(command)
  
#select random event
def eventOutcome(eventName):

  eventSet=[]
  for i in data["random"][eventName]:
    for o in range(i):
      eventSet.append(data["random"][eventName][i])
  
  chosenEvent=eventSet[random.randint(0, len(eventSet))]
  return(chosenEvent)

#clear console
def clear():

  os.system('clear')

#delay with input
def delay(): 

  delay=input("Press enter to continue.")