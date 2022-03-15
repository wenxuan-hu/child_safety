# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
#client = Client("ACf9ecac2323a924462328c12f154a3ace", "3b988524b9630bfc59f38b61e71b6ae7")
client = Client("AC74c199f3aef549b56942f8790a145591", "bf744324cc318b1bfe2c014b143cd038")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+12066706309", 
                       #from_="+17406886657",
                       from_="+17124236097", 
                       body="A child or pet has been detected in your vehicle and the temperature is not safe!")