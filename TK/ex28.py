from tkinter import *
import csv
import datetime

m = Tk()
m.title("tkinter Attendee List")
m.configure(padx=20, pady=20, bg="#4D6B53")
m.geometry("+500+200")


def today_button():
    x = datetime.datetime.now()
    e4.insert(0, x.strftime("%m"))
    e5.insert(0, x.strftime("%d"))
    e6.insert(0, x.strftime("%Y"))


def clear_fields():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)


def pace_calc():
    minutes = int(e1.get())
    sec = int(e2.get())
    miles = int(e3.get())
    total_time = (minutes) + (sec / 60)
    min_per_mile = total_time / miles
    seconds = min_per_mile - int(min_per_mile)
    final_seconds = seconds * 60
    pace = f'{int(min_per_mile)}:{round(final_seconds)}'
    e7.insert(0, pace)


def record_run():
    time = []
    minutes = int(e1.get())
    sec = int(e2.get())
    miles = int(e3.get())
    total_time = (minutes) + (sec / 60)
    min_per_mile = total_time / miles
    seconds = min_per_mile - int(min_per_mile)
    final_seconds = seconds * 60
    miles = e3.get()
    date = f'{e4.get()}/{e5.get()}/{e6.get()}'
    time.append(int(min_per_mile))
    time.append(final_seconds)
    time.append(miles)
    time.append(date)
    with open('runningrecords.csv', 'a', newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(time)
    clear_fields()


title = Label(m, text="Running Pace Calculator", padx=6, pady=6, bg="#4D6B53")
lab1 = Label(m, text="Minutes:", padx=6, pady=6, bg="#4D6B53")
lab2 = Label(m, text="Seconds:", padx=6, pady=6, bg="#4D6B53")
lab3 = Label(m, text="Miles:", padx=6, pady=6, bg="#4D6B53")
lab4 = Label(m, text="Date:", padx=6, pady=6, bg="#4D6B53")
lab5 = Label(m, text="Or Enter Past Date:", padx=6, pady=6, bg="#4D6B53")
lab6 = Label(m, text="Month:", padx=6, pady=6, bg="#4D6B53")
lab7 = Label(m, text="Day:", padx=6, pady=6, bg="#4D6B53")
lab8 = Label(m, text="Year:", padx=6, pady=6, bg="#4D6B53")
lab9 = Label(m, text="ex: 4 8 2019", padx=6, pady=6, bg="#4D6B53")
lab10 = Label(m, text="Pace/Mile", padx=6, pady=6, bg="#4D6B53")

e1 = Entry(m, font=("none, 8"))
e2 = Entry(m, font=("none, 8"))
e3 = Entry(m, font=("none, 8"))
e4 = Entry(m, font=("none, 8"))
e5 = Entry(m, font=("none, 8"))
e6 = Entry(m, font=("none, 8"))
e7 = Entry(m, font=("none, 8"))

btn1 = Button(m, text="Use Today", command=today_button)
btn2 = Button(m, text="Show Pace", command=pace_calc)
btn3 = Button(m, text="SAVE", command=record_run)

title.grid(row=0, columnspan=2)
lab1.grid(row=1, column=0, sticky=E)
e1.grid(row=1, column=1)
lab2.grid(row=2, column=0, sticky=E)
e2.grid(row=2, column=1)
lab3.grid(row=3, column=0, sticky=E)
e3.grid(row=3, column=1)
lab4.grid(row=4, column=0, sticky=E)
btn1.grid(row=4, column=1, sticky=W)
lab5.grid(row=5, column=1, sticky=W)
lab6.grid(row=7, column=1, sticky=W)
lab7.grid(row=7, column=2, sticky=W)
lab8.grid(row=7, column=3, sticky=W)
lab9.grid(row=8, column=0, sticky=E)
e4.grid(row=8, column=1, sticky=W)
e5.grid(row=8, column=2)
e6.grid(row=8, column=3, sticky=E)
btn2.grid(row=9, column=1, sticky=W)
lab10.grid(row=10, column=0, sticky=E)
e7.grid(row=10, column=1)
btn3.grid(row=11, column=1)

m.mainloop()
