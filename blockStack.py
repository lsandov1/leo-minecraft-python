from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 16
y = 110
z = 12
blockType = 103
mc.setBlock(x, y, z, blockType)
y = y + 1
mc.setBlock(x, y, z, blockType)
y = y + 1
mc.setBlock(x, y, z, blockType)
