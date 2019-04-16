from tkinter import *

m = Tk()
m.title("Running Pace Calculator")
m.configure(padx=20, pady=20, bg="#E5E7E4")
m.geometry("+500+200")


def down():
    t = int(e2.get())
    t -= 1
    e2.delete(0, END)
    e2.insert(0, t)


def up():
    t = int(e2.get())
    t += 1
    e2.delete(0, END)
    e2.insert(0, t)


# def clear_tip_amounts():


def calculate_tip():
    e3.delete(0, END)
    e4.delete(0, END)
    t = (int(e2.get()) / 100)
    meal = int(e1.get())
    tip_amount = meal * t
    tip = f'${tip_amount:.2f}'
    e3.insert(0, tip)
    meal_tip = meal + tip_amount
    e4.insert(0, f'${meal_tip:.2f}')


frame1 = Frame(m, bg="#E5E7E4")

frame1.grid(row=3, column=1)

title = Label(m, text="Tip Calculator", padx=6, pady=6, bg="#E5E7E4", fg="#000000", font=("Calibri", "20", "bold"))
lab1 = Label(m, text="Meal Total", font=("Calibri", "12"), padx=6, pady=6, bg="#E5E7E4")
lab2 = Label(m, text="Tip Percent", font=("Calibri", "12"), padx=6, pady=6, bg="#E5E7E4")
lab3 = Label(m, text="Adjust Tip %", font=("Calibri", "12"), padx=6, pady=6, bg="#E5E7E4")
lab4 = Label(m, text="Tip Amount", font=("Calibri", "12"), padx=6, pady=6, bg="#E5E7E4")
lab5 = Label(m, text="Meal & Tip", font=("Calibri", "12"), padx=6, pady=6, bg="#E5E7E4")

title.grid(row=0, columnspan=2)
lab1.grid(row=1, column=0, sticky=E)
lab2.grid(row=2, column=0, sticky=E)
lab3.grid(row=3, column=0, sticky=E)
lab4.grid(row=5, column=0, sticky=E)
lab5.grid(row=6, column=0, sticky=E)

e1 = Entry(m, font=("none, 8"))  # Meal Total
e2 = Entry(m, font=("none, 8"))  # tip space
e3 = Entry(m, font=("none, 8"))
e4 = Entry(m, font=("none, 8"))

t = 20  # default tip
e2.insert(0, t)

e1.grid(row=1, column=1, sticky=W)
e2.grid(row=2, column=1, sticky=W)
e3.grid(row=5, column=1, sticky=W)
e4.grid(row=6, column=1, sticky=W)

btn1 = Button(frame1, text="<<", command=down)
btn2 = Button(frame1, text=">>", command=up)
btn3 = Button(m, text="Calculate", font=("bold"), command=calculate_tip)

btn1.grid(row=0, column=0, sticky=W)
btn2.grid(row=0, column=1, sticky=W)
btn3.grid(row=4, column=1)

m.mainloop()
