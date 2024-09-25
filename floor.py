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
        self.halls = []
        self.map = []
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
                
                # currentRoom.randomDoors("NWSE")
                line.append(currentRoom)
            self.layout.append(line)
        
        self.generateMap()
        self.print()
        self.connectRooms(0,0,0,1)
        print("_____________________________")
        self.generateMap()
        self.print()


    def print(self):
        for row in self.map:
            for col in row:
                print(f"{col}",end="")
            print("")
        
    
    def generateMap(self):
        self.map = []
        for row in self.layout:
            for line in range(self.cellHeight):
                string = []
                for item in row:
                    l = list(item.getlineOffset(line))
                    # print(l)
                    string = string + l
                # for char in string:
                #     print(char,end="")
                # print("")
                self.map.append(string)
        
        for hall in self.halls:
            hallMap = hall.map
            for row in range(hall.height):
                line = self.map[hall.positionY + row]
                # print(line)
                for col in range(hall.width):
                    # print(f"col:{col} pos:{hall.positionX}")
                    if(not hallMap[row][col] == custom.empty):
                        line[col+hall.positionX] = hallMap[row][col]
                self.map[hall.positionY + row] = line

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
        
        else:
            if(row1 == row2):
                if(col1 > col2):
                    self.connectRooms(row2,col2,row1,col1)
                else:
                    hall = Hall()
                    startX = room1.positionX + room1.width - 1
                    startY = random.randint(1,room1.height-2)
                    endX = room2.positionX + self.cellWidth
                    endY = random.randint(1,room2.height-2)
                    print(f"startX:{startX} startY:{startY} endX:{endX} endY:{endY}")
                    hall.generate(startX,endX,startY + room1.positionY,endY + room2.positionY)
                    positionX = startX
                    positionY = startY + room1.positionY
                    if(endY + room2.positionY < positionY):
                        positionY = endY + room2.positionY
                    hall.place(positionX,positionY)
                    self.halls.append(hall)
                    print(f"startX:{startX} startY:{startY + room1.positionY} endX:{endX} endY:{endY + room2.positionY}")
                    self.layout[row1][col1].placeDoor(room1.width-1,startY)
                    self.layout[row2][col2].placeDoor(0,endY)


    