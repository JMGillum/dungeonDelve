import random, os, math
    
class Screen:
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines

                
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
    
    def generateHalls(self):
        hall = Hall(self.rooms[0], self.rooms[1], self.cellWidth, self.cellHeight)


class Room:
    def __init__(self, width, height):
        self.cellWidth = width
        self.cellHeight = height
    
    def generate(self):
        self.width = random.randrange(8,self.cellWidth-1)
        self.height = random.randrange(5,self.cellHeight-1)
        self.padLeft = random.randrange(1,self.cellWidth-self.width)
        self.padTop = random.randrange(1,self.cellHeight-self.height)
        self.floor = []
        for line in range(1, self.cellHeight+1):
            if(line <= self.padTop or line > (self.padTop+self.height)):
                for character in range(1, self.cellWidth + 1):
                    if(character == self.cellWidth or character == 1):
                        self.floor.append("|")
                    else:
                        if(line == 1 or line == self.cellHeight):
                            self.floor.append("-")
                        else:
                            self.floor.append(" ")
            elif (line == self.padTop + 1 or line == self.padTop + self.height):
                for character in range(1, self.cellWidth + 1):
                    if (character <= self.padLeft or character > self.padLeft + self.width):
                        if(character == self.cellWidth or character == 1):
                            self.floor.append("|")
                        else:
                            self.floor.append(" ")
                    else:
                        self.floor.append("@")
            else:
                for character in range(1, self.cellWidth+1):
                    if (character <= self.padLeft or character > self.padLeft + self.width):
                        if(character == self.cellWidth or character == 1):
                            self.floor.append("|")
                        else:
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
    def __init__(self, room1, room2, width, height):
        self.room1 = room1
        self.room2 = room2
        self.cellWidth = width
        self.cellHeight = height
        self.startX = room1.padLeft + room1.width
        self.startY = random.randrange(2,room1.height) + room1.padTop
        self.endX = room2.padLeft + 1
        self.endY = random.randrange(2,room2.height) + room2.padTop
        self.deltaX = (self.cellWidth - self.startX) + self.endX
        self.deltaY = self.startY - self.endY

        print(f"StartX: {self.startX} StartY: {self.startY} EndX: {self.endX} EndY: {self.endY} DeltaX: {self.deltaX} DeltaY: {self.deltaY}")
        self.generate()

    def generate(self):
        pass
