from tkinter import*
import tkinter as tk
from datetime import datetime
import time
import winsound

#Create the function Alarm

# Set up variables



alarm_clock = tk.Tk()
alarm_clock.title("Alarm clock")
alarm_clock.geometry("400x200")
time_format = Label(alarm_clock, text= "Enter time in 24 hour format!",
                    fg="red" , bg= "black" , font="Arial").place(x=60,y=120)

add_time = Label(alarm_clock , text = "Hour Min Sec" ,font= 60).place(x=110)

set_your_alarm = Label (alarm_clock , text = "what time to wake up", fg="blue",relief="solid", font=("Helevetica",7,"bold")).place(x=0,y=29)

hour = StringVar()
#minu  = StringVar()
#sec = StringVar()



def alarm(set_alarm):
    set_alarm_timer = f"{hour.get()}"
    
    #get hours
    set_alarm_timer_hours = set_alarm_timer[0:2]
    
    #get minutes
    set_alarm_timer_mins = set_alarm_timer[3:5]
    
    #get seconds
    set_alarm_timer_sec = set_alarm_timer[6:8]
    

    while True:
        time.sleep(1)
        current_time = datetime.now()
        time_now_hours = current_time.strftime("%I")
        time_now_mins = current_time.strftime("%M")
        time_now_sec = current_time.strftime("%S")
        #date_now = current_time.strftime("%d/%m/%Y")
        #print("The date is:",date_now)
        #print(time_now)
        #if time_now == set_alarm:
        if time_now_hours == set_alarm_timer_hours:
            if time_now_mins == set_alarm_timer_mins:
                if time_now_sec == set_alarm_timer_sec:
                    print("It is time to get  up sleep head")
                    winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
                    break    

def actual_time():
    set_alarm_timer = f"{hour.get()}"
    alarm(set_alarm_timer)    


#Time of the alarm

hour_time = Entry(alarm_clock , textvariable = hour , bg="pink" ,
                  width = 15).place(x=110,y=30)

#min_time = Entry(alarm_clock , textvariable = minu , bg="pink" ,
                  #width = 15).place(x=150,y=30)

#sec_time = Entry(alarm_clock , textvariable = sec , bg="pink" ,
                  #width = 15).place(x=200,y=30)

# User enters the time

submit = Button (alarm_clock, text = "Set alarm" , fg="red",width=10,command=actual_time).place(x=110, y=70)

alarm_clock.mainloop()
