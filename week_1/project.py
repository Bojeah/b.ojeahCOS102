#function for czlculating simple interest
def s_interest():
	print("\nYOU ARE CALCULATING SIMPLE INTEREST\n")

	# asking user for needed parameters
	p = float(input("PRINCIPLE(₦): "))
	r = float(input("RATE(%): "))
	t = float(input("TIME(Yrs): "))
    
    #calculating simple interest
	amount = (p * (1 + (r * 0.01) * t)) + p
	interest= (p * (1 + (r * 0.01) * t))

	print(f"\nAfter {t} years with an interest rate of {r}%, you will have ₦{round(amount, 2)}K")
	print(f"That is an interest of ₦{round(interest, 2)}K")

#function for calculating compound interest
def c_interest():
	print("\nYOU ARE CALCULATING COMPUND INTEREST\n")

	# asking user for needed parameters
	p = float(input("PRINCIPLE(₦): "))
	r = float(input("RATE(%): "))
	t = float(input("TIME(Yrs): "))
	n = float(input("Number of compounding periods per year: "))
    
    #calculating compound interest
	amount = (p * (1 + (r * 0.01 / n)) ** (n * t)) + p
	interest = (p * (1 + (r * 0.01 / n)) ** (n * t))

	print(f"\nAfter {t} years with an interest rate of {r}%, you will have ₦{round(amount, 2)}K")
	print(f"That is an interest of ₦{round(interest, 2)}K")

#Fuction for calculating annuity
def annuity():
	print("\nYOU ARE CALCULATING ANNUITY\n")

	#asking for user needed parameters
	p = float(input("Periodic payment (annuity payment)(₦): "))
	n = int(input("Compounding periods per year: "))
	t = float(input("Time(Yrs): "))
	r = float(input("Rate(%): "))

	#calculating amount paid by user to the company/ organization he/she would be recieving annuity from
	amt_paid =  p * ((1 - (1 +(r * 0.01 / n)) ** (-1 * n * t)) / (r * 0.01 / n)) 
	#calculating the total amount the user would be getting from the company over the given period of time
	amt_recieved = p * n * t
	#calculating interest the user will recieve
	interest = amt_recieved - amt_paid

	print(f"\nAfter {t} years, you would have:")
	print(f"Paid: ₦{round(amt_paid, 2)}K")
	print(f"Recieved: ₦{round(amt_recieved, 2)}K")
	print(f"An interest of : ₦{round(interest, 2)}K")

print("INTEREST CALCULATOR")
print("\n1.) SIMPLE INTEREST\n2.) COMPOUND INTEREST\n3.) ANNUITY PLAN")
Input = int(input("Choose the index of what you would like to calculate:\n"))

if Input == 1:
	s_interest()

elif Input == 2:
	c_interest()

elif Input == 3:
	annuity()

else:
	print("Invalid input")
