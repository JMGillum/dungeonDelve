# import level
import floor
import random
from datetime import datetime


# def convertListToString(ls):
#     string = ""
#     for item in ls:
#         string += item
#     return string



# screen = level.Screen()
# print(f"Width: {screen.width} Height: {screen.height}")

# floor = level.Floor()
# print(convertListToString(floor.combineRooms()))

# star = ""
# for i in range(screen.width):
#     star += "*"
# print(star)

# floor.generateHalls()
# print(convertListToString(floor.combineHalls()))

random.seed(datetime.now().timestamp())

level = floor.Floor()
level.setSize(80,24)
level.generateRooms()
