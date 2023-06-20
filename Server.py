dogdict = {
  "schäferhund": 15,
  "bulldogge": 19,
  "Chihuahua": 10
}

def SplitStringFromClient(clientString):
    seperations = clientString.split(',')
    personInformations = seperations[0].split(';')
    dogInformations = seperations[1].split(';')
def printDogTax(dogTax):
    print(f"\n{dogTax}")

def getDogTax(dog):
    dogTax = dogdict[dog]
    return dogTax
