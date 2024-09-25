import math
import random
import getData
from datetime import datetime
from room import Room
from hall import Hall

custom = getData.Customization()

class Floor:
    def __init__(self):
        self.cellWidth = math.floor(78/3) # 26
        self.cellHeight = math.floor(24/3) # 8
        self.types = {"hall":0,
             "normal":1,
             "treasure":2,
             "stairs":3
             }
        self.layout = []
        self.size = 3 # 3 x 3 rooms

    def setSize(self,width,height):
        self.width = width
        self.cellWidth = math.floor(width/self.size)
        self.height = height
        self.cellHeight = math.floor(height/self.size)

    def generateRooms(self):
        
        random.seed(datetime.now().timestamp())

        numRooms = self.size * self.size # Number of rooms in map. Should be a square number.
        
        self.rooms = [] # Stores lists of room objects. Each item is a list containing room of objects. Each item is a row.
        tempRooms = [] # Used to store room type during generation
        chanceHall = 50 # Percent chance a normal room will be converted into a hall
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
        
        # Generates rooms based on their type, and appends to rooms list
        for row in range(self.size):
            line = []
            for col in range(self.size):
                index = row*self.size + col # Index of tempRooms[]
                currentRoom = Room(self.cellWidth,self.cellHeight)
                
                if(tempRooms[index] == self.types["hall"]):
                    currentRoom.generateHall()
                elif(tempRooms[index] == self.types["stairs"]):
                    currentRoom.generateStairs()
                else:
                    currentRoom.generate() # Defaults to generating a normal room
                
                currentRoom.placeDoors("NWSE")
                line.append(currentRoom)
            self.layout.append(line)
        
        
        for row in self.layout:
            for line in range(self.cellHeight):
                string = ""
                for item in row:
                    string = string + item.getlineOffset(line)
                print(string)
        
        self.connectRooms(0,0,0,1)

    def connectRooms(self,row1,col1,row2,col2):
        """
        Connects the room at self.layout[row1][col1] to self.layout[row2][col2]
        """
        
        room1 = self.layout[row1][col1]
        room2 = self.layout[row2][col2]

        if(not room1.type):
            if(room2.type):
                self.connectRooms(row2,col2,row1,col1)
            else:
                return
        elif(not room2.type):
            return
        
        if(row1 == row2):
            if(col1 > col2):
                self.connectRooms(row2,col2,row1,col1)
            else:
                hall = Hall()
                startX = room1.positionX + room1.width - 1
                startY = room1.positionY + random.randint(0,room1.height)
                endX = room2.positionX + self.cellWidth
                endY = room2.positionY + random.randint(0,room2.height)
                print(f"startX:{startX} startY:{startY} endX:{endX} endY:{endY}")
                hall.generate(startX,endX,startY,endY)


    