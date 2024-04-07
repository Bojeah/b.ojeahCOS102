response = int(input("How many staff members information woud you like to input?\n"))

staff_atr = []
staff_age = []
staff_exp = []
staff_names = []

i = 0

while i < response:
    print(f"STAFF {i + 1} INFORMATION")
    print("-" * 20)
    name = input("Name: ")
    age = int(input("Age: "))
    exp = int(input("Years of experience: "))

    if exp > 25 and age >= 55:
        atr = 5600000
        i += 1
        staff_atr.append(atr)
        staff_names.append(name)
        staff_age.append(age)
        staff_exp.append(exp)


    elif exp > 20 and age >= 45:
        atr = 4480000
        i += 1
        staff_atr.append(atr)
        staff_names.append(name)
        staff_age.append(age)
        staff_exp.append(exp)


    elif exp > 10 and age >= 35:
        atr = 1500000
        i += 1
        staff_atr.append(atr)
        staff_names.append(name)
        staff_age.append(age)
        staff_exp.append(exp)

    elif exp < 10 and age < 35:
        atr = 550000
        i += 1
        staff_atr.append(atr)
        staff_names.append(name)
        staff_age.append(age)
        staff_exp.append(exp)

    elif exp > age:
        print("Invalid input")

    elif age > 65 or age < 18:
        print("Age not withing working class range")

    else:
        print("\nStaff credentials don't allign with atr requirements\n")


print("\nSTAFF INFORMATION")
print("-" * 17)
print(f"{"NAME":<15}| {"AGE":<5}| {"EXPERIENCE(YEARS)":<20}| {"ANNUAL TAX REVENUE(ATR)"}")
print("-" * 70)
for i in range(response):
    print(f"{staff_names[i]:<15}| {staff_age[i]:<5}| {staff_exp[i]:<20}| {staff_atr[i]}")