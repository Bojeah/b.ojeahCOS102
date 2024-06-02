# Importing necessary modules from tkinter
from tkinter import *

def home():
    global home_win
    home_win = Tk()
    home_win.title("PAU Cafeteria ")
    home_win.minsize(height=100, width=300)
    home_win.geometry("+650+0")
    home_win.config(bg="navy blue")
    Label(home_win, text="PAU CAFETERIA", font=("times New Roman", 30, "bold"), fg="white", bg="navy blue").pack()

    Label(home_win, text="WELCOME TO PAU CAFETERIA, ENJOY YOURSELF!!", font=("Times New Roman", 12), fg="white", bg="navy blue").pack()

    Button(home_win, text="PROCEED TO MENU", command=menu_window, width= 15, height= 3).pack()

    home_win.mainloop()

# Function to calculate discounted price
def calculate_discounted_price(total, discount):
    return total - (total * (discount / 100))

# Function to calculate the order total and display it
def calculate_order_total():
    # Destroy the order window after calculation
    order_window.destroy()

    # Create a new window for displaying the total
    total_window = Tk()
    total_window.title("PAU Cafeteria Total")
    total_window.minsize(height=100, width=300)
    total_window.geometry("+650+0")
    total_window.config(bg="navy blue")
    Label(total_window, text="RECEIPT\n", font=("Times New Roman", 23, "bold"), fg="white", bg="navy blue").pack()


    # Labels for displaying total and discount information
    total_label = Label(total_window, text="\n", font=("Arial", 18), fg="black", bg="navy blue")
    total_label.pack()
    discount_label = Label(total_window, text="", font=("Arial", 18), fg="black", bg="navy blue")
    discount_label.pack()
    
    # List of items and quantities selected by the user
    items = [rice_var, sides_var, soups_var, proteins_var, beverages_var]
    quantities = [quantity1_var, quantity2_var, quantity3_var, quantity4_var, quantity5_var]

    total_price = 0
    # Calculate the total price based on selected items and quantities
    for i in range(5):
        if items[i].get() == "--select--" or quantities[i].get() == "--select--":
             total_price += 0
        else:
            total_price += items_list[items[i].get()] * int(quantities[i].get())

    # Determine discount based on total price
    if total_price < 2500:
        total = total_price
        total_label.config(text=f"Total: ₦{total}", fg="white")
        discount = 10
        final_price = calculate_discounted_price(total, discount)
        discount_label.config(text=f"Discount: {discount}%\nFinal Price: ₦{final_price}", fg="white")
    elif total_price > 2500:
        total = total_price
        total_label.config(text=f"Total: ₦{total}", fg="white")
        discount = 5
        final_price = calculate_discounted_price(total, discount)
        discount_label.config(text=f"Discount: {discount}%\nFinal Price: ₦{final_price}", fg="white")
    else:
        total = total_price
        total_label.config(text=f"Total: ₦{total}", fg="white")
        discount = 0
        final_price = calculate_discounted_price(total, discount)
        discount_label.config(text=f"Discount: {discount}%\nFinal Price: ₦{final_price}", fg="white")

