# -*- coding: utf-8 -*-

class Location:
    def __init__(self):
        self.people = []
        self.food = 0
        self.water = 0
        self.shelter = 0
        self.regionalShelterMod = 0
        self.traverseEnergy = 0
        
    def addPerson(self, person):
        self.people.append(person)
        
    def removePerson(self, person):
        self.people.remove(person)
        
    def modifyFood(self, amount):
        self.food = self.food + amount
        
    def modifyWater(self, amount):
        self.water = self.water + amount
    
    def modifyShelter(self, amount):
        self.shelter = self.shelter + amount
    
    def modifyRegionalShelterMod(self, amount):
        self.regionalShelterMod = self.regionalShelterMod + amount
    
    def modifyTraverseEnergy(self, amount):
        self.traverseEnergy = self.traverseEnergy + amount
    
    def getLocationShelter(self):
        return self.shelter + self.regionalShelterMod