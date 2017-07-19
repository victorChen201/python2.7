#!/usr/bin/env python
# coding=utf-8


from Tkinter import *

root = Tk()
frame = Frame()
frame.pack()

bottomframe = Frame()
bottomframe1 = Frame()
bottomframe1.pack( side = BOTTOM  )
bottomframe.pack( side = BOTTOM  )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT )

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT  )

bluebutton = Button(bottomframe1, text="Blue", fg="blue")
bluebutton.pack( side = LEFT  )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM )

root.mainloop()
