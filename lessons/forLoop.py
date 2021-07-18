mylist = ['ji', 'ju', 'jo']

mydict = {
    'name': 'john',
    'age': 13
}

#iterate over a string/word
for letter in 'Hello':
    print(letter)

#iterate over a list
for values in mylist:
    print(values)

#iterate over dictionary
for values in mydict:
    print(values)

#break in for loop
for values in mylist:
    print(values)
    if values == 'ju':
        break

#this will break before printing since python runs code line by line
for values in mylist:    
    if values == 'ju':
        break
    print(values)

for x in range(4):
    print(x)

for x in range(3, 7):
    print(x)

#else in for loop
for x in range(7):
    print(x)
else:
    print('Finished Looping!')