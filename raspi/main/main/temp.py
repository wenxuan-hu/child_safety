from http.client import TEMPORARY_REDIRECT
import time
import os

# This function reads the temperature from STM32 whenever called
def readTemp():
    os.system('/home/pi/Workspaces/prj/run/trigger_spi.sh')
    
    f=open('/home/pi/Workspaces/prj/run/spi_rx') 

    line = None 
    for line in f:
        tempRead = int(line)
        #print("you entered: " + tempRead)
        #print("you entered: " + line.strip())
    f.close()
    
    #tempRead = int(input("Enter a temperature: "))
    #print("you entered: " + str(tempRead))
    
    return tempRead
    