from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.wm_minsize(width=200, height=100)
window.config(padx=20, pady=20)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

km_output = Label(text="0")
km_output.grid(column=1, row=1)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_output.config(text=f"{km}")


calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
