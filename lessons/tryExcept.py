try:
    x = int(input('Input an integer: '))
    print(x)
except:
    print('Something went wrong')

#Except with specific error
try:
    x = int(input('Input a number: '))
    print(x)
except ValueError:
    print('Value is not an integer')

#else after try except
try:
    x = int(input('Input an integer: '))
    print(x)
except:
    print('Something went wrong')
else:
    print('nothing went wrong')

#using finally - executes regardless of error
try:
    x = int(input('Input an integer: '))
    print(x)
except:
    print('Something went wrong')
finally:
    print('try except finished')


    