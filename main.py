import level



screen = level.Screen()
print(f"Width: {screen.width} Height: {screen.height}")

floor = level.Floor()
floor.listRooms()

ls = floor.combineRooms()
floorStr = ""
for item in ls:
    floorStr += item

print(floorStr)

"""
room = level.Room(26,10)
room.generate()
roomList = room.getRoom()
roomStr = ""
for item in roomList:
    roomStr += item

print(f"Cell Width: 26 Cell Height: 10 PadTop: {room.padTop} PadLeft: {room.padLeft} Width: {room.width} Height: {room.height}")
print(roomStr)
"""
