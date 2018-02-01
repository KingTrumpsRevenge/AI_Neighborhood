# -*- coding: utf-8 -*-
from random import random, randint

from ai import Dqn

class Person():
    def __init__(self, inAncestors, inParents, inSiblings, ssn, birth_stamp):
        # inputs, resulting actions, gamma

        #initializers
        self.birthday = birth_stamp
        self.ssn = ssn
        self.reproductionHose = bool(random.getrandbits(1))
        self.gestationalPeriod = 1 * 270 * 24 * 60 * 60
        self.teachingPeriod = 18 * 365 * 24 * 60 * 60
        #resources
        self.cashBalance = 0
        self.foodBalance = 0
        self.waterBalance = 0
        
        #Environment
        self.xLoc = 0
        self.yLoc = 0
        
        #Emotions
        self.energy = 0
        self.confidence = 0
        self.fear = 0
        self.anger = 0
        self.happiness = 0
        self.sadness = 0
        self.safety = 0
        self.intelligent = 0

        #Relationships
        self.ancestors = []
        self.parents = []
        self.siblings = []
        self.offspring = []
        self.teachingOffspring = []
        self.gestatingOffspring = []
        #friend with trust > .95 (not ancestor, parent, sibling or offspring)        
        self.mates = []
        #Aquiantences with trust > .33
        self.friends = []
        self.aquiantences = []
        
        #add in ancestors with trust level .50
        for ancestor in inAncestors:
            self.ancestors.append((ancestor, .50))
        
        #add in parents with trust level 1
        for parent in inParents:
            self.parents.append((parent, 1))
        
        #add in siblings with trust level .75
        for sibling in inSiblings:
            self.siblings.append((sibling, .75))
        
        #Lobes
        
        #Inputs:
        #--5--CashBalance, Food, Water, Food/Min, Water/Min
        #Outputs:
        #--4--AquireFood, SellFood, AquireWater, SellWater
        self.resourceLobe = Dqn(5, 4, 0.9)
        
        #Inputs:
        #--10--X, Y, Year, Month, Day, Hour, Minute, Second, ShelterValue, RegionValue
        #Outputs:
        #--5--Move-Up, Move-Left, Move-Right, Move-Down, stay put
        self.environmentLobe = Dqn(10, 5, 0.9)
        
        #Inputs:
        #--5--#People in conversation range, Conversation Range Trust Level, Conversation Range Need Water, Conversation Range Need Food, Conversation Range Need Cash
        #--5--#People in announcemnet range, announcemnet Range Trust Level, announcemnet Range Need Water, announcemnet Range Need Food, announcemnet Range Need Cash
        #--3--Conversation Range Have Water, Conversation Range Have Food, Conversation Range Have Cash
        #--3--announcemnet Range Have Water, announcemnet Range Have Food, announcemnet Range Have Cash
        #Outputs:
        #--8--Ask for food, Ask for Water, Ask for cash, Offer food, Offer water, offer cash, Conversation, Announcement
        self.socialLobe = Dqn(16, 8, 0.9)
        
        #Inputs:
        #--8--Energy, confidence, fear, anger, happiness, sadness, saftey, intelligent
        #Outputs:
        #--6--Motivation, Extroversion(<.5 = Introverted, >.5=Extroverted), Defensive, hungry, thirsty, tired
        self.personalLobe = Dqn(8, 6, 0.9)
        
        #Inputs:
        #--8--#Ancestors, Ancestoral Trust, #Siblings, Sibling Trust, #Offspring, Offspring Trust, #Mates, Mate Trust, 
        #--6--#Parents, Parental Trust, #Friends, Friend Trust, #Aquaintences, Aquaintences Trust
        #Outputs:
        #--7--flirt, chat, share meal, reproduce, share drinks, play game, fight
        self.relationshipLobe = Dqn(14, 7, 0.9)
        
        #Inputs(Outputs of other nodes:
        #--4--ResourceLobe--AquireFood, SellFood, AquireWater, SellWater
        #--5--EnvironmentNode--Move-Up, Move-Left, Move-Right, Move-Down, stay put
        #--8--SocialLobe--Ask for food, Ask for Water, Ask for cash, Offer food, Offer water, offer cash, conversation, announcement
        #--6--personalLobe--Motivation, Extroversion(<.5 = Introverted, >.5=Extroverted), Defensive, hungry, thirsty, tired
        #--7--relationshipLobe--flirt, chat, share meal, reproduce, grab drinks, play game, fight
        #Outputs:
        #--4--Private correspondance, Conversation, Announcement, 
        #--7--WithAncestor, WithParent, WithSibling, WithMate, WithFriend, With Aquaintence, trust floor
        #--6--Ask for food, Ask for Water, Ask for cash, offer food, offer water, offer cash
        #--5--Move-Up, Move-Down, Move-Left, Move-Right, stay put
        #--4--eat, drink, sleep, do nothing
        #--7--flirt, chat, share meal, reproduce, share drinks, play game, fight
        self.consciousLobe = Dqn(30, 33, 0.9)
        
    def flirtRequest(self, initiatorSSN):
        #compiler placeholder
        return (1, 2, 3)
    
    def recieveFlirtResponse(self, response):
        #compiler placeholder
        1 + 1

    def chatRequest(self, initiatorSSN):
        #compiler placeholder
        return (1, 2, 3)
        
    def recieveChatResponse(self, response):
        #compiler placeholder
        1 + 1
    
    def shareMealRequest(self, initiator):
        #compiler placeholder
        #potentially request food
        return (1, 2, 3)
        
    def recieveShareMealResponse(self, response):
        #compiler placeholder
        1 + 1
        
    def reproduceRequest(self, initiator):
        #compiler placeholder
        #full initiator in case flirt/chat request
        return (1, 2, 3)
        
    def recieveReproduceResponse(self, response):
        #compiler placeholder
        1 + 1
        
    def shareDrinkRequest(self, initiator):
        #compiler placeholder
        #potentially request food
        return (1, 2, 3)
        
    def recieveShareDrinkResponse(self, response):
        #compiler placeholder
        1 + 1

    def playGameRequest(self, initiatorSSN):
        #compiler placeholder
        return (1, 2, 3)
        
    def recievePlayGameResponse(self, response):
        #compiler placeholder
        1 + 1
        
    def fightingWith(self, initiatorSSN):
        #compiler placeholder
        return (1, 2, 3)
        
    def fightResponse(self, response):
        #compiler placeholder
        1 + 1
        
    def askForFood(self, initiatorSSN):
        #compiler placeholder
        return (1, 2, 3)
        
    def askForFoodResponse(self, response):
        #compiler placeholder
        1 + 1
        
    def askForWater(self, initiatorSSN):
        #compiler placeholder
        return (1, 2, 3)
        
    def askForWaterResponse(self, response):
        #compiler placeholder
        1 + 1
        
    def askForCash(self, initiatorSSN):
        #compiler placeholder
        return (1, 2, 3)
        
    def askForCashResponse(self, response):
        #compiler placeholder
        1 + 1