import tkinter

def button_clicked():
    # converted["text"] = pre_con.get()
    converted["text"] = str(round(float(pre_con.get())*1.609))

window = tkinter.Tk()
window.title("Mi to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)




#Entry box
pre_con = tkinter.Entry(width=10)
pre_con.grid(column=1, row=0)

#Miles label
miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)

#Is equal to label
equal = tkinter.Label(text="is equal to")
equal.grid(column=0, row=1)

#Converted label
converted = tkinter.Label(text="0")
converted.grid(column=1, row=1)

#Kilometer label
kilometers = tkinter.Label(text="Km")
kilometers.grid(column=2, row=1)

#Calculate button
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()