from tkinter import *
import csv

m = Tk()
m.title("tkinter Attendee List")
m.configure(padx=20, pady=20, bg="#CCCCEE")
m.geometry("+500+200")


def showname():
    name_disp = e1.get() + " " + e2.get()
    e3.delete(0, END)
    e3.insert(0, name_disp)


def clear_fields():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


def add_attendee():
    attendees = []
    first = e1.get()
    last = e2.get()
    attendees.append(first)
    attendees.append(last)
    with open('attendees.csv', 'a', newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(attendees)
    clear_fields()


lab1 = Label(m, text="First", padx=6, pady=6, bg="#CCCCEE")
lab2 = Label(m, text="Last", padx=6, pady=6, bg="#CCCCEE")
lab3 = Label(m, bg="#CCCCEE")
lab4 = Label(m, bg="#CCCCEE")
lab5 = Label(m, bg="#CCCCEE")

e1 = Entry(m)
e2 = Entry(m)
e3 = Entry(m)

btn1 = Button(m, text="Insert", padx=6, pady=6, command=showname)
# btn2 = Button(m, text="Add another", padx=6, pady=6, command=clear_fields)
btn3 = Button(m, text="Add Attendee", padx=6, pady=6, command=add_attendee)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
lab1.grid(row=0, sticky=W)
lab2.grid(row=1, sticky=W)
lab3.grid(row=2, column=1)
btn1.grid(row=3, column=1, sticky=E)
# btn2.grid(row=3, column=0, sticky=W)
lab4.grid(row=4, column=1)
e3.grid(row=5, columnspan=2, sticky=E + W)
lab5.grid(row=6, column=1)
btn3.grid(row=7, column=1, sticky=E)

m.mainloop()
