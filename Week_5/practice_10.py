import tkinter as tk
from tkinter import messagebox

#Handling button click event
def button_click():
	print("Button clicked!")

	#Show an information message box
	messagebox.showinfo("Info", "Welcome to COS 102 GUI App!\n")

	#Ask for user confirmation
	result = messagebox.askyesno("Confirmation", "Do you want to continue?")

#create the main window
root = tk.Tk()
root.title("Home Page")
root.geometry("300x100")

#Add label widget
label = tk.Label(root, text = "Hello friend\n")
label.pack()

#Add button widget
button = tk.Button(root, text = "Click Me!", command=button_click)
button.pack()

#Styling the button widget
button.config(fg="blue", bg="yellow")

#Start the event loop
root.mainloop()
