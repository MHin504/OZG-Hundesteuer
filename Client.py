import Server as Server

Name = None
Vorname = None
GeburtsdatumHuman = None
Strasse = None
Hausnummer = None
Ort = None
PLZ = None
NameDog = None
GeburtsdatumDog = None
Dograsse = None
Ermaessigung = None

def buildStringForServer():
    buildetStiring = f"{Name};{Vorname};{GeburtsdatumHuman};{Strasse};{Hausnummer};{Ort};{PLZ};,{NameDog};{GeburtsdatumDog};{Dograsse};{Ermaessigung}"
    return buildetStiring

def getInformations():
    print("Persönliche Angaben")
    setName()
    setVorname()
    setBirthHuman()
    print("Wohnanschrift")
    setStreet()
    setStreetNumber()
    setCity()
    setPLZ()
    print("Angaben zum Hund")
    setNameDog()
    setBirthDog()
    setDogRase()
    setErmaessigung()


def setName():
    state = True
    while state:
        global Name
        Name = input("Name*: ")
        result = Server.checkInput(Name, True, "Name")
        if(result):
            break;
        else:
            print("Bitte geben Sie einen Namen ein.")


def setVorname():
    state = True
    while state:
        global Vorname
        Vorname = input("Vorname*: ")
        result = Server.checkInput(Vorname, True, "Vorname")
        if (result):
            break;
        else:
            print("Bitte geben Sie einen Vorname ein.")

def setBirthHuman():
    state = True
    while state:
        global GeburtsdatumHuman
        GeburtsdatumHuman = input("Geburtsdatum*: ")
        result = Server.checkInput(GeburtsdatumHuman, True, "GeburtstagMensch")
        if (result[1]):
            break;
        else:
            print(f"{result[0]}")

def setStreet():
    state = True
    while state:
        global Strasse
        Strasse = input("Strasse*: ")
        result = Server.checkInput(Strasse, True,"Strasse")
        if(result):
            break;
        else:
            print("Bitte geben Sie eine Strasse ein.")

def setStreetNumber():
    state = True
    while state:
        global Hausnummer
        Hausnummer = input("Hausnummer*: ")
        result = Server.checkInput(Hausnummer, True, "Hausnummer")
        if(result):
            break;
        else:
            print("Bitte geben Sie eine Hausnummer ein.")

def setCity():
    state = True
    while state:
        global Ort
        Ort = input("Ort*: ")
        result = Server.checkInput(Ort, True, "Stadt")
        if (result):
            break;
        else:
            print("Bitte geben Sie eine Stadt ein.")

def setPLZ():
    state = True
    while state:
        global PLZ
        PLZ = input("PLZ*: ")
        result = Server.checkInput(PLZ, True, "PLZ")
        if (result):
            break;
        else:
            print("Bitte geben Sie eine gültige PLZ ein.")

def setNameDog():
    state = True
    while state:
        global NameDog
        NameDog = input("Name: ")
        result = Server.checkInput(NameDog, False, "NameHund")
        if (result):
            break;
        else:
            print("Bitte geben Sie einen Namen ein.")

def setBirthDog():
    state = True
    while state:
        global GeburtsdatumDog
        GeburtsdatumDog = input("Geburtstag*: ")
        result = Server.checkInput(GeburtsdatumDog, True, "GeburtstagHund")
        if (result[1]):
            break;
        else:
            print(f"{result[0]}")

def setDogRase():
    state = True
    while state:
        global Dograsse
        Dograsse = input("Hunderasse*: ")
        result = Server.checkInput(Dograsse, True, "Hunderasse")
        if (result):
            break;
        else:
            print("Bitte geben Sie eine gültige Hunderasse ein.")

def setErmaessigung():
    state = True
    while state:
        global Ermaessigung
        Ermaessigung = input("Steuerbefreitung/Ermaessigung (Ja/Nein)*: ")
        result = Server.checkInput(Ermaessigung, True, "Ermaessigung")
        if (result):
            break;
        else:
            print("Bitte geben Sie einen gültigen Wert ein. (Ja/Nein)")

try:
    getInformations()
    serverString = buildStringForServer()
    print(f"Ihre jährliche Hundesteuer beläuft sich auf {Server.serverHandler(serverString)}€.\nBitte überweisen Sie diese auf das Ihnen Postalisch mitgeteilte Bankkonto.")
except:
 print("An exception occurred.")