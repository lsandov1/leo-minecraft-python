from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()

# coordinates
#
#  6=(-1,0,1) 7=(0,0,1) 8=(1,0,1) 
#  5=(-1,0,0) (x,y,z) 1 =(1,0,0) 
#  4=(-1,0,-1) 3=(0,0,-1) 2=(1,0,-1)

x = pos.x
y = pos.y
z = pos.z
blockType = 1

# 1
mc.setBlock(x+1, y, z, blockType)

#2
mc.setBlock(x+1, y, z-1, blockType)

#3
mc.setBlock(x, y, z-1, blockType)

#4
mc.setBlock(x-1, y, z-1, blockType)

#5
mc.setBlock(x-1, y, z, blockType)

#6
mc.setBlock(x-1, y, z+1, blockType)

#7
mc.setBlock(x, y, z+1, blockType)

#8
mc.setBlock(x+1, y, z+1, blockType)
