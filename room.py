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
        self.generate()
        x = random.randint(1,self.width-2)
        y = random.randint(1,self.height-2)

        line = self.map[y]
        line = list(line)
        line[x] = custom.stairs
        line = "".join(line)
        self.map[y] = line

        

    def generateHall(self):
        self.generate()
        x = random.randint(1,self.width-2)
        y = random.randint(1,self.height-2)

        line = self.map[y]
        line = list(line)
        line[x] = "H"
        line = "".join(line)
        self.map[y] = line
    

    def placeDoors(self,location):
        """
        Location should be a string that contains at most one of each: NWSE
        These are the cardinal directions corresponding to the side of the room that a door will be placed
        """

        self.halls = [] # Stores the coordinates of each door. stored as [x,y]
        x = -1
        y = -1

        # Picks a random location along one of the walls, and places a door there. Then appends to list of hallways
        if(location.find('N') >= 0):
            x = random.randint(1,self.width-2)
            y = 0 
            self.halls.append([x,y])

        if(location.find('S') >= 0):
            x = random.randint(1,self.width-2)
            y = self.height-1
            self.halls.append([x,y])

        if(location.find('W') >= 0):
            x = 0
            y = random.randint(1,self.height-2) 
            self.halls.append([x,y])
            
        if(location.find('E') >= 0):
            x = self.width-1
            y = random.randint(1,self.height-2) 
            self.halls.append([x,y])
            
        # Loops through each item in the hallway coordinates, and places a door there
        for item in self.halls:
            line = self.map[item[1]]
            line = list(line)
            line[item[0]] = custom.door
            line = "".join(line)
            
            self.map[item[1]] = line
            print(f"HALL: x:{item[0]},y:{item[1]}")


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

