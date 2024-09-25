import math
import getData


custom = getData.Customization()

class Hall:
    def __init__(self):
        self.width = -1
        self.height = -1
        self.map = [] # List of lists of lines (characters) Ex: [['#','#',' '],[' ','#',' '],[' ','#','#']]
    

    def place(self,positionX,positionY):
        """
        Stores the starting location of the hall. (Upper left coordinate)
        """
        self.positionX = positionX
        self.positionY = positionY
    

    def generate(self,startX,endX,startY,endY,type=-1):
        """
        type of 0 is horizontal S, type of 1 is x^3
        """
        self.width = abs(startX-endX) + 1
        self.height = abs(startY-endY) + 1

        if(type == -1):
            type = 0 # 0 = S hall
        


        # Determines if the hall is shaped like a S, Z, or straight line
        if(type == 0):
            """
            Horizontal connection
            """
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
                    middle = math.floor(self.width/2) # The column with the vertical line
                    for col in range(self.width):
                        if((line == 0 and col <= middle) or (line == self.height - 1 and col > middle) or (col == middle)):
                            string.append(custom.hallMiddle)
                        else:
                            string.append(custom.empty)
                    self.map.append(string)
                            
            elif(sType == 1):
                for line in range(self.height):
                    string = []
                    middle = math.floor(self.width/2) # The column with the vertical line
                    for col in range(self.width):
                        if((line == 0 and col > middle) or (line == self.height - 1 and col <= middle) or (col == middle)):
                            string.append(custom.hallMiddle)
                        else:
                            string.append(custom.empty)
                    self.map.append(string)
            else:
                for i in range(self.width):
                    string.append(custom.hallMiddle)
                self.map.append(string)

        elif(type == 1):
            """
            Vertical connection
            """
            if(startX < endX):
                sType = 0 # x^3
            elif(startX > endX):
                sType = 1 # -x^3
            else:
                sType = 2 # - (straight line)

            string = []
            if(sType == 0): # down on left and up on right
                for line in range(self.height):
                    string = []
                    middle = math.floor(self.height/2) # The column with the vertical line
                    for col in range(self.width):
                        if((col == 0 and line <= middle) or (col == self.width - 1 and line > middle) or (line == middle)):
                            string.append(custom.hallMiddle)
                        else:
                            string.append(custom.empty)
                    self.map.append(string)
                            
            elif(sType == 1): # up on left and down on right
                for line in range(self.height):
                    string = []
                    middle = math.floor(self.height/2) # The column with the vertical line
                    for col in range(self.width):
                        if((col == 0 and line > middle) or (col == self.width - 1 and line <= middle) or (line == middle)):
                            string.append(custom.hallMiddle)
                        else:
                            string.append(custom.empty)
                    self.map.append(string)

            else: # Straight line
                for i in range(self.height):
                    string.append(custom.hallMiddle)
                self.map.append(string)


    def print(self):
        """
        Prints out the hall, irrespective of its position
        """
        if(self.map):
            for line in self.map:
                for char in line:
                    print(f"{char}",end="")
                print()
