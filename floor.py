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
        
        self.connectRooms(0,0,0,1)
        self.connectRooms(0,1,0,2)
        self.connectRooms(1,0,1,1)
        self.connectRooms(1,1,1,2)
        self.connectRooms(2,0,2,1)
        self.connectRooms(2,1,2,2)
        self.connectRooms(0,0,1,0)
        self.connectRooms(0,1,1,1)
        self.connectRooms(0,2,1,2)
        self.connectRooms(1,0,2,0)
        self.connectRooms(1,1,2,1)
        self.connectRooms(1,2,2,2)
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
                    try:
                        if(not hallMap[row][col] == custom.empty):
                            line[col+hall.positionX] = hallMap[row][col]
                    except IndexError:
                        pass
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
                    startX = room1.positionX + room1.width - 1 + self.cellWidth*col1
                    startY = random.randint(1,room1.height-2) + self.cellHeight*row1
                    endX = room2.positionX + self.cellWidth*col2
                    endY = random.randint(1,room2.height-2) + self.cellHeight*row2
                    # print(f"startX:{startX} startY:{startY} endX:{endX} endY:{endY}")
                    hall.generate(startX,endX,startY + room1.positionY,endY + room2.positionY)
                    # hall.print()
                    positionX = startX
                    positionY = startY + room1.positionY
                    if(endY + room2.positionY < positionY):
                        positionY = endY + room2.positionY
                    hall.place(positionX,positionY)
                    self.halls.append(hall)
                    # print(f"startX:{startX} startY:{startY + room1.positionY} endX:{endX} endY:{endY + room2.positionY}")
                    self.layout[row1][col1].placeDoor(room1.width-1,startY)
                    self.layout[row2][col2].placeDoor(0,endY)
            elif(col1 == col2):
                if(row1 > row2):
                    self.connectRooms(row2,col2,row1,col1)
                else:
                    hall = Hall()
                    startX = random.randint(1,room1.width-2) + self.cellWidth*col1
                    startY = room1.positionY + room1.height - 1 + self.cellHeight*row1
                    endX = random.randint(1,room2.width-2) + self.cellWidth*col2
                    endY = room2.positionY + self.cellHeight*row2
                    print(f"startX:{startX} startY:{startY} endX:{endX} endY:{endY}")
                    hall.generate(startX + room1.positionX,endX + room2.positionX,startY,endY,1)
                    hall.print()
                    print(f"startX:{startX + room1.positionX} startY:{startY + room1.positionY} endX:{endX + room2.positionX} endY:{endY + room2.positionY}")
                    positionX = startX + room1.positionX
                    positionY = startY
                    if(endX + room2.positionX < positionX):
                        positionX = endX + room2.positionX
                    hall.place(positionX,positionY)
                    self.halls.append(hall)
                    
                    self.layout[row1][col1].placeDoor(startX,room1.height-1)
                    self.layout[row2][col2].placeDoor(endX,0)
            


    