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
        #self.roomCount = random.randrange(5,10)
        self.roomCount = 9
        print(self.roomCount)
        self.generateRooms()
    def generateRooms(self):
        self.rooms = []
        for i in range(self.roomCount):
            self.rooms.append(Room())
            print(self.rooms[-1].getRoom())
        print(self.rooms)

class Room:
    def __init__(self):
        self.width = random.randrange(5,26)
        self.height = random.randrange(3,8)
        self.floor = []
        for i in range(self.width*self.height):
            self.floor.append(" ")
    def fillRoom(self, type = 0):
        """
        Types can be:
            1 ~ room does not exist
            2 ~ empty room
            3 ~ store room
            4 ~ monster room
            5 ~ maze
        """
        if not type == 0:
            weight = [4,19,44,94,99]
            roll = random.randrange(100)
            if roll <= weight[1]:
                self.type = 1
            elif roll <= weight[2]:
                self.type = 2
            elif roll <= weight[3]:
                self.type = 3
            elif roll <= weight[4]:
                self.type = 4
            elif roll <= weight[5]:
                self.type = 5
            else:
                self.type = 4
        else:
            self.type = type
        
    def getRoom(self, border = False):
        if(border):
            room = []
            index = 0
            for i in range(self.height + 2):
                if i == 0 or i == self.height +1:
                    for j in range(self.width + 2):
                        room.append("@")
                else:
                    room.append("@")
                    for j in range(self.width):
                        room.append(self.floor[index])
                        index += 1
                    room.append("@")
                room.append("\n")
            return room
        else:
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
    def spawn(self, type = " "):
        self.floor[random.randrange(len(self.floor))] = type


class Hall:
    def __init__(self, room1, room2):
        self.generate(self, room1, room2)
    
    def generate(self, room1, room2):
        pass