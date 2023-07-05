import datetime

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
    "mops": False,
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

def serverHandler(clientString):
    dogInformations = splitStringFromClient(clientString, True)
    personalInformation = splitStringFromClient(clientString, False)
    if(dogInformations[3].lower() == "nein"):
        regionTax = getRegionTax(personalInformation)
        dogRaceSeperation = getDogRaceSeperation(dogInformations)
        dogTax = getDogTax(dogRaceSeperation, regionTax)

    else:
        dogTax = 0
    return dogTax

def splitStringFromClient(clientString, state):
    try:
        seperations = clientString.split(',')
        if(state):
            dogInformation = seperations[1].split(';')
            return dogInformation
        else:
            personalInformation = seperations[0].split(';')
            return personalInformation
    except:
        print("Error in SplitStringFormClient")
def printDogTax(dogTax):
    print(f"\n{dogTax}")

def getRegionTax(personalInformations):
    regionTax = citydict[int(personalInformations[6])]
    return regionTax
def getDogTax(dogRaceSeperation,regionTax):
    dogTax = None
    if(dogRaceSeperation == True):
       dogTax = int(regionTax) * 5
    else:
        dogTax = int(regionTax)
    if(dogTax != None):
        return dogTax
    else:
        return "Error in DogTax"

def getDogRaceSeperation(dogInformations):
    dogRaceSeperation = dogdict[dogInformations[2]]
    return dogRaceSeperation


def checkDate(value):
    try:
        day, month, year = map(int, value.split('.'))
        geburtstag_obj = datetime.date(year, month, day)
        try:
            date = value.strip()
            datetime.datetime.strptime(date, "%d.%m.%Y")
        except ValueError:
            return "Ungueltiges Datumsformat. Bitte geben Sie den Geburtstag im Format TT.MM.JJJJ ein.", False
        if geburtstag_obj >= datetime.date.today():
            return "Ungueltiges Datumsformat. Der Geburtstag muss in der Vergangenheit liegen.", False
        if month == 2 and day > 28:
            leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            if (day == 29 and not leap_year) or (day > 29):
                return "Ungueltiges Datumsformat. Bitte geben Sie ein gueltiges Geburtsdatum ein.", False
        return "", True
    except:
        return "Bei der Datumsüberprüfung lief etwas schief. Bitte wenden Sie sich an einen Admin", False

def checkInput(value,nessesary, nameCheck):
    if(nessesary):
        if(value == None or value == ''):
            return False
        else:
            if("Geburtstag" in nameCheck):
                result = checkDate(value)
                return result
            elif(nameCheck == "Hunderasse"):
                if(value in dogdict):
                    return True
                else:
                    return False
            elif(nameCheck == "Ermaessigung"):
                if(value.lower() == "ja" or value.lower() == "nein"):
                    return True
                else:
                    return False
            elif(nameCheck == "PLZ"):
                if(value.isnumeric and int(value.strip()) in citydict):
                    return True
                else:
                    return False
            elif(nameCheck == "Hausnummer"):
                if(value.isnumeric()):
                    return True
                else:
                    return False
            else:
                return True
    else:
        if(value != None):
            return True
        else:
            return False
