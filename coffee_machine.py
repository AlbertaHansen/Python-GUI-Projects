import tkinter as tk
from tkinter import ttk, DISABLED

# create root window with geometry
root = tk.Tk()
root.title('Coffee Machine!')
root.geometry('300x200')


# create function for button submission
def latte_click():
    """
    function when gui button is clicked
    fills drink box with chosen output
    """
    drink_box.set("Latte")


def espresso_click():
    """
    function when gui button is clicked
    fills drink box with chosen output
    """
    drink_box.set("Espresso")


def cappuccino_click():
    """
    function when gui button is clicked
    fills drink box with chosen output
    """
    drink_box.set("Cappuccino")


def add_200():
    """
    function when gui button is clicked
    fills money box with added amount
    """
    money = float(money_box.get()[1:])
    money_box.set(f"${money + 2.00:.2f}")


def add_100():
    """
    function when gui button is clicked
    fills money box with added amount
    """
    money = float(money_box.get()[1:])
    money_box.set(f"${money + 1.00:.2f}")


def add_25():
    """
    function when gui button is clicked
    fills money box with added amount
    """
    money = float(money_box.get()[1:])
    money_box.set(f"${money + 0.25:.2f}")


def make_drink():
    """
    function when gui button is clicked
    checks the money and drink box input to see if the customer has enough money for chosen drink
    if not print appropriate message in result box
    if yes subtract necessary money and print appropriate message in result box
    """
    money = float(money_box.get()[1:])
    if drink_box.get() == "Latte" and money >= 2.50:
        money_box.set(f"${money - 2.50:.2f}")
        result_box.set("Enjoy your Latte!")
        drink_box.set("")
    elif drink_box.get() == "Espresso" and money >= 1.50:
        money_box.set(f"${money - 1.50:.2f}")
        result_box.set("Enjoy your Espresso!")
        drink_box.set("")
    elif drink_box.get() == "Cappuccino" and money >= 3.00:
        money_box.set(f"${money - 3.00:.2f}")
        result_box.set("Enjoy your Cappuccino!")
        drink_box.set("")
    else:
        result_box.set("Insufficient Money")


# create the main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)

# Create label
ttk.Label(frame_home, text="Coffee Maker ").grid(column=0, row=0)

# Drink buttons
ttk.Button(frame_home, text='Latte ($2.50)', command=latte_click).grid(column=0, row=1)
ttk.Button(frame_home, text='Espresso ($1.50)', command=espresso_click).grid(column=1, row=1)
ttk.Button(frame_home, text='Cappuccino ($3.00)', command=cappuccino_click).grid(column=2, row=1)

# Money buttons
ttk.Button(frame_home, text='$2.00', command=add_200).grid(column=0, row=2)
ttk.Button(frame_home, text='$1.00', command=add_100).grid(column=1, row=2)
ttk.Button(frame_home, text='$0.25', command=add_25).grid(column=2, row=2)

# Money and drink boxes
money_box = tk.StringVar()
ttk.Entry(frame_home, width=30, state=DISABLED, textvariable=money_box).grid(column=0, row=3, columnspan=3)
money_box.set("$0.00")
drink_box = tk.StringVar()
ttk.Entry(frame_home, width=30, state=DISABLED, textvariable=drink_box).grid(column=0, row=4, columnspan=3)

# Make drink button
ttk.Button(frame_home, text='Make Drink', command=make_drink).grid(column=1, row=5)

# Result box
result_box = tk.StringVar()
ttk.Entry(frame_home, width=30, state=DISABLED, textvariable=result_box).grid(column=0, row=6, columnspan=3)

root.mainloop()
