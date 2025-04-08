#!/usr/bin/env python3
 
APPROVED_BREEDS = [
     "Mastiff",
     "Chihuahua",
     "Corgi",
     "Shar Pei",
     "Beagle",
     "French Bulldog",
     "Pug",
     "Pointer"
 ]
 
class Dog:
    def __init__(self, name=None, breed=""):
          self._name = None
          self._breed = ""
          if name is not None:
            self.name = name
          self.breed = breed
     
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
         if not isinstance(name, str) or not (1 <= len(name) <= 25):
             print("Name must be string between 1 and 25 characters.")
         else:
             self._name = name

    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, breed):
        if breed and breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed

            
dog = Dog("Fido","Chihuahua")
print(dog.name)
print(dog.breed)
