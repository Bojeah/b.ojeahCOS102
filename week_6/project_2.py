from tkinter import *
from tkinter import messagebox

def comp_sc():

	def button():
		name = name_entry.get()

		interview = str(interview_entry.get())
		jamb = int(jamb_entry.get())

		credit = 0

		for grade_value in grade_entries:
			grade = str(grade_value.get())

			if grade.lower() in ["a1", "b2", "b3", "c4", "c5", "c6"]:
				credit += 1

			else:
				credit += 0

		if jamb >= 250 and credit == 5 and interview.lower() == "pass":
			messagebox.showinfo("ADMISSION", f"CONGRATULATIONS {name}!! YOU HAVE BEEN ADMITTED INTO PAU")
			admitted.append(name)
			print(admitted)
		else:
			messagebox.showinfo("ADMISSION", "YOUR APPLICATION FOR ADMISSION HAS BEEN REJECTED AS YOU DID NOT MEET NESSECARY REQUIREMENTS")
			not_admitted.append(name)
			print(not_admitted)

	window1 = Tk()
	window1.title("Computer science")
	window1.minsize(height = 500, width = 500)

	Label(window1, text = "Enter JAMB score").pack()
	jamb_entry = Entry(window1)
	jamb_entry.pack()

	subjects = ["Math", "English", "Chemistry", "Physics", "Biology"]
	grade_entries = []
	Label(text= "PLEASE IPUT THE GRADES YOU AQUIRED IN THE FOLLOWING SUBJECTS IN WAEC")

	for subject in subjects:
		Label(window1, text = subject).pack()
		grade_entry = Entry(window1)
		grade_entry.pack()
		grade_entries.append(grade_entry)


	Label(window1, text = "Interview status (pass/fail)").pack()
	interview_entry = Entry(window1)
	interview_entry.pack()

	Button(window1, text= "submit", command = button).pack()

def mass_com():

	def button():
		name = name_entry.get()

		interview = str(interview_entry.get())
		jamb = int(jamb_entry.get())

		credit = 0

		for grade_value in grade_entries:
			grade = str(grade_value.get())

			if grade.lower() in ["a1", "b2", "b3", "c4", "c5", "c6"]:
				credit += 1

			else:
				credit += 0

		if jamb >= 230 and jamb <= 400 and credit == 5 and interview.lower() == "pass":
			messagebox.showinfo("ADMISSION", f"CONGRATULATIONS {name}!! YOU HAVE BEEN ADMITTED INTO PAU")
			admitted.append(name)
			print(admitted)
		else:
			messagebox.showinfo("ADMISSION", "YOUR APPLICATION FOR ADMISSION HAS BEEN REJECTED AS YOU DID NOT MEET NESSECARY REQUIREMENTS")
			not_admitted.append(name)
			print(not_admitted)

	window1 = Tk()
	window1.title("Mass communication")
	window1.minsize(height = 500, width = 500)

	Label(window1, text = "Enter JAMB score").pack()
	jamb_entry = Entry(window1)
	jamb_entry.pack()

	Label(text= "PLEASE IPUT THE GRADES YOU AQUIRED IN THE FOLLOWING SUBJECTS IN WAEC")

	subjects = ["Math", "English", "Government", "Economics","LITERATURE"]
	grade_entries = []

	for subject in subjects:
		Label(window1, text = subject).pack()
		grade_entry = Entry(window1)
		grade_entry.pack()
		grade_entries.append(grade_entry)


	Label(window1, text = "Interview status (pass/fail)").pack()
	interview_entry = Entry(window1)
	interview_entry.pack()

	Button(window1, text= "submit", command = button).pack()



def button_clicked():
	department = department_entry.get()

	if department.lower() == "computer science":
		comp_sc()
	elif department.lower() =="mass communication":
		mass_com()
	else:
		messagebox.showerror("Error", "We do not have this department in our school")
admitted = []
not_admitted = []

root = Tk()
root.title("PAU ADMISSION PORTAL")
root.geometry("500x200")

Label(text = "Enter name").pack()
name_entry = Entry()
name_entry.pack()

Label(text = "Enter Department (in full)").pack()
department_entry = Entry()
department_entry.pack()

Button(text = "submit", command = button_clicked).pack()

root.mainloop()