# Import the api
from mcpi_addons.minecraft import Minecraft
# Initialize the api (MCPI must be open and in a world at
# this time)
mc = Minecraft.create()
mc.postToChat("Hello World!")
x = input("X Coordinate: ")
y = input("Y Coordinate: ")
z = input("Z Coordinate: ")
x = int(x)
y = int(y)
z = int(z)
length = 22
width = 22
height = 12
mc.setBlocks(x,y,z, x + width, y + height, z+length, 19)
mc.setBlocks(x,y ,z , x + width-5, y + height-5, z+length-5, 0)
# 98 7 100

