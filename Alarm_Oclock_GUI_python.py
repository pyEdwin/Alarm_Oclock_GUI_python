#Import libraries
from tkinter import*
import datetime
import time
import winsound

#Create the function Alarm

def alarm(set_alarm):

    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        time_now = current_time.strftime("%H:%M:%S")
        date_now = current_time.strftime("%d/%m/%Y")
        print(time_now)
        if time_now == set_alarm:
            print("It is time to get  up sleep head")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break    