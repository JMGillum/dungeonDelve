import math
import random
import getData
from datetime import datetime
from room import Room

custom = getData.Customization()

class Floor:
    def __init__(self):
        self.cellWidth = math.floor(78/3)
        self.cellHeight = math.floor(30/3)
        self.types = {"hall":0,
             "normal":1,
             "treasure":2,
             "stairs":3
             }

    def setSize(self,width,height):
        self.width = width
        self.cellWidth = math.floor(width/3)
        self.height = height
        self.cellHeight = math.floor(height/3)

    def generateRooms(self):
        
        random.seed(datetime.now().timestamp())

        numRooms = 9 # Number of rooms in map. Should be a square number.
        
        self.rooms = [] # Stores lists of room objects. Each item is a list containing room of objects. Each item is a row.
        tempRooms = [] # Used to store room type during generation
        chanceHall = 20 # Percent chance a normal room will be converted into a hall
        minRooms = 7 # Minimum number of rooms on map
        numHalls = 0 # Number of hall rooms found (abscence of a room)
        for i in range(numRooms):
            tempRooms.append(self.types["normal"])

        tempRooms[random.randint(0,numRooms-1)] = self.types["stairs"]
        while True:
            if((numRooms - numHalls) > minRooms and random.randint(1,100) <= chanceHall):
                while True:
                    location = random.randint(0,numRooms-1)
                    if(tempRooms[location] == self.types["normal"]):
                        tempRooms[location] = self.types["hall"]
                        numHalls = numHalls + 1
                        break
            else: 
                break
        
        for i in range(numRooms):
            currentRoom = Room(self.cellWidth,self.cellHeight)
            
            if(tempRooms[i] == self.types["hall"]):
                currentRoom.generateHall()
            elif(tempRooms[i] == self.types["stairs"]):
                currentRoom.generateStairs()
            else:
                currentRoom.generate()
                
            currentRoom.print()


        

    def combineRooms(self):
        self.floor = []
        for i in range(3):
            for j in range(self.cellHeight):
                line = []
                for k in range(3):
                    line += self.rooms[(3*i)+k].getLine(j)
                    if(k < 2):
                        del line[-1]
                self.floor += line
        return self.floor

    def listRooms(self):
        for item in self.rooms:
            print(f"Cell Width: 26 Cell Height: 10 PadTop: {item.padTop} PadLeft: {item.padLeft} Width: {item.width} Height: {item.height}")
            for i in range(10):
                print(item.getLine(i))
    