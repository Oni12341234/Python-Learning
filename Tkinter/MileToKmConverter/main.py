from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)


distance_miles = 0
distance_kilometer = 0
def button_clicked():
    global distance_kilometer
    distance_miles=float(input.get())
    distance_kilometer = distance_miles * 1.6
    value_label["text"] = f"{round(distance_kilometer, 2)}"

input = Entry(width=10)
input.grid(column=4, row=1)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=4, row=3)

my_label = Label(text= "is equal to ", font =("Arial", 10 , "normal"))
my_label.grid(column=2 , row=2)

miles_label = Label(text = "Miles" , font = ("Arial" , 10, "normal"))
miles_label.grid(row=1, column=5)

kilometer_label = Label(text= "Km", font = ("Arial", 10, "normal"))
kilometer_label.grid(column=5  , row=2)

value_label = Label(text=f"{distance_kilometer}", font = ("Arial", 10, "normal"))
value_label.grid(column=4, row=2)

window.mainloop()