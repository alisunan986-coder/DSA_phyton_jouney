my_string ="hello world!"
print(my_string)


numbers = range(0, 10)  # Numbers from 0 to 9
print(tuple(numbers))
user = {"name": "Bob", "age": 30, "is_admin": True}
print(user)
unique_ids = {101, 102, 103, 101}  # The duplicate 101 is automatically removed
print(unique_ids)
is_logged_in = True
has_cheeseburger = False
print(is_logged_in)
print(has_cheeseburger)
#only list, dict and set are mutable the rest are immutable.
#PEMDAS

#The order of priority from highest to lowest is:

#Parentheses ()

#Exponents 

#Multiplication *, Division /, Floor Division //, and Modulo % (evaluated left-to-right)

#Addition + and Subtraction - (evaluated left-to-right)
result = 5 + 3 * 2 ** 2
print(result)

#calc with input
# Taking inputs from the user
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Converting strings to floats so we can handle decimals
number1 = float(num1_str)
number2 = float(num2_str)

# Performing calculations
sum_result = number1 + number2
product_result = number1 * number2
print("Sum:", sum_result)
print("difference:", number1 - number2)
print("Product:", product_result)

#f-strings(formatted strings)
name = "Alice"
age = 25
print(f"Hello, {name}! You are {age} years old.")

# 1. Gather numerical inputs
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# 2. Evaluate the expression
# Python calculates the right side first, then assigns it to 'area'
area = 0.5 * base * height

# 3. Display the computed results
print(f"\n--- Results ---")
print(f"Base provided: {base}")
print(f"Height provided: {height}")
print(f"The total area of the triangle is: {area}")

# Bonus: Formatting decimals to 2 decimal places using :.2f
print(f"Formatted Area: {area:.2f}")
#day 4 if-else
is_raining = True

if is_raining:
    print("Take an umbrella!")

    score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

    #another example
    number = 150

if number == 0:
    print(f"the number {number} belongs to the category: ZERO")
elif number > 100:
    print(f"the number {number} belongs to the category: LARGE")
elif number > 0:
    print(f"the number {number} belongs to the category: POSITIVE")
else:
    print(f"The number {number} belongs to the category: NEGATIVE NUMBER.")