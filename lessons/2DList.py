my_list = {1, 2, 3, 4}
print(my_list)

my_nested_list = [
    [1, 2, 3],
    [4,5, 6],
    [7, 8, 9]
]
print(my_nested_list)

#Get an element value from 2D list
print(my_nested_list[1][1])

#nested loop is a for loop within a for loop
for lists in my_nested_list:
    for row in lists:
        print(row)