#!/usr/bin/env python
#-*- coding: utf-8 -*-
from Tkinter import *
class App(object):
    def __init__(self,master):
        self.com = Button(master, text='dazhaohu', command=self.say_hello)
        self.com.pack(side=BOTTOM)
        text = Entry(master, background = 'red', foreground='#0000ff', show='*', highlightbackground = 'red', highlightthickness = 1)
        text.pack()
        
        default_value = StringVar()
        default_value.set('This is a default value')
        text = Entry(master, textvariable = default_value, width=50)
        text['show']='*'
        
        text.pack()
        for mask in ['*','#','$']:
                e = StringVar()
                entry = Entry(root,textvariable = e)
                e.set('input password')
                entry.pack()
                entry['show'] = mask
        v = IntVar()
        def callCheckbutton():
                print v.get()
        Checkbutton(root, variable = v, text = 'checkbutton value', command = callCheckbutton).pack()
        
        for i in range(3):
            Radiobutton(root,variable = v,text = 'python',value = i).pack()
        vLang = IntVar()
        vOS = IntVar()
        vLang.set(1)
        vOS.set(2)

        for v in [vLang,vOS]:    #创建两个组
            for i in range(3):    #每个组含有3个按钮
                Radiobutton(root, variable = vOS, indicatoron=0, value = i, text = 'python' + str(i)).pack()
        self.bt1 = Button(master, text='right key')
        self.bt1.bind('F5')
        lb = Listbox(root,selectmode=BROWSE)
        for item in ['python','tkinter','widget']:
            lb.insert(END, item)
        lb.pack()
    def say_hello(self):
        print 'hello,gui'

    def printCoords(self,event):
        print 'event.char = ',event.char
        print 'event.keycode = ',event.keycode
if __name__=='__main__':
    root = Tk()
    root.title('window with command')
    root.geometry('400x200')
    App(root)
    root.mainloop()
