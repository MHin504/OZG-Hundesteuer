import Server as Server

Name = None
Vorname = None
GeburtsdatumHuman = None
Straße = None
Hausnummer = None
Ort = None
PLZ = None
NameDog = None
GeburtsdatumDog = None
Dograsse = None
Ermäßigung = None

def buildStringForServer():
    buildetStiring = f"{Name};{Vorname};{GeburtsdatumHuman};{Straße};{Hausnummer};{Ort};{PLZ};,{NameDog};{GeburtsdatumDog};{Dograsse};{Ermäßigung}"
    return buildetStiring

def getInformations():
    print("Persönliche Angaben")
    getName()
    getVorname()
    getBirthHuman()
    print("Wohnanschrift")
    getStreet()
    getStreetNumber()
    getCity()
    getPLZ()
    print("Angaben zum Hund")
    getNameDog()
    getBirthDog()
    getDogRase()
    getErmäßigung()

def getName():
    global Name
    Name = input("Name*: ")
def getVorname():
    global Vorname
    Vorname = input("Vorname*: ")

def getBirthHuman():
    global GeburtsdatumHuman
    GeburtsdatumHuman = input("Geburtsdatum*: ")

def getStreet():
    global Straße
    Straße = input("Straße*: ")

def getStreetNumber():
    global Hausnummer
    Hausnummer = input("Hausnummer*: ")

def getCity():
    global Ort
    Ort = input("Ort*: ")

def getPLZ():
    global PLZ
    PLZ = input("PLZ*: ")

def getNameDog():
    global NameDog
    NameDog = input("Name: ")

def getBirthDog():
    global GeburtsdatumDog
    GeburtsdatumDog = input("Geburtstag*: ")

def getDogRase():
    global Dograsse
    Dograsse = input("Hunderasse*: ")

def getErmäßigung():
    global Ermäßigung
    Ermäßigung = input("Steuerbefreitung/Ermäßigung (Ja/Nein)*: ")

try:
    getInformations()
    serverString = buildStringForServer()
    print(Server.serverHandler(serverString))
except:
 print("An exception occurred.")