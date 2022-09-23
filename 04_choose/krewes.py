"""
Emily Ortiz, Sadi Narloy, Ravindra Mangar
SoftDev
TNPG: Wasabi Rain
2022-09-22

DISCO:
  -The existence of the dict.keys() function
    -It does not return a list, but rather a "viewing object" that holds the array
    -This object can be type casted into a list
  -random.choice() takes a random element from a list
  -do while loops do not exist in python

QCC:
  -Super shocked that "do while" does not exist
  
OPS SUMMARY:
  -Start by making a list from the set of keys
  -Pick a random key from the list
  -Get the list that the key refers to
  -Check if that list has any values in it
    -If not, repeat the process of picking a new key until an array with values is addressed
  -Pick a random element from the area 
"""

import random

krewes = {
          2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"], 
          7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"], 
          8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
         }

def fixKrewes(krewes):
  listOfKeys = list(krewes.keys())
  for i in listOfKeys:
    for j in range(len(krewes[i])):
      krewes[i][j] = [False, krewes[i][j]]
  return krewes

def randFromDictOfArr(dictionary):
  listOfKeys = list(dictionary.keys())
  #print(ListOfKeys)
  pickingFromKeys= random.choice(listOfKeys)
  #print(pickingFromKeys)
  arrFromDict = dictionary[pickingFromKeys]
  while (len(arrFromDict) <= 0):
    pickingFromKeys= random.choice(listOfKeys)
    arrFromDict = dictionary[pickingFromKeys]
  pickingFromArr = random.choice(arrFromDict)
  pickingFromArr[0] = True

  #print((krewes[list[get_rand_num()]])[get_rand_num()])
  
#FOR LOOP TO VERIFY THAT RESULTS ARE RANDOM // RUNS TEN TIMES
fixKrewes(krewes)

for i in range(1000):
  randFromDictOfArr(krewes)

listOfKeys = list(krewes.keys())
for i in listOfKeys:
  for j in range(len(krewes[i])):
   print(krewes[i][j])
