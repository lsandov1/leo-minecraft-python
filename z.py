from mcpi.minecraft import Minecraft
mc=Minecraft.create()
pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
blockType=1
mc.getBlock(x,y,z,blockType)

