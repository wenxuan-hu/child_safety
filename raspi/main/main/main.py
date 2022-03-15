import time
import display
import Camera
import temp
import threading
import _thread
import textMsg

#-------------------------------------------


# Constants
WARNTIME = 20 # Amount of time disable the alarm until police are called
MAXTEMP = 10

# Variables
tempVal = 0
child = 0
pet = 0
sent = 0 # 1 when vehicle owner has been notified
police = 0 # 1 when police have been notified
currTime = time.time()
startTime = time.time()

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
        display.updateChild(child, tempVal)
        display.updatePet(pet, tempVal)
        display.updateStat(tempVal, child, pet, police)
        # display.alarmBut(tempVal, child, pet)
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
    global police
    while True:
        Camera.takePic()
        if (police == 0):
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


#----------------------------------------------------------
#thread 4
#function: send message
def send_message(threadName, delay):
    global tempVal
    global child
    global currTime
    global startTime
    global sent
    global police

    while True:
        if((tempVal > MAXTEMP) & (child == 1 | pet == 1) & (sent == 0)):
            textMsg.callSMS() #UNCOMMENT THIS! ITS JUST COMMENTED FOR TESTING
            print("Activating messaging system...")
            currTime = time.time()
            startTime=time.time()
            sent = 1

        if((tempVal > MAXTEMP) & (child == 1 | pet == 1) & (sent == 1) & (police == 0)):
            currTime = time.time()
            if(currTime - startTime > WARNTIME):
                police = 1
                print("Notifying Police!")

#delay in every2 minutes 


_thread.start_new_thread(send_message,("send_message_inst",10))
_thread.start_new_thread(get_tmp,("temp",10))
_thread.start_new_thread(image_proc,("image",40))
display_gui("gui",2)

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

