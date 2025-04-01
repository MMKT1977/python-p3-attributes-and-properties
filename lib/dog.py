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
    def __init__(self, name):
        self.name = name
        self.set_name(name)
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        if(isinstance(name, str) and (1 <= len(name) <= 25) ):
            self.name = name
        
        else:
            print("Name must be string between 1 and 25 characters.")
    
dog = Dog()
dog.set_name("Fido")
print(dog.get_name())