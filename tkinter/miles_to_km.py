from tkinter import *

window = Tk()
window.title("miles to km")
window.minsize(width=200, height=80)

entry = Entry(width=10)
entry.grid(row=0, column=2)

label_miles = Label(text="miles")
label_miles.grid(row=0, column=3)

label_result = Label(text="is equal to")
label_result.grid(row=1, column=1)

label_func = Label(text="0")
label_func.grid(row=1, column=2)

label_km = Label(text="km")
label_km.grid(row=1, column=3)


# button and action of it
def action():
    mile = float(entry.get())
    km = f"{mile * 1.6:.0f}"
    label_func.config(text=km)


button = Button(text="calculate", command=action)
button.grid(row=2, column=2)


window.mainloop()