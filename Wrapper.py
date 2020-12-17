## Python wrapper for program

from tkinter import *
import webbrowser
import subprocess

#Place standard wireless card in monitoring mode on launch
subprocess.run(['airmon-ng start wlan0'], shell=TRUE, capture_output=TRUE)

#Scan AP's and write to APList object
subprocess.run(['sudo iwlist scan > ./aplist.txt'],shell=TRUE)
#Manually creating AP for testing
subprocess.run(['echo "eduroam" > aplist.txt'], shell=TRUE)

#Generate parent window
window = Tk()
window.title("Kyle's WiFi PWNER Ver. 1")
window.geometry('1000x500')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

#NEEDS SUBPROCESS TO GENERATE LIST
#Generate List window, Pull data, Place window
APList = Listbox(window, fg="Red", selectbackground='Green', selectmode=BROWSE)
f = open('aplist.txt', "r")
for x in f:
    APList.insert(END,x)

APList.grid(row=0, column=2)
APList.place(relx=0.5, rely=0.5, anchor=CENTER)

#On-Click, run the airodump-ng, write to a file
def loadDefaults():
    btn.configure(text="Cracking....")
    subprocess.run('')

#Generate button, click to 'loadDefaults()'
btn = Button(window, text="Crack my PW", activebackground="Red", command=loadDefaults)
btn.grid(row=9, column=0)
btn.place(relx=0.5, rely=1, anchor=S)

window.mainloop()
