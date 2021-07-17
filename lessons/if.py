a=4
b=3
c='Tim'
d='Tim'
e=True
f= False

if a>b:
    print(str(a) + ' is greater than ' + str(b))

if c == d:
    print('c is equal to d')

if e ==True:
    print('e is true')

if f!=True:
    print('f is false')

if a==b:
    print('a equals B')
else:
    print('a not equal to b')

if e==True:
    print('e is true')
else:
    print('e is not true')

if e == True:
    print('e is true')
elif e == False:
    print('e is false')
else:
    print('e is none of the two')

boy = True
short = True

value = input('Input a value: ')

if boy == True or short == False:
    print('He is a boy or he is short')

if boy == True and short == False:
    print('He is a boy or he is short')

if type(value) == str:
    print(value + 'is a string')
elif type(value) == int:
    print(value + ' is an integer')
elif type(value) == list:
    print(value + 'is a list')
else:
    print('We do not know the data type of ' + value)

number = int(input('enter a number'))
if number%5 == 0:
    print(number, 'is divisible by 5')
else:
    print(number, 'cannot be divided by 5')

