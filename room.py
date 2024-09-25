import random
import getData
import os

custom = getData.Customization()

class Room:
    def __init__(self, width, height):
        self.cellWidth = width
        self.cellHeight = height
        self.width = -1
        self.height = -1
        self.positionX = -1
        self.positionY = -1
        self.map = []
        self.halls = []
        self.type = 0 # empty, normal, stairs
        
    
    def generate(self):
        """
        Generates a regular room. Places it at a random spot within its cell.
        """
        self.width = random.randint(4,self.cellWidth)
        self.height = random.randint(4,self.cellHeight)
        
        # print(f"cell:{self.cellWidth}, width:{self.width}")
        self.positionX = random.randint(0,self.cellWidth-self.width)
        self.positionY = random.randint(0,self.cellHeight-self.height)

        self.map = []
        self.type = 1
        # Top wall
        line = custom.cornerWall
        for i in range(self.width - 2):
            line = line + custom.topWall
        line = line + custom.cornerWall

        self.map.append(line)

        # Rows with floor.
        for row in range(self.height-2):
            line = custom.leftWall
            for col in range(self.width-2):
                line = line + custom.floor
            line = line + custom.rightWall
            self.map.append(line)
        
        # Bottom wall
        line = custom.cornerWall
        for i in range(self.width - 2):
            line = line + custom.bottomWall
        line = line + custom.cornerWall

        self.map.append(line)

    


    def generateStairs(self):
        """
        Generates a room with stairs in it
        """
        self.generate()
        x = random.randint(1,self.width-2)
        y = random.randint(1,self.height-2)

        line = self.map[y]
        line = list(line)
        line[x] = custom.stairs
        line = "".join(line)
        self.map[y] = line
        self.type = 2

        

    def generateHall(self):
        """
        Generates a nonexistent room.
        """
        self.width = -1
        self.height = -1
        self.positionX = -1
        self.positionY = -1
        self.map = []
        self.type = 0
    

    def placeDoor(self,x,y):
        """
        Places a door at the specified coordinates, if they are valid
        """
        if(self.type):
            if((x >= 0 and x < self.width) and (y >= 0 and y < self.height)):
                line = list(self.map[y])
                line[x] = custom.door
                line = "".join(line)
                self.map[y] = line
                self.halls.append([x,y])


    def print(self):
        """
        Prints out every character in the map
        """
        for line in self.map:
            for character in line:
                print(character, end='')
            print("")
    
    def getline(self,n):
        """
        Returns the line at index n. If n is out of bounds, returns empty string
        """
        if(n >= 0 and n < self.height):
            return self.map[n]
        else:
            return ""
    
    def getlineOffset(self,n):
        """
        Pads the room with empty space where needed to fill cell. Returns line this way. Returns empty string if outside of cell bounds
        """
        if(n < 0 or n >= self.cellHeight):
            return ""
        elif(n < (self.positionY) or n >= self.positionY + self.height):
            return "".zfill(self.cellWidth).replace("0"," ")
        else:
            beginning = "".zfill(self.positionX).replace("0"," ")
            end = "".zfill(self.cellWidth-self.positionX-self.width).replace("0"," ")
            return beginning + self.getline(n-self.positionY) + end

