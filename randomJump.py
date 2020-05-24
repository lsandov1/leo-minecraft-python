from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
x=x+random.randint(-100,100)
y=y+random.randint(-100,100)
z=z+random.randint(-100,100)
mc.player.setPos(x, y, z)
blockType=1
mc.setBlock(x,y-1,z,blockType)
