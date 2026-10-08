# Max DeRocher
# 9/9/2026
# This is my week 3 lab prep assignment



age = int(input("How many years old are you?"))

if age >= 0 and age < 13:
    print("Child")
    
elif age >= 13 and age <= 17:
    print("Teen")
    
elif age >= 18 and age < 65:
    print("Adult")
    
elif age >= 65 and age <= 105:
    print("Senior")

else:
    print("Invalid age input")

