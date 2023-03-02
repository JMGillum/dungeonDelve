import random, os, math
    
class Screen:
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines
    """
    def displayRooms(self, rooms):
        screen = []

        
        for j in range(5):
            line = []
            line += rooms[0].getLine(j,True)
            line += rooms[1].getLine(j,True)
            line += rooms[2].getLine(j,True)
            line.append("\n")
            screen += line
        
        
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
                    
                    try:
                        line += rooms[i*3+k].getLine(j,True)
                    except ValueError:
                        for l in range(rooms[i*3+k].width + 2):
                            line.append("V")
                    line.append("   ")
                line.append("\n")
                screen += line
            screen.append("\n\n\n")
        
        print(screen)
        screenStr = ""
        for item in screen:
            screenStr += item
        print(screenStr)
        """

                
class Floor:
    def __init__(self):
        self.cellWidth = math.floor(78/3)
        self.cellHeight = math.floor(30/3)
        self.generateRooms()
    def generateRooms(self):
        self.rooms = []
        for i in range(9):
            self.rooms.append(Room(self.cellWidth,self.cellHeight))
            self.rooms[-1].generate()
            print(self.rooms[-1].getRoom())
        #print(self.rooms)
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

class Room:
    def __init__(self, width, height):
        self.cellWidth = width
        self.cellHeight = height
        pass
    def generate(self):
        self.width = random.randrange(8,self.cellWidth-1)
        self.height = random.randrange(5,self.cellHeight-1)
        self.padLeft = random.randrange(1,self.cellWidth-self.width)
        self.padTop = random.randrange(1,self.cellHeight-self.height)
        self.floor = []
        for line in range(1, self.cellHeight+1):
            if(line <= self.padTop or line > (self.padTop+self.height)):
                for character in range(1, self.cellWidth + 1):
                    self.floor.append(" ")
            elif (line == self.padTop + 1 or line == self.padTop + self.height):
                for character in range(1, self.cellWidth + 1):
                    if (character <= self.padLeft or character > self.padLeft + self.width):
                        self.floor.append(" ")
                    else:
                        self.floor.append("@")
            else:
                for character in range(1, self.cellWidth+1):
                    if (character <= self.padLeft or character > self.padLeft + self.width):
                        self.floor.append(" ")
                    elif (character == self.padLeft + 1 or character == self.padLeft + self.width):
                        self.floor.append("@")
                    else:
                        self.floor.append(" ")
            self.floor.append(os.linesep)
    def getRoom(self):
        return self.floor
    def getLine(self, line):
        section = []
        index = line*(self.cellWidth+1)
        try:
            for i in range(self.cellWidth+1):
                section.append(self.floor[index])
                index += 1
            return section
        except IndexError:
            return None
        


class Hall:
    def __init__(self, room1, room2):
        self.generate(self, room1, room2)
    
    def generate(self, room1, room2):
        pass