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
        self.hallsHorizontal = []
        for i in range(3):
            for j in range(2):
                self.hallsHorizontal.append(Hall(self.rooms[(i*3)+j], self.rooms[(i*3)+j+1], self.cellWidth, self.cellHeight))
                for k in range(10):
                    print(self.hallsHorizontal[j].getLine(k))
    
    def combineHalls(self):
        self.newFloor = []
        for item in range(len(self.hallsHorizontal)):
            start = self.hallsHorizontal[item].startX + (26 * (item%2))
            end = 26 + self.hallsHorizontal[item].endX + (26 * (item%2))
            print(f"Start: {start} End: {end}")
            for i in range(10):
                line = i
                section = []
                index = line*((self.cellWidth*3)+1)
                for k in range((self.cellWidth*3)+1):
                    section.append(self.floor[index])
                    index += 1
                
                hallList = self.hallsHorizontal[item].getLine(line)
                print(hallList)
                #print(len(hallList))
                #print(len(section))
                for j in range(start,end):
                    #print(f"Line: {line} Spot: {j} Value: {hallList[j-start]}, Start: {start}, End: {end}")
                    if(not(hallList[j-start] == " ")):
                        section[j] = hallList[j-start]
                self.newFloor += section
        return self.newFloor



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
        self.startX = room1.padLeft + room1.width - 1
        self.startY = random.randrange(2,room1.height) + room1.padTop
        self.endX = room2.padLeft + 1
        self.endY = random.randrange(2,room2.height) + room2.padTop
        self.deltaX = (self.cellWidth - self.startX) + self.endX
        self.deltaY = self.startY - self.endY

        print(f"StartX: {self.startX} StartY: {self.startY} EndX: {self.endX} EndY: {self.endY} DeltaX: {self.deltaX} DeltaY: {self.deltaY}")
        self.generate()

    def generate(self):
        self.floor = []
        startIsLower = self.startY >= self.endY
        print(startIsLower)
        for line in range(1, self.cellHeight + 1):
            if(line < self.startY and line < self.endY):
                for character in range(self.deltaX):
                    self.floor.append(" ")
            else:
                if(line == self.startY or line == self.endY):
                    for character in range(self.deltaX):
                        if (line == self.startY and line == self.endY):
                            self.floor.append("#")
                        elif(line == self.startY):
                            if character <= math.floor(self.deltaX/2):
                                self.floor.append("#")
                            else:
                                self.floor.append(" ")
                        elif (line == self.endY):
                            if character >= math.floor(self.deltaX/2):
                                self.floor.append("#")
                            else:
                                self.floor.append(" ")
                else:
                    if(not(self.startY == self.endY)):
                        for character in range(self.deltaX):
                            if(character == math.floor(self.deltaX/2) and ((self.startY <= line <= self.endY) or (self.endY <= line <= self.startY))):
                                self.floor.append("#")
                            else:
                                self.floor.append(" ")
                    else:
                        for character in range(self.deltaX):
                            self.floor.append(" ")
            self.floor.append(os.linesep)
    
    def getHall(self):
        return self.floor
    
    def getLine(self,line):
        section = []
        index = line*(self.deltaX+1)
        try:
            for i in range(self.deltaX+1):
                section.append(self.floor[index])
                index += 1
            return section
        except IndexError:
            print("ERROR GETTING LINE FROM HALL")
            return None
