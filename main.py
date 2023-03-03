import level



screen = level.Screen()
print(f"Width: {screen.width} Height: {screen.height}")

floor = level.Floor()

ls = floor.combineRooms()
floorStr = ""
for item in ls:
    floorStr += item

print(floorStr)
star = ""
for i in range(78):
    star += "*"
print(star)
floor.generateHalls()
ls = floor.combineHalls()
floorStr = ""
for item in ls:
    floorStr += item

print(floorStr)

hallV = level.HallVertical(floor.rooms[0],floor.rooms[3],floor.cellWidth,floor.cellHeight)
print(hallV.getHall())
for i in range(floor.cellHeight * 2):
    print(hallV.getLine(i))
