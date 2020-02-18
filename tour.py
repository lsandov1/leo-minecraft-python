# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# Set x, y, and z variables to represent coordinates
x = 10
y = 110
z = 12

#Change the player's position
mc.player.setTilePos(x, y, z)

# Wait 10 seconds
time.sleep(10)

#Set x, y, and z variables to represent cordinates
x = 15
y = 120
z = 20

#Change the player's position
mc.player.setTilePos(x, y, z)

# Wait 5 seconds
time.sleep(10)

#Set x, y, and z variables to represent cordinates
x = 25
y = 110
z = 17

