from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
width = 10
height = 5
length = 6

air = 1

# LEO JR
### solid (out)
##blockType = 4
##delta = 1 
##mc.setBlocks(x, y, z, x + width+delta, x + width-delta, y + height + delta, y + height - delta, z + length + delta, z + length - delta, blockType)
##
### air (in)
##blockType = 0
##delta = -1
##mc.setBlocks(x, y, z, x + width+delta, y + height + delta, z + length + delta, blockType)


# solution from hint (book, page 61)
# solid (out)
blockType = 4
delta = 1
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)

# air (in)
blockType = 0
delta = -1
mc.setBlocks(x+1, y+1, z+1, x + width + delta, y + height + delta, z + length + delta, blockType)


