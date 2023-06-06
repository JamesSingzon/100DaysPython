import tkinter

def button_clicked():
    my_label["text"] = contribution.get()

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

#Button 1
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Button 2
button = tkinter.Button(text="New Button", command=button_clicked)
button.grid(column=2, row=0)

#Entry
contribution = tkinter.Entry(width=10)
print(contribution.get())
contribution.grid(column=3, row=2)

#Tkinter Layout Managers
#Pack, Place, Grid


#Advanced Python Arguments  **kw
#Arguments with Default Values

#*args: Many Positional Arguments
#Passes in unlimited number of arguments in the form of a tuple
#Means you can index through the tuple

# def add(*args):
#     return sum(args)

# print(add(5,8,4,9,7,6))

#**kwargs: Many Keyworded Arguments
#can add an unlimited number of keyword arguments
#passes them in as a dictionary


# class Car:
#     def __init__(self, **kw) -> None:
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.colour = kw.get("colour")
#         self.seats = kw.get("seats")



# car = Car(make="Nissan", model="GT-R")
# print(car.seats)



#Must always be at the bottom of our program
window.mainloop()