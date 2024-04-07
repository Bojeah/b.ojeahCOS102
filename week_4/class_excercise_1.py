# python program to swap two cities

# To take input from user
city_1 = input("Enter name of city 1: ")
city_2 = input("Enter name of city 2: ")

#create a temprory variable and swap the cities
temp = city_1
city_1 = city_2
city_2 = temp

print(f"The name of city 1 after swapping is {city_1}")
print(f"The name of city 2 after swapping is {city_2}")