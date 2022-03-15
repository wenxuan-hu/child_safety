import time
import display
import Camera
import temp
import threading
import _thread


#-------------------------------------------
#initial
tempVal = 0
child = 0
pet = 0
counter = 0    # counter set to 59 so that the temp updates at startup

#--------------------------------------------------------------
#thread 1
#main loop
#function: display
def display_gui(threadName, delay):
    global tempVal
    global child
    global pet
    global counter
    while True:
        # Update GUI
        display.updateTemp(tempVal)
        display.updateChild(child)
        display.updatePet(pet)
        display.updateStat(tempVal, child, pet)
        display.alarmBut(tempVal, child, pet)
        display.gui.update()   


        print(tempVal)
        time.sleep(delay)
        #display.gui.mainloop()
        #delay every 1 minutes






#----------------------------------------------------------
#thread 2
#function: input the temp
def get_tmp(threadName, delay):
    global tempVal
    while True:
        tempVal = temp.readTemp()

        time.sleep(delay)

#delay in every2 minutes 


#----------------------------------------------------------
#thread 3
#function: image_proc
def image_proc(threadName, delay):
    global child
    global pet
    global counter
    while True:
        Camera.takePic()
        result=Camera.runDet()
            #------------------------
            #extra the type of object
        if(result == None):
            child = 0
        else:
            result_type =   result.split(":")[0]
            print(result_type)
            if(result_type == 'person'):
                child = 1
            else:
                child = 0
        time.sleep(delay)

#delay in every2 minutes 



_thread.start_new_thread(get_tmp,("temp",40))
_thread.start_new_thread(image_proc,("image",40))
display_gui("gui",10)

try:
    _thread.start_new_thread(get_tmp,("temp",40))
    #_thread.start_new_thread(display_gui,("gui",40))
    display_gui()
    #_thread.start_new_thread(image_proc,("image",40))
except:
    print ("Error!!!!!!!!!!!!!!!!!!!!!!!!!!!!      unable to start thread")

while 1:
    pass



#-------------------------------------------------------------
#triggle thread

