dogdict = {
  "schäferhund": 15,
  "bulldogge": 19,
  "Chihuahua": 10
}

def printDogTax(dogTax):
    print(f"\n{dogTax}")

def getDogTax(dog):
    dogTax = dogdict[dog]
    return dogTax
