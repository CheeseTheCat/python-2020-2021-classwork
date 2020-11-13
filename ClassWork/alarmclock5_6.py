#James Hooper
#Alarm Clock

import random
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound
import calendar
import time
import datetime

def gmtnow(alarm):
    """geting Greenwich Mean Time this is based on
Unix time (also known as Epoch time this is the number of
seconds that have elapsed since the Unix epoch,
minus leap seconds;
the Unix epoch is 00:00:00 UTC on 1 January 1970"""
    # this gives us the total seconds that have passed since the Unix epoch
    seconds = calendar.timegm(time.gmtime())
    # we need to brake this down to the current secconds
    # so there are 60 seccond in a min so if we devide by 60
    # the remainder is the curent seccond
    current_sec = seconds%60
    # now we need to figure out the minutes that have passed since the Unix epoch
    minutes = seconds//60
    current_min = minutes%60
    hours = minutes//60
    current_hour = hours%24

    # set time zone mt time
    #current_hour = current_hour - 6
    current_hour -= 6

    # now lets figue out the Am pm tag and set this to a 12 hour clock not 24 hour
    if current_hour >= 12:
        tag = "PM"
        current_hour -= 12
        if current_hour == 0:
            current_hour = 12
            
        
    else:
        if current_hour == 0:
            tag = "AM"
            current_hour = 12
            
    if current_hour < 10:
        ajusted_hour = "0"+str(current_hour)
    else:
        ajusted_hour = str(current_hour)
    if current_min < 10:
        ajusted_minute = "0"+str(current_min)
    else:
        ajusted_minute = str(current_min)
    if current_sec < 10:
        ajusted_second = "0"+str(current_sec)
    else:
        ajusted_second = str(current_sec)

    
    time_string = str.format("{:2}:{:2}:{:2},{}",ajusted_hour,ajusted_minute,ajusted_second,tag)
    
    if alarm == time_string:
        alarm_snd()

    return time_string
    
def show_time():
    time = gmtnow(alarm)
    #show the time
    txt.set(time)
    #trigger the tick after 1000ms
    root.after(1000,show_time)
def alarm_snd():
    for i in range(5):
        winsound.Beep(750,1000)
        winsound.Beep(1000,500)
        winsound.Beep(750,1000)
    
def time_input():
    """get the alarm time that you want to set"""
    ahour = input("what hour?")
    aminute = input("What minute")
    asecond = "00"
    atag = input("AM or PM").upper()
    if len(ahour) < 2:
        ahour = "0"+ahour
    if len(aminute) < 2:
        aminute = "0"+aminute

    alarm = str.format("{:2}:{:2}:{:2},{}",ahour,aminute,asecond,atag)
    return alarm

    
    


#setup the gui window
alarm = time_input()
root = Tk()
root.geometry("800x200")
root.configure(background = "black")
root.bind("x",quit)
root.after(1000, show_time)
fnt = font.Font(family ="Century Gothic",size = 60,weight = "normal")
txt = StringVar()
lbl = ttk.Label(root,textvariable = txt,foreground="white",background="black",font=fnt)
lbl.place(relx = 0.5,rely = 0.5,anchor = CENTER)







#running the gui
root.mainloop()
