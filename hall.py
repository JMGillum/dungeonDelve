

class Hall:
    def __init__(self):
        self.width = -1
        self.height = -1
        self.map = []
    

    def generate(self,startX,endX,startY,endY):
        self.width = abs(startX-endX) + 1
        self.height = abs(startY-endY) + 1

        string = ""
        for i in range(self.width):
            string = string + "#"
        
        print(string)