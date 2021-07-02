from tkinter import *

window = Tk()
window.title("Miles to Kms Converter")
window.minsize(width=300, height=100)

#Label
# my_label = Label(text='I am a Label', font=("Arial", 24, "bold"))

# Entry

miles = Entry(width=10)

miles.grid(column=1, row=0, pady=10)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

eq_label = Label(text='is equal to')
eq_label.grid(column=0, row=1, padx=(50,0), pady=10)

kms_label = Label(text='___Kms')
kms_label.grid(column=1, row=1, pady=10)

#Button

def button_clicked():
    print("I got clicked")
    kms_label["text"] = f'{int(miles.get()) * 1.609: .3f} Kms'    

button = Button(text='Calculate', command=button_clicked)

button.grid(column=1, row=2, padx=5, pady=10)


window.mainloop()