import math
import getData


custom = getData.Customization()

class Hall:
    def __init__(self):
        self.width = -1
        self.height = -1
        self.map = []
    

    def generate(self,startX,endX,startY,endY):
        self.width = abs(startX-endX) + 1
        self.height = abs(startY-endY) + 1

        type = 0 # 0 = S hall


        if(type == 0):
            if(startY < endY):
                sType = 0 # Z
            elif(startY > endY):
                sType = 1 # S
            else:
                sType = 2 # - (straight line)

        
            string = []
            if(sType == 0):
                for line in range(self.height):
                    string = []
                    middle = math.floor(self.width/2)
                    for col in range(self.width):
                        if((line == 0 and col <= middle) or (line == self.height - 1 and col > middle) or (col == middle)):
                            string.append(custom.hallMiddle)
                        else:
                            string.append(custom.empty)
                    self.map.append(string)
                            
            elif(sType == 1):
                for line in range(self.height):
                    string = []
                    middle = math.floor(self.width/2)
                    for col in range(self.width):
                        if((line == 0 and col > middle) or (line == self.height - 1 and col <= middle) or (col == middle)):
                            string.append(custom.hallMiddle)
                        else:
                            string.append(custom.empty)
                    self.map.append(string)
            else:
                for i in range(self.width):
                    string.append(custom.hallMiddle)
        self.print()

    def print(self):
        if(self.map):
            for line in self.map:
                for char in line:
                    print(f"{char}",end="")
                print()
