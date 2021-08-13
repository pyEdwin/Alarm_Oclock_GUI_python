#Import libraries
from tkinter import*
import tkinter as tk
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
        print("The date is:",date_now)
        if time_now == set_alarm:
            print("It is time to get  up sleep head")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break    


# def actual_time():
#     set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
#     alarm(set_alarm_timer)    

clock = tk.Tk()
clock.title("Alarm clock")
clock.geometry("400x200")
time_format = Label(alarm_clock, text= "Enter time in 24 hour format!",
                    fg="red" , bg= "black" , font="Arial").place(x=60,y=120)

add_time = Label(alarm_clock , text = "Hour Min Sec" ,font= 60).place(x=110)

set_your_alarm = Label (alarm_clock , text = "what time to wake up", fg="blue",relief="solid", font=("Helevetica",7,"bold")).place(x=0,y=29)
submit = Button (alarm_clock, text = "Set alarm" , fg="red",width=10,command=actual_time).place(x=110, y=70)
clock.mainloop()
