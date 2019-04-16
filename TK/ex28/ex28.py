from tkinter import *
import csv
import datetime

m = Tk()
m.title("Running Pace Calculator")
m.configure(padx=20, pady=20, bg="#E5E7E4")
m.geometry("+500+200")
file_path = r"C:\Users\jkom8\Dropbox (Personal)\Personal\github\CSC121\TK\ex28\runningrecords.csv"
# My computer was having permission issues with inputting the file
# name so I included the entire file path. This format worked.


def today_button():
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
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
    time = []
    if e1.get() == "":
        lab12.config(text="Please input your minutes.")
        m.after(3000, clear_notice)
        return
    elif e2.get() == "":
        lab12.config(text="Please input your seconds.")
        m.after(3000, clear_notice)
        return
    elif e3.get() == "":
        lab12.config(text="Please input your miles.")
        m.after(3000, clear_notice)
        return
    minutes = int(e1.get())
    sec = int(e2.get())
    miles = int(e3.get())
    total_time = (minutes) + (sec / 60)
    min_per_mile = total_time / miles
    seconds = min_per_mile - int(min_per_mile)
    final_seconds = seconds * 60
    time.append(int(min_per_mile))
    time.append(round(final_seconds))
    time.append(miles)
    return time
    # index 0 is min per miles
    # index 1 is Seconds
    # index 2 is miles


def insert_pace():
    time = pace_calc()
    if time is None:
        return
    pace = f'{time[0]}:{round(time[1])}'
    e7.insert(0, pace)


def clear_notice():
    lab12.config(text="")


def success_notice():
    lab12.config(text="Saved successfully!")
    m.after(3000, clear_notice)


def record_run():
    if e4.get() == "" or e5.get() == "" or e6.get() == "":
        lab12.config(text="Please input a full date.")
        m.after(3000, clear_notice)
        return
    time = pace_calc()
    date = f'{e4.get()}/{e5.get()}/{e6.get()}'
    time.append(date)
    with open(file_path, "a", newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(time)
    clear_fields()
    success_notice()

# Gui Layout


frame1 = Frame(m, bg="#E5E7E4")

frame1.grid(row=7, column=1, rowspan=2)

title = Label(m, text="Running Pace Calculator", padx=6, pady=6, bg="#E5E7E4", fg="#000000", font=("Calibri", "20", "bold"))
lab1 = Label(m, text="Minutes:", font=("Calibri", "12"), padx=6, pady=6, bg="#E5E7E4")
lab2 = Label(m, text="Seconds:", font=("Calibri", "12"), padx=6, pady=6, bg="#E5E7E4")
lab3 = Label(m, text="Miles:", font=("Calibri", "12"), padx=6, pady=6, bg="#E5E7E4")
lab4 = Label(m, text="Date:", font=("Calibri", "12"), padx=6, pady=6, bg="#E5E7E4")
lab5 = Label(m, text="Or Enter Past Date:", font=("Calibri", "12"), padx=6, pady=6, bg="#E5E7E4")
lab6 = Label(frame1, text="Month:", font=("Calibri", "12"), padx=6, pady=6, bg="#E5E7E4")
lab7 = Label(frame1, text="Day:", font=("Calibri", "12"), padx=6, pady=6, bg="#E5E7E4")
lab8 = Label(frame1, text="Year:", font=("Calibri", "12"), padx=6, pady=6, bg="#E5E7E4")
lab9 = Label(m, text="ex: 4 8 2019", font=("Calibri", "12", "italic"), padx=6, pady=6, bg="#E5E7E4")
lab10 = Label(m, bg="#E5E7E4")  # help with spacing of frame and show pace button
lab11 = Label(m, text="Pace/Mile", font=("Calibri", "12"), padx=6, pady=6, bg="#E5E7E4")
lab12 = Label(m, font=("Calibri", "12"), padx=6, pady=6, bg="#E5E7E4")

title.grid(row=0, columnspan=2)
lab1.grid(row=1, column=0, sticky=E)
lab2.grid(row=2, column=0, sticky=E)
lab3.grid(row=3, column=0, sticky=E)
lab4.grid(row=4, column=0, sticky=E)
lab5.grid(row=5, column=1, sticky=W)
lab6.grid(row=0, column=0, sticky=W)
lab7.grid(row=0, column=1, sticky=W)
lab8.grid(row=0, column=2, sticky=W)
lab9.grid(row=8, column=0, sticky=E)
lab10.grid(row=9)
lab11.grid(row=11, column=0, sticky=E)
lab12.grid(row=13, columnspan=2)

e1 = Entry(m, font=("none, 8"))
e2 = Entry(m, font=("none, 8"))
e3 = Entry(m, font=("none, 8"))
e4 = Entry(frame1, width=4)
e5 = Entry(frame1, width=4)
e6 = Entry(frame1, width=6)
e7 = Entry(m, font=("none, 8"), state="readonly")

e1.grid(row=1, column=1, sticky=W)
e2.grid(row=2, column=1, sticky=W)
e3.grid(row=3, column=1, sticky=W)
e4.grid(row=1, column=0)
e5.grid(row=1, column=1)
e6.grid(row=1, column=2, sticky=E)
e7.grid(row=11, column=1, sticky=W)

btn1 = Button(m, text="Use Today", command=today_button)
btn2 = Button(m, text="Show Pace", command=insert_pace)
btn3 = Button(m, text="SAVE", command=record_run)

btn1.grid(row=4, column=1, sticky=W)
btn2.grid(row=10, column=1, sticky=W)
btn3.grid(row=12, column=1, sticky=W)

m.mainloop()
