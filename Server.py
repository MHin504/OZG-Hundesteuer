dogdict = {
    "american staffordshire terrier": True,
    "pitbull terrier": True,
    "bullterrier": True,
    "bullmastiff": True,
    "staffordshire bullterrier": True,
    "cane corso": True,
    "dogo argentino": True,
    "bordeaux dogge": True,
    "fila brasileiro": True,
    "mastin espanol": True,
    "französische bulldogge": False,
    "labrador": False,
    "chihuahua": False,
    "australian shepherd": False,
    "rottweiler": False,
    "border collie": False,
    "golden retriever": False,
    "rhodesian ridgeback": False,
    "mops":False,
    "berner sennenhund": False
}

citydict = {
    75015: 108,
    76359: 96,
    69254: 78,
    76275: 96,
    76287: 90,
    76337: 108,
    76307: 66,
    76327: 72,
    75045: 108,
    76356: 96,
    76297: 84,
    76344: 84,
    76351: 72,
    76707: 72,
    76676: 60,
    76689: 69,
    76646: 96,
    75053: 48,
    75038: 90,
    76703: 87,
    76698: 61,
    76707: 48,
    68753: 96,
    76661: 96,
    76709: 72,
    76669: 90,
    76684: 75,
    75059: 72
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
