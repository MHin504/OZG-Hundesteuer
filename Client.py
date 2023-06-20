import Server as Server

def BuildStringForServer():
    serverString = f"{Name};{Vorname};{GeburtsdatumHuman};{Straße};{Hausnummer};{Ort};{PLZ};,{NameDog};{GeburtsdatumDog};{Dograsse};{Ermäßigung}"
    return serverString

#def CheckForValue():


print("Persönliche Angaben")
Name = input("Name*: ")
Vorname = input("Vorname*: ")
GeburtsdatumHuman = input("Geburtsdatum*: ")
print("Wohnanschrift")
Straße = input("Straße*: ")
Hausnummer = input("Hausnummer*: ")
Ort = input("Ort*: ")
PLZ = input("PLZ*: ")
print("Angaben zum Hund")
NameDog = input("Name: ")
GeburtsdatumDog = input("Geburtstag*: ")
Dograsse = input("Hunderasse*: ")
Ermäßigung = input("Steuerbefreitung/Ermäßigung (Ja/Nein)*: ")



try:
    serverString = BuildStringForServer()
    dogTax = Server.getDogTax(Dograsse.lower())
    Server.printDogTax(dogTax)
except:
 print("An exception occured.")