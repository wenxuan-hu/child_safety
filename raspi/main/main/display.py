from distutils import command
import tkinter as tk
from turtle import exitonclick

MAXTEMP = 10

# create window and set name
gui = tk.Tk(className="Car Alarm Status")

# set window size
gui.geometry("1920x1080")
gui.config(bg='white')
gui.attributes('-fullscreen', True)

# Initial set-up
tempLab = 'Temperature:'
tempLabVar = tk.Message(gui, text=tempLab, width=800, font=("Arial", 90), bg='white')
tempLabVar.place(x=60, y=30)

detectStat = 'Detection:'
detectStatVar = tk.Message(gui, text=detectStat, width=800, font=("Arial", 90), bg='white')
detectStatVar.place(x=1000, y=30)

# safeStat ='Safety Status:'
# safeStatVar = tk.Message(gui, text=safeStat, width=600, font=("Arial", 70), bg='white')
# safeStatVar.place(x=800, y=30)

notStat = 'Notifications:'
notStatVar = tk.Message(gui, text=notStat, width=800, font=("Arial", 90), bg='white')
notStatVar.place(x=1000, y=600)

# Initial values
tempMsg = '- -'
tempVar = tk.Message(gui, text=tempMsg, width=700, bg='white',
            font=("Arial", 200))
tempVar.place(x=30, y=200)


# Display safe message
# safeMsg = '...pending'
# safeMsgVar = tk.Message(gui, text=safeMsg, width=230, bg='white', 
#             font=("Arial", 25))
# safeMsgVar.place(x=235, y=70)

# Detection Statuses
childDetVar = tk.Message(gui, width=400, bg='white', font=("Arial", 70))
childDetVar.place(x=1000, y=200)

petDetVar = tk.Message(gui, width=400, bg='white', 
            font=("Arial", 70))
petDetVar.place(x=1000, y=350)

notMsg = 'None'
notMsgVar = tk.Message(gui, width=700, fg='green', bg='white', text=notMsg, 
            font=("Arial", 70))
notMsgVar.place(x=1000, y=800)

# Initialize alarm button but do not place it anywhere
# alarmButton = tk.Button(gui, text='Click to deactivate',
# fg='white', bg='red', font=("Arial", 100))
# alarmButton.configure(command=lambda: alarmButton.pack_forget())


def updateTemp(tempVal):
    if tempVal > MAXTEMP:
        tempVal = str(tempVal) + "°C"
        tempVar.configure(text=tempVal, fg='red') 
    else:
        tempVal = str(tempVal) + "°C"
        tempVar.configure(text=tempVal, fg='green')

def updateChild(child, tempVal):
    if (child == 1) & (tempVal < MAXTEMP):
        childDetVar.configure(text='CHILD', fg='green')
    elif (child == 1) & (tempVal > MAXTEMP):
        childDetVar.configure(text='CHILD', fg='red')
    else:
        childDetVar.configure(text='')

def updatePet(pet, tempVal):
    if (pet == 1) & (tempVal < MAXTEMP):
        petDetVar.configure(text='PET', fg='green')
    elif (pet == 1) & (tempVal > MAXTEMP):
        petDetVar.configure(text='PET', fg='red')
    else:
        petDetVar.configure(text='')

def updateStat(tempVal, child, pet, police):
    if (child==1 | pet==1) & (tempVal > MAXTEMP) & (police == 0):
        #safeMsgVar.configure(text='DANGER', fg='red', bg='white')
        notMsgVar.configure(text='Text alert sent.', fg='red')
    elif (child==1 | pet==1) & (tempVal > MAXTEMP) & (police == 1):
        #safeMsgVar.configure(text='DANGER', fg='red', bg='white')
        notMsgVar.configure(text='Police have been notified.', fg='red')
    else:
        #safeMsgVar.configure(text='All good!', fg='black', bg='lightgreen')
        notMsgVar.configure(text='None', fg='green')

# def alarmBut(tempVal, child, pet):
#     if((tempVal > MAXTEMP) & (child | pet)):
#         alarmButton.pack()