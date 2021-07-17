def greetings_function(name, age):
    print('Welcome ' + name + '. You are ' + str(age) + ' years old.')

greetings_function('John', 27)

#another way to pass arguments in the funtion
greetings_function(name = 'Tim', age = 25)

#user input arguments
name = input('Enter your name: ')
age = input('Enter your age: ')
greetings_function(name, age)

#unknown number of arguments passed - use array indexing
def random_function(*names):
    print('Welcome ' +names[1])

random_function('John', 'Tim', 'Tom')