import tkinter as tk


def showname():
    name_disp = e1.get() + " " + e2.get()
    e3.delete(0, END)
    e3.insert(0, name_disp)


def clear_fields():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


# def add_attendee():
#     attendees = []
#     cvs_attendee_file = open("attendees.csv, "w")

# Six label buttons to include the directions for user
class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master

        tk.Label(self, text="First", padx=6, pady=6, bg="#CCCCEE").grid(row=0, sticky=W)
        tk.Label(self, text="Last", padx=6, pady=6, bg="#CCCCEE").grid(row=1, sticky=W)
        tk.Label(self, bg="#CCCCEE").grid(row=2, column=1).grid(row=4, column=1)
        tk.Label(self, bg="#CCCCEE").grid(row=6, column=1)
        tk.Label(self, bg="#CCCCEE")

        # Entries
        e1 = tk.Entry(self)
        e1.grid(row=0, column=1)
        e2 = tk.Entry(self)
        e2.grid(row=1, column=1)
        e3 = tk.Entry(self)
        e3.grid(row=5, columnspan=2, sticky=E + W)

        insert_button = tk.Button(m, text="Insert", padx=6, pady=6, command=showname)
        insert_button.grid(row=3, column=1, sticky=E)
        add_another = tk.Button(m, text="Add another", padx=6, pady=6, command=clear_fields)
        add_another.grid(row=3, column=0, sticky=W)
        add_attendee = tk.Button(m, text="Add Attendee", padx=6, pady=6)
        add_attendee.grid(row=7, column=1, sticky=E)

# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# lab1.grid(row=0, sticky=W)
# lab2.grid(row=1, sticky=W)
# lab3.grid(row=2, column=1)
# btn1.grid(row=3, column=1, sticky=E)
# btn2.grid(row=3, column=0, sticky=W)
# lab4.grid(row=4, column=1)
# e3.grid(row=5, columnspan=2, sticky=E + W)
# lab5.grid(row=6, column=1)
# btn3.grid(row=7, column=1, sticky=E)


# GUI settings
root = tk.Tk()
app = App(root)
root.title("tkinter Attendee List")
root.configure(padx=20, pady=20, bg="#CCCCEE")
root.geometry("+500+200")

# Initialize GUI
root.mainloop()
