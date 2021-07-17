#return statements are the last statements in a function, no block of code can be written after that 
def my_function():
    return 5+4

print(my_function())

def add_numbers(num1, num2):
    return num1+num2

print(add_numbers(2, 3))

num1= int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print(add_numbers(num1, num2))