# Function to handle the order process
def order():
    global items_list
    items_list = {
        "Jollof rice": 350, "Coconut Fried Rice": 350, "Jollof Spaghetti": 350, "Savoury beans": 350,
        "Roasted Sweet Potatoes": 300, "Fried Plantains": 150, "Mixed vegetable Salad": 150, "Boiled Yam": 150,
        "Eba": 100, "Poundo Yam": 100, "Semo": 100, "Atama Soup": 450,
        "Egusi Soup": 480, "Sweet Grilled Chicken": 1100, "Grilled Chicken Wings": 200, "Fried Beef": 400,
        "Fried Fish": 500, "Boiled Egg": 200, "Sauteed sausages": 200, "Water": 200,
        "Glass Drink(35cl)": 150, "PET Drink(35cl)": 300, "PET Drink(50cl)": 350, "Glass/Canned Malt": 500,
        "Fresh Yo": 600, "Pineapple Juice": 350, "Mango Juice": 350, "Zobo Juice": 350,
    }

    # Create the order window
    global order_window
    order_window = Tk()
    order_window.title("PAU Cafeteria Order")
    order_window.minsize(height=500, width=600)
    order_window.geometry("+650+0")
    order_window.config(bg="navy blue")

    Label(order_window, text="ORDER", font=("Times New Roman", 23, "bold"), fg="white", bg="navy blue").place(x=250, y=0)

    # Initialize variables for selected items and quantities
    global rice_var, sides_var, soups_var, proteins_var, beverages_var
    global quantity1_var, quantity2_var, quantity3_var, quantity4_var, quantity5_var
    
    rice_var = StringVar(order_window)
    sides_var = StringVar(order_window)
    soups_var = StringVar(order_window)
    proteins_var = StringVar(order_window)
    beverages_var = StringVar(order_window)

    item_options = list(items_list.keys())
    
    item_rice = list(item_options[0:3])
    item_rice.append("--select--")
    rice_var.set("--select--")

    item_sides = list(item_options[3:8])
    item_sides.append("--select--")
    sides_var.set("--select--")

    item_soups = list(item_options[8:13])
    item_soups.append("--select--")
    soups_var.set("--select--")

    item_proteins = list(item_options[13:19])
    item_proteins.append("--select--")
    proteins_var.set("--select--")

    item_beverages = list(item_options[19:28])
    item_beverages.append("--select--")
    beverages_var.set("--select--")

    Label(order_window, text='MENU ITEM', font=("Times New Roman", 20, "bold"), fg="white", bg="navy blue").place(x=200, y=90)

    # Create dropdown menus for item selection
    Label(order_window, text='RICE/PASTA', font=("Times New Roman", 15, "bold"), fg="white", bg="navy blue").place(x=0, y=120)
    OptionMenu(order_window, rice_var, *item_rice).place(x=250, y=120)
  
    Label(order_window, text="SIDES", font=("Times New Roman", 15, "bold"), fg="white", bg="navy blue").place(x=0, y=170)
    OptionMenu(order_window, sides_var, *item_sides).place(x=250, y=170)
    
    Label(order_window, text="SOUPS & SWALLOW", font=("Times New Roman", 15, "bold"), fg="white", bg="navy blue").place(x=0, y=220)
    OptionMenu(order_window, soups_var, *item_soups).place(x=250, y=220)

    Label(order_window, text="PROTEIN", font=("Times New Roman", 15, "bold"), fg="white", bg="navy blue").place(x=0, y=270)
    OptionMenu(order_window, proteins_var, *item_proteins).place(x=250, y=270)

    Label(order_window, text="BEVERAGES", font=("Times New Roman", 15, "bold"), fg="white", bg="navy blue").place(x=0, y=320)
    OptionMenu(order_window, beverages_var, *item_beverages).place(x=250, y=320)


    Label(order_window, text='QTY', font=("Times New Roman", 20, "bold"), fg="white", bg="navy blue").place(x=450, y=90)

    # Create dropdown menus for quantity selection
    quantity1_var = StringVar(order_window)
    quantity_options = list(range(0, 11))
    quantity1_var.set(quantity_options[0])

    OptionMenu(order_window, quantity1_var, *quantity_options).place(x=450, y=120)

    quantity2_var = StringVar(order_window)
    quantity2_var.set(quantity_options[0])
    OptionMenu(order_window, quantity2_var, *quantity_options).place(x=450, y=170)

    quantity3_var = StringVar(order_window)
    quantity3_var.set(quantity_options[0])
    OptionMenu(order_window, quantity3_var, *quantity_options).place(x=450, y=220)

    quantity4_var = StringVar(order_window)
    quantity4_var.set(quantity_options[0])
    OptionMenu(order_window, quantity4_var, *quantity_options).place(x=450, y=270)

    quantity5_var = StringVar(order_window)
    quantity5_var.set(quantity_options[0])
    OptionMenu(order_window, quantity5_var, *quantity_options).place(x=450, y=320)

    # Button to calculate and display the order total
    Button(order_window, text="CHECKOUT", command=calculate_order_total, width= 15, height= 3).place(x=250, y=400)

    order_window.mainloop()

