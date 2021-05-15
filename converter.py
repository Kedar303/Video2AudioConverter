import tkinter as tk
from tkinter import *
from tkinter import filedialog
#from functools import lru_cache

#@lru_cache()
#filedialog.askopenfilename(title='k')

def call():
    import  moviepy.editor as mp
    i = mp.VideoFileClip(e.get())
    i.audio.write_audiofile(e1.get())
    #print(i)

root = Tk()
#root.iconphoto(True,tk.PhotoImage(file='10.png'))
root['bg'] = '#49A'
root.title("Converter")
root.geometry("500x200")
l = Label(root, text = "Enter video path" , font = "Trebuchet")
l.place(x=10,y=10)
e = Entry(root,bd=5,font="Trebuchet")
e.place(x=170,y=10)
l1 = Label(root,text="Enter audio path",font="Trebuchet")
l1.place(x=10,y=60)
e1 = Entry(root,bd=5,font="Trebuchet")
e1.place(x=170,y=60)
b = Button(root,text = "Convert",font="Trebuchet",command=call)
b.place(x=140,y=120)
root.mainloop()