grades = [55, 70, 65, 40, 90, 85, 50, 77]
passed_with_bonus = list(map(lambda x: x + x*(5/100),filter(lambda x: x > 60, grades)))

print("Grades after filtering and applying bonus: ",passed_with_bonus)