# Function to create the menu window
def menu_window():

    home_win.destroy()

    menu = Tk()
    menu.title("PAU Cafeteria Menu")
    menu.minsize(height=550, width=600)
    menu.geometry("+0+0")
    menu.config(bg="navy blue")

    Label(menu, text="MENU", font=("Times New Roman", 23, "bold"), fg="white", bg="navy blue").place(x=250, y=0)

    # === RICE/PASTA category ===
    Label(menu, text="RICE/PASTA", font=("Times New Roman", 15, "bold"), fg="white", bg="navy blue").place(x=70, y=50)
    Label(menu, text="Jollof rice: ₦350", font=("calibri", 13), fg="white", bg="navy blue").place(x=20, y=75)
    Label(menu, text="Coconut Fried Rice: ₦350", font=("calibri", 13), fg="white", bg="navy blue").place(x=20, y=100)
    Label(menu, text="Jollof Spaghetti: ₦350", font=("calibri", 13), fg="white", bg="navy blue").place(x=20, y=125)

    # === SIDE DISHES category ===
    Label(menu, text="SIDE DISHES", font=("Times New Roman", 15, "bold"), fg="white", bg="navy blue").place(x=70, y=175)
    Label(menu, text="Savoury beans: ₦350", font=("calibri", 13), fg="white", bg="navy blue").place(x=20, y=200)
    Label(menu, text="Roasted Sweet Potatoes: ₦300", font=("calibri", 13), fg="white", bg="navy blue").place(x=20, y=225)
    Label(menu, text="Fried Plantains: ₦150", font=("calibri", 13), fg="white", bg="navy blue").place(x=20, y=250)
    Label(menu, text="Mixed vegetable Salad: ₦150", font=("calibri", 13), fg="white", bg="navy blue").place(x=20, y=275)
    Label(menu, text="Boiled Yam: ₦150", font=("calibri", 13), fg="white", bg="navy blue").place(x=20, y=300)

    # === SOUPS & SWALLOWS category ===
    Label(menu, text="SOUPS & SWALLOWS", font=("Times New Roman", 15, "bold"), fg="white", bg="navy blue").place(x=70, y=350)
    Label(menu, text="Eba: ₦100", font=("calibri", 13), fg="white", bg="navy blue").place(x=20, y=375)
    Label(menu, text="Poundo Yam: ₦100", font=("calibri", 13), fg="white", bg="navy blue").place(x=20, y=400)
    Label(menu, text="Semo: ₦100", font=("calibri", 13), fg="white", bg="navy blue").place(x=20, y=425)
    Label(menu, text="Atama Soup: ₦450", font=("calibri", 13), fg="white", bg="navy blue").place(x=20, y=450)
    Label(menu, text="Egusi Soup: ₦480", font=("calibri", 13), fg="white", bg="navy blue").place(x=20, y=475)

    # === PROTEINS category ===
    Label(menu, text="PROTEINS", font=("Times New Roman", 15, "bold"), fg="white", bg="navy blue").place(x=380, y=50)
    Label(menu, text="Sweet Grilled Chicken: ₦1100", font=("calibri", 13), fg="white", bg="navy blue").place(x=310, y=75)
    Label(menu, text="Grilled Chicken Wings: ₦200", font=("calibri", 13), fg="white", bg="navy blue").place(x=310, y=100)
    Label(menu, text="Fried Beef: ₦400", font=("calibri", 13), fg="white", bg="navy blue").place(x=310, y=125)
    Label(menu, text="Fried Fish: ₦500", font=("calibri", 13), fg="white", bg="navy blue").place(x=310, y=150)
    Label(menu, text="Boiled Egg: ₦200", font=("calibri", 13), fg="white", bg="navy blue").place(x=310, y=175)
    Label(menu, text="Sauteed sausages: ₦200", font=("calibri", 13), fg="white", bg="navy blue").place(x=310, y=200)

    # === BEVERAGES category ===
    Label(menu, text="BEVERAGES", font=("Times New Roman", 15, "bold"), fg="white", bg="navy blue").place(x=380, y=250)
    Label(menu, text="Water: ₦200", font=("calibri", 13), fg="white", bg="navy blue").place(x=310, y=275)
    Label(menu, text="Glass Drink(35cl): ₦150", font=("calibri", 13), fg="white", bg="navy blue").place(x=310, y=300)
    Label(menu, text="PET Drink(35cl): ₦300", font=("calibri", 13), fg="white", bg="navy blue").place(x=310, y=325)
    Label(menu, text="PET Drink(50cl): ₦350", font=("calibri", 13), fg="white", bg="navy blue").place(x=310, y=350)
    Label(menu, text="Glass/Canned Malt: ₦500", font=("calibri", 13), fg="white", bg="navy blue").place(x=310, y=375)
    Label(menu, text="Fresh Yo: ₦600", font=("calibri", 13), fg="white", bg="navy blue").place(x=310, y=400)
    Label(menu, text="Pineapple Juice: ₦350", font=("calibri", 13), fg="white", bg="navy blue").place(x=310, y=425)
    Label(menu, text="Mango Juice: ₦350", font=("calibri", 13), fg="white", bg="navy blue").place(x=310, y=450)
    Label(menu, text="Zobo Juice: ₦350", font=("calibri", 13), fg="white", bg="navy blue").place(x=310, y=475)

    order()
    menu.mainloop()

home()