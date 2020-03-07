import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:    
    mc.setBlock(-121,101,193, 46)
    time.sleep(1)
