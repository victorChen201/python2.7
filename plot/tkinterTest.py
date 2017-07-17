#!/usr/bin/env python
#-*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import askopenfilename
import sys 
sys.path.append('..')
class App(object):
    def __init__(self,master):
        self.com = Button(master, text='画图', command=self.say_hello)
        self.com.grid(column=10, row =100)
        #self.com.pack(side=BOTTOM)
         
        self.label = Label(master, text="")
        self.label.grid(row=1, column=0, padx=15, pady=15, sticky="wesn")
        #self.label.pack()
    
        mainmenu = Menu(master)
        mainmenu.add_command(label='打开文件', command=self.OpenFile)
        master['menu'] = mainmenu

        self.v = IntVar()
        text = ['Line', 'Bar', 'Stack']       
        for i in range(len(text)):
           rb = Radiobutton(root, variable=self.v, text = text[i], value=i+1 , command=self.Drawing_type)
           rb.grid(row=3, column=100+i, sticky=E)
           
        
        lb = Listbox(root, selectmode=BROWSE)
        for item in ['python','tkinter','widget']:
            lb.insert(END, item)
        lb.grid(row=200, column=200)

       
       # bootframe = Frame(root)
        
    def Drawing_type(self):
        print self.v.get()
        
    def OpenFile(self):
        file_path = askopenfilename(filetypes=(("py files", "*.csv"),("All files", "*.*")))
        if not file_path:
            return
        self.label["text"] = file_path

    def say_hello(self):
        print 'hello,gui'

    def printCoords(self,event):
        print 'event.char = ',event.char
        print 'event.keycode = ',event.keycode
if __name__=='__main__':
    root = Tk()
    root.title('window with command')
    root.geometry('800x600')
    App(root)
    root.mainloop()
