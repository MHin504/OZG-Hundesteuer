import Server as Server

Name = input("Name: ")
Vorname = input("Vorname: ")
Alter = input("Alter: ")
Dograse = input("Hunderasse: ")

#def importInformationsToServer():
    #Server.getDogTax(Dograse.lower())

try:
    #importInformationsToServer()
    dogTax = Server.getDogTax(Dograse.lower())
    Server.printDogTax(dogTax)
except:
 print("An exception occured.")