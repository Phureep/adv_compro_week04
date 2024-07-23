numbers = [1,2,3,4,5]
modify_numbers = [n+10 if n%2 == 0 else n-1 for n in numbers]
print(modify_numbers)