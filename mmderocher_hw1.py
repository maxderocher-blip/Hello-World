# Max DeRocher
# 9/13/2026
# Homework 1

# Part 1

# Item price
item_price = float(input("Item price:"))

# Number of items
quantity = int(input("Quantity:"))

# Subtotal
subtotal = float(item_price * quantity)

# Sales tax (%)
SALES_TAX = .075

# Sales tax ($)
tax_amount = float(SALES_TAX * subtotal)

# Total with sales tax
total = float(subtotal * (1 + SALES_TAX))

# Final display
print("Subtotal: $", round(subtotal, 2))
print("Tax: $", round(tax_amount, 2))
print("Total $:", round(total, 2))

# Part 2

# Hourly Wage
hourly_wage = float(input("Hourly wage: $"))

# Hours worked
hours_worked = float(input("Hours worked: "))

# Base pay
base_pay = hourly_wage * hours_worked

#Overtime Hours
overtime_hours = hours_worked - 40

# Overtime Pay
overtime_pay = hourly_wage * 1.5

# Total Pay
total_pay = base_pay + overtime_pay

# Pay if working overtime
if hours_worked > 40:
    print("Base pay: $", round(base_pay, 2))
    print("Overtime pay: $", round(overtime_pay, 2))
    print("Total pay: $", round(total_pay, 2))
    
# Pay if no overtime
else:
    print("Pay: $", round(base_pay, 2))


# Part 3

# Numeric Grade
numeric_grade = float(input("Grade = ___%:"))

# Converting numeric grade to letter grade
if numeric_grade >= 0 and numeric_grade < 60:
    print("Letter grade: F")
    
elif numeric_grade >= 60 and numeric_grade < 70:
    print("Letter grade: D")
    
elif numeric_grade >= 70 and numeric_grade < 80:
    print("Letter grade: C")
    
elif numeric_grade >= 80 and numeric_grade < 90:
    print("Letter grade: B")
    
elif numeric_grade >= 90 and numeric_grade <=100:
    print("Letter grade: A")
    
else:
    print("Invalid input")

###Test Cases###

# -1 = "Invalid input"
# 101 = "Invalid input"
# 0 =  "Letter grade: F"
# 59 =  "Letter grade: F"
# 60 =  "Letter grade: D"
# 69 =  "Letter grade: D"
# 70 =  "Letter grade: C"
# 79 =  "Letter grade: C"
# 80 =  "Letter grade: B"
# 89 =  "Letter grade: B"
# 90 =  "Letter grade: A"
# 99 = "Letter grade: A"
# 100 = "Letter grade: A"

# Part 4

# Hours worked
hours_worked = int(input("How many hours did you work?"))

# Performance score
performance_score = int(input("What is your performance score?"))

# Conditions for bonus
if hours_worked > 35 and performance_score > 85:
    print("You are eligible for a $100 bonus!")
    
else:
    print("Sorry, you are not eligible for a bonus.")
    
### Test cases ###

# 36, 86 = "You are eligible for a $100 bonus!"
# 36, 85 = "Sorry, you are not eligible for a bonus."
# 35, 86 = "Sorry, you are not eligible for a bonus."
# 35, 85 = "Sorry, you are not eligible for a bonus."






    