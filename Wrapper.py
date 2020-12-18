# MAIN
from tkinter import *
import webbrowser
import subprocess
import sys, os

#PLACE CARD IN MONITOR MODE
#subprocess.run(['airmon-ng start wlan0'], shell=TRUE, capture_output=TRUE)

#GENERATE PARENT WINDOW
window = Tk()
window.title("Kyle's WiFi PWNER Ver. 1")
window.geometry('500x250')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

#GENERATE CHILD LIST & DISPLAY
APList = Listbox(window, fg="Red", selectbackground='Green', selectmode=BROWSE)
f = open(os.path.join(sys.path[0], "aplist.txt"), "r")
for x in f:
    APList.insert(END,x)

APList.grid(row=0, column=2)
APList.place(relx=0.5, rely=0.5, anchor=CENTER)

#On-Click, RUN AIRODUMP TO GATHER HANDSHAKE
def handshakeCap():
    btn.configure(text="Cracking....")

#BUTTON GENERATION, LINKS TO handshakeCap()
btn = Button(window, text="Crack my PW", activebackground="Red", command=handshakeCap)
btn.grid(row=9, column=0)
btn.place(relx=0.5, rely=1, anchor=S)

window.mainloop()
