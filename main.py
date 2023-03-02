import level


"""
f1 = level.Floor()
screen = level.Screen()
screen.displayRooms(f1.rooms)



#"" "
f1 = Floor()
for item in f1.rooms:
    for i in range(item.height+2):
        print(item.getLine(i,True))
#r1 = Room()
#for i in range(r1.height+2):
#    print(r1.displayRoom(True,True,i))
"""

screen = level.Screen()
print(f"Width: {screen.width} Height: {screen.height}")

room = level.Room()
roomList = room.generate(26, 10)
roomStr = ""
for item in roomList:
    roomStr += item

print(f"Cell Width: 26 Cell Height: 10 PadTop: {room.padTop} PadLeft: {room.padLeft} Width: {room.width} Height: {room.height}")
print(roomStr)
