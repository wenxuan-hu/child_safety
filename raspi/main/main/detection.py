import time
import display
import temp
#detection
import os

tempVal = 0
child = 0
pet = 0
counter = 59    # counter set to 59 so that the temp updates at startup


#added by wenxuan, detection
#------------------------------------------------------------
os.system('/home/pi/Workspaces/prj/run/run.sh')

#-----------------------------------------------------------
f = open("/home/pi/Workspaces/prj/run/result")
for line in f:
    print(line.strip())
f.close()

print(line)