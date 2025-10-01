import tkinter as tk

FONT = ('Arial', 20)
# Window
window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)
window.config(padx=50,pady=50)

#input mile
input = tk.Entry(width=10)
input.grid(column=2, row=0)

# Miles text
miles = tk.Label(text='Miles')
miles.grid(column=3, row=0)
miles.config(padx=10, pady=10)

# Is equal text
equal_text = tk.Label(text='is equal to')
equal_text.grid(column=0, row=1)
equal_text.config(padx=10, pady=10)

# Output
km_output = tk.Label(text='0')
km_output.grid(column=2, row=1)
km_output.config(padx=10, pady=10)


# KM text
km_text = tk.Label(text='KM')
km_text.grid(column=3, row=1)
km_text.config(padx=10, pady=10)


# Button
def calculate_km():
    mile = float(input.get())
    km = mile * 1.609344
    km_output.config(text=km)

button = tk.Button(text='Calculate', command=calculate_km)
button.grid(column=2, row=2)


# # Label
# my_label = tk.Label(text='Label')
# my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)


# # Button
# def click():
#     # my_label['text'] = 'Button Got Clicked'
#     my_input = input.get()
#     my_label.config(text=my_input)

# button = tk.Button(text='net button', command=click)
# button.grid(column=3, row=0)

# button = tk.Button(text='click me', command=click)
# button.grid(column=2, row=2)



window.mainloop()
