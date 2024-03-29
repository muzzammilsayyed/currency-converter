from currency_converter import CurrencyConverter
import tkinter as tk
from datetime import date

c = CurrencyConverter()
d = c.convert(100, 'EUR', 'USD', date=date(2014, 3, 28))


window = tk.Tk()
window.geometry("500x360")
window.title("Currency Converter")

def clicked():
    amount = int(entry1.get())
    cur1 = entry2.get()
    cur2 = entry3.get()
    data = c.convert(amount, cur1, cur2)
    label4 = tk.Label(window, text=data, font="Times 16 bold").place(x = 200, y = 300)

label = tk.Label(window, text="Currency converter", font = "Times 20 bold").place(x = 100, y = 40)
label1 = tk.Label(window, text= "Enter Amount here: ", font = "Times 16 bold").place(x = 60, y = 100)
entry1 = tk.Entry(window)

label2 = tk.Label(window, text= "Enter your Currency here: ", font = "Times 16 bold").place(x = 30, y = 150)
entry2 = tk.Entry(window)

label3 = tk.Label(window, text= "Enter your desired currency: ", font = "Times 16 bold").place(x = 15, y = 200)
entry3 = tk.Entry(window)

button = tk.Button(window, text= "click", font = "Times 16 bold", command=clicked).place(x = 220, y = 250)
entry1.place(x = 270 , y = 107)
entry2.place(x = 270 , y = 157)
entry3.place(x = 270 , y = 207)
window.mainloop()