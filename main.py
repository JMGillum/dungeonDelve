import level



screen = level.Screen()
print(f"Width: {screen.width} Height: {screen.height}")

floor = level.Floor()

ls = floor.combineRooms()
floorStr = ""
for item in ls:
    floorStr += item

print(floorStr)

floor.generateHalls()
