from tkinter import *
from tkinter import messagebox

def logged_in():
	log = Tk()
	log.minsize(width=500, height=200)
	log.title("Welcome")

	label_2 = Label(log, text="YOU HAVE SIGNED IN SECESSFULLY", font=("Arial", 30, "bold"))
	label_2.place(x=250, y=100)

# Creating window
window = Tk()
window.geometry("500x200")
window.title("Login")

#Creating a username label
username = Label(window, text="USERNAME")
username.pack()

#creating a username entry
user_entry = Entry()
user_entry.pack()

#creating password label
password = Label(window, text="PASSWORD")
password.pack()

#Creating a password entry
pass_entry = Entry()
pass_entry.pack()


def button_clicked():
	# messagebox.askyesno("Error","Are you good")
	Username = user_entry.get()
	Password = pass_entry.get()

	if Username == "Benedict" and Password == "Trinity07":
		logged_in()
	else:
		messagebox.showerror("Error","INCORRECT USERNAME OR PASSWORD")

#Creating login button
login_button = Button(window, text="Login", command=button_clicked)
login_button.pack()

window.mainloop()