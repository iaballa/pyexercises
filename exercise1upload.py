# Exercise 1 from https://pynative.com/python-basic-exercise-for-beginners/
# "Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum."

def main():  
# Getting user input
    try:
        number1 = int(input("First number: "))
    except ValueError:
        number1 = int(input("Try again, this time inputting a number: "))
    print("First number selected: " + str(number1))  

    try:
        number2 = int(input("Second number: "))
    except ValueError:
        number2 = int(input("Try again, this time inputting a number: "))
    print("Second number selected: " + str(number2))

    if (number1 * number2) > 1000:
        print("Product is greater than 1000. Summing...")
        print("Result is: " + str(number1 + number2))
    else:
        print("Result is: " + str(number1 * number2))

# git test