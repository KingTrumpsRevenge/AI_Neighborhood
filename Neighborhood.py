# -*- coding: utf-8 -*-

from random import random, randint

class Map():

    def __init__(self):
        self.people = []
        self.height = 1000
        self.width = 1000
        self.Year = 0
        self.Month = 0
        self.Day = 0
        self.Hour = 0
        self.Minute = 0
        self.Second = 0
        self.locations = []
        self.initLocations()
        
    def initLocations(self):
        row = []
        #populate rows
        for i in range (0, self.height):
            #populate columns
            for j in range (0, self.width):
                row.append(Location())
            self.locations.append(row)
            row = []

    def performAction(self, initiatingPerson, initiatingLocation, actionParameters):
        #--4--Private correspondance, Conversation, Announcement, 
        #--6--WithAncestor, WithParent, WithSibling, WithMate, WithFriend, With Aquaintence, trust floor
        #--6--Ask for food, Ask for Water, Ask for cash, offer food, offer water, offer cash
        #--5--Move-Up, Move-Down, Move-Left, Move-Right, stay put
        #--4--eat, drink, sleep, do nothing
        #--7--flirt, chat, share meal, reproduce, share drinks, play game, fight
        
        #0 = privateCorrespondance(SOFTMAX(WithAncestor, WithParent, WithSibling, WithMate, WithFriend, With Aquaintence), 
        #                          trustFloor, 
        #                          Rectifier(flirt, chat, share meal, reproduce, share drinks, play game, fight, ask for food, ask for water, ask for cash)
        #1 = conversation(SOFTMAX(chat, share meal, share drinks, play game, fight, ask for food, ask for water, ask for cash))
        #2 = announcement(SOFTMAX(share meal, share drinks, play game, ask for food, ask for water, ask for cash))
        #3 = move(SOFTMAX(up, right, down, left, stayPut))
        #4 = eat()
        #5 = drink()
        #6 = sleep()
        #7 = playGame()

        #compiler placeholder
        initiatingPerson = initiatingPerson + 1
        
    def privateCorrespondance(self, initiator, corresponderID, topics):
        #topics
        #--0--flirt
        #--1--chat
        #--2--share meal
        #--3--reproduce
        #--4--share drinks
        #--5--play game
        #--6--fight
        #--7--ask for food
        #--8--ask for water
        #--9--ask for cash
        corresponder = self.getPerson(corresponderID)
        for i in topics
            if i.topic is 0
                initiator.recieveFlirtResponse(reciever.flirtRequest(initiator.ssn))
            elif i.topic is 1
                initiator.recieveChatResponse(reciever.chatRequest(initiator.ssn))
            elif i.topic is 2:
                #send full initiator in case of food request
                initiator.recieveshareMealResponse(reciever.shareMealRequest(initiator))
            elif i.topic is 3:
                #full initiator in case flirt/chat request
                initiator.recieveReproduceResponse(reciever.reproduceRequest(initiator))
    def getPerson(self, id):
        
        #placeholder for compiler        
        return id
        