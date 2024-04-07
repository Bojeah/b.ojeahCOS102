# Data for girls
girl_names = ["Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"]
girl_ages = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17]
girl_heights = [5.5, 6.0, 5.4, 5.9, 5.6, 5.5, 6.1, 6.0, 5.7, 5.5]
girl_scores = [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]

# Data for boys
boy_names = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
boy_ages = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19]
boy_heights = [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7]
boy_scores = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

# Print the table header
print(f"{'Name':<10}| {'Age':<5}| {'Height':<8}| {'Score'}")
print("-" * 40)

# Print girls' data
for i in range(len(girl_names)):
    print(f"{girl_names[i]:<10}| {girl_ages[i]:<5}| {girl_heights[i]:<8}| {girl_scores[i]}")

# Print boys' data
for i in range(len(boy_names)):
    print(f"{boy_names[i]:<10}| {boy_ages[i]:<5}| {boy_heights[i]:<8}| {boy_scores[i]}")
