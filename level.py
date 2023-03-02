import random, os
    
class Screen:
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines
    def displayRooms(self, rooms):
        screen = []

        """
        for j in range(5):
            line = []
            line += rooms[0].getLine(j,True)
            line += rooms[1].getLine(j,True)
            line += rooms[2].getLine(j,True)
            line.append("\n")
            screen += line
        
        """
        for i in range(3):
            maxHeight = rooms[i*3].height
            if rooms[i*3+1].height > maxHeight:
                maxHeight = rooms[i*3+1].height
            if rooms[i*3+2].height > maxHeight:
                maxHeight = rooms[i*3+2].height
            
            print(f"Max: {maxHeight}, HxW {rooms[i*3].height}x{rooms[i*3].width} {rooms[i*3+1].height}x{rooms[i*3+1].width} {rooms[i*3+2].height}x{rooms[i*3+2].width} ")

            for j in range(maxHeight+2):
                line = []
                for k in range(3):
                    section = rooms[i*3+k].getLine(j,True)
                    print(section)
                    if section is None:
                        for l in range(rooms[i*3+k].width + 2):
                            line.append("V")
                    else:
                        line += rooms[i*3+k].getLine(j,True)
                    """
                    try:
                        line += rooms[i*3+k].getLine(j,True)
                    except ValueError:
                        for l in range(rooms[i*3+k].width + 2):
                            line.append("V")
                    """
                    line.append("   ")
                line.append("\n")
                screen += line
            screen.append("\n\n\n")
        
        print(screen)
        screenStr = ""
        for item in screen:
            screenStr += item
        print(screenStr)


                
class Floor:
    def __init__(self):
        self.cellWidth = 78/3
        self.cellHeight = 30/3
        self.generateRooms()
    def generateRooms(self):
        self.rooms = []
        for i in range(9):
            self.rooms.append(Room())
            print(self.rooms[-1].getRoom())
        print(self.rooms)

class Room:
    def __init__(self):
        pass
    def generate(self,width,height):
        self.width = random.randrange(8,width-1)
        self.height = random.randrange(5,height-1)
        self.padLeft = random.randrange(1,width-self.width)
        self.padTop = random.randrange(1,height-self.height)
        self.floor = []
        for line in range(1, height+1):
            if(line <= self.padTop or line > (self.padTop+self.height)):
                for character in range(1, width + 1):
                    self.floor.append("p")
            elif (line == self.padTop + 1 or line == self.padTop + self.height):
                for character in range(1, width + 1):
                    if (character <= self.padLeft or character > self.padLeft + self.width):
                        self.floor.append("p")
                    else:
                        self.floor.append("@")
            else:
                for character in range(1, width+1):
                    if (character <= self.padLeft or character > self.padLeft + self.width):
                        self.floor.append("p")
                    elif (character == self.padLeft + 1 or character == self.padLeft + self.width):
                        self.floor.append("@")
                    else:
                        self.floor.append(" ")
            self.floor.append("\n")
    def getRoom(self):
        return self.floor
    def getLine(self, line, border = False):
        section = []
        index = line*self.width
        if(border):
            try:
                if line == 0 or line == self.height + 1:
                    for i in range(self.width + 2):
                        section.append("@")
                else:
                    section.append("@")
                    index = ((line-1) * self.width)
                    while(index < line*self.width):
                        section.append(self.floor[index])
                        index += 1
                    section.append("@")
            except IndexError:
                return None
        else:
            try:
                for i in range(self.width):
                    section.append(self.floor[index])
                    index += 1
            except IndexError:
                return None
        return section


class Hall:
    def __init__(self, room1, room2):
        self.generate(self, room1, room2)
    
    def generate(self, room1, room2):
        pass