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
# used for validating the breed property.

class Dog:
    def __init__(self,name="Fido", breed="Mastiff"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name
# getter for the dog's name and returns  private variable self_name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
# validates the name : must be string and length between 1-25
# if valid set self_name and helpful error message
    # Breed property
    @property
    def breed(self):
        return self._breed
# getter for breed and return the value stored in self._breed
    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.") 

# validates that the value is one of the approved breeds
# if valid sets self._breed and if not ptint error message