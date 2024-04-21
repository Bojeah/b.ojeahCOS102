import tkinter as tk
from tkinter import messagebox

def welcomemessage(username):
	#create a tkinter window
	window = tk.Toplevel(root)
	window.title("Admin Box")
	window.geometry("500x200")

	label_1 = tk.Label(window, text=f"Welcome {username}\n")
	label_1.pack()
	label_2 = tk.Label(window, text=f"This is python GUI with tkinter")
	label_2.pack()


	#Run the tkinter event loop
	root.mainloop()

def submit():
	username = username_entry.get()
	password = password_entry.get()

	if username == "Benedict" and password == "cos102":
		welcomemessage(username)
	else:
		messagebox.showerror("Login", "Invalid username or password")

#create main window
root = tk.Tk()
root.title("login form")
root.geometry("500x200")


# create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# create password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create submit button
submit_button = tk.Button(root, text="submit", command=submit)
submit_button.pack()

#run the main event loop
root.mainloop()