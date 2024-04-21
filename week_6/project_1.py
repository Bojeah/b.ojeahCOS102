from tkinter import *
from tkinter import messagebox

def button_clicked():
	weight = float(weight_entry.get())
	location = location_entry.get()

	if location.lower() == "ibeju-lekki" or location.lower() == "ibeju lekki" or location.lower() == "ibeju-lekki community" or location.lower() == "ibeju lekki community":
		if weight >= 10.0:
			messagebox.showinfo("Receipt", "DELIVERY FEE: N 5000")

		else:
			messagebox.showinfo("Receipt", "DELIVERY FEE: N 3500")

	elif location.lower() == "epe":
		if weight >= 10.0:
			messagebox.showinfo("Receipt", "DELIVERY FEE: N 10000")

		else:
			messagebox.showinfo("Receipt", "DELIVERY FEE: N 5000")

	else:
		messagebox.showerror("Error", "We do not deliver to this location")

root = Tk()
root.config(bg = "black")
root.title("DELIVERY MENU")
root.minsize(width = 500, height = 250)

Label(root, text = "SIMI SERVICES", font = ("MV Boli", 40, "bold"), bg = "black", fg = "gold").grid(row = 1, column = 3)

Label(root , text = "DELIVERY LOCATIONS", font = ("calibri", 15, "bold"), bg = "black", fg = "white").grid(row = 3, column = 1)

Label(root , text = "- EPE", font = ("calibri", 15, "bold"), bg = "black", fg = "white").grid(row = 4, column = 1)

Label(root , text = "- IBEJU-LEKKI COMMUNITY", font = ("calibri", 15, "bold"), bg = "black", fg = "white").grid(row = 5, column = 1)

Label(root, text = "Package Weight (Kg)", font = ("calibri", 15), bg = "black", fg = "white").grid(row = 3, column = 4)
weight_entry = Entry(root)
weight_entry.grid(row = 4, column = 4)

Label(root, text = "Delivery Location", font = ("calibri", 15), bg = "black", fg = "white").grid(row = 5, column = 4)
location_entry = Entry(root)
location_entry.grid(row = 6, column = 4)


Button(root, text = "Dispatch", fg = "black", bg = "gold", command = button_clicked).grid(row = 7, column = 4)


root.mainloop()
 