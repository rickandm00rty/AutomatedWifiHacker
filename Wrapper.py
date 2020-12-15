## Python wrapper for program

from tkinter import *
import webbrowser
import subprocess

#Place standard wireless card in monitoring mode on launch
EnableMonitor = subprocess.Popen(['airmon-ng start wlan0'], shell=TRUE)

window = Tk()

window.title("Kyle's WiFi PWNER Ver. 1")
window.geometry('640x100')

txt = Entry(window, width=20)
txt.grid(column=0, row=1)

def loadDefaults():
    btn.configure(text="Cracking....")
    

btn = Button(window, text="Crack my PW", activebackground="Red", command=loadDefaults)
btn.grid(column=0, row=2)


window.mainloop()