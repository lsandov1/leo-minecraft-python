from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 12
y = 110
z = 12
blockType = 103
up = 1
mc.setBlock(x, y, z, blockType)
mc.setBlock(x, y + up, z, blockType)
