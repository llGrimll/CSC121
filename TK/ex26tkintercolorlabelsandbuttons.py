from tkinter import *


def changepurple():
    lab1.config(bg='purple', text='Purple Label')
    showmessage()


def changebrown():
    lab2.config(bg='brown', text='Brown Label')
    showmessage()


def changeyellow():
    lab3.config(bg='yellow', text='Yellow Label')
    showmessage()


def showmessage():
    v.set("Label Changed!")


def resetall():
    lab1.config(bg='red', text='Red Label')
    lab2.config(bg='green', text='Green Label')
    lab3.config(bg='blue', text='Blue Label')
    resetmessage()


def resetmessage():
    v.set("Reset All Labels")


m = Tk()

m.title('Tkinter Color Labels')

fr1 = Frame(m)
fr1.pack(side=TOP)

lab1 = Label(fr1, text='Red Label', fg='white', bg='red', width=9, height=6,
             font=('Cambria, 24'))
lab2 = Label(fr1, text='Green Label', fg='white', bg='green', width=9,
             height=6, font=('Cambria, 24'))
lab3 = Label(fr1, text='Blue Label', fg='white', bg='blue', width=9, height=6,
             font=('Cambria, 24'))

fr2 = Frame(m)
fr2.pack(side=BOTTOM)

btn1 = Button(fr2, text='Change Purple', padx=6, font=('none', 16),
              command=changepurple)
btn2 = Button(fr2, text='Change Red', padx=6, font=('none', 16),
              command=changebrown)
btn3 = Button(fr2, text='Change Yellow', padx=6, font=('none', 16),
              command=changeyellow)
btn4 = Button(fr2, text='Reset', padx=6, font=('none', 16),
              command=resetall)

v = StringVar()

lab4 = Label(fr2, textvariable=v, fg='red', font=('Cambria', 20))

lab1.pack(side=LEFT, fill=Y)
lab2.pack(side=LEFT, fill=Y)
lab3.pack(side=LEFT, fill=Y)
lab4.pack(side=BOTTOM, fill=Y)

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack(side=LEFT)

m.mainloop()
