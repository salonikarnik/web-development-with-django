list1 = [1, 2, 3, 4, 5]
list2 = ['banana', 'apples', 'mango','oranges']
list3 = [4, 5, 3, 1, 2]

#join first list with the second list
list1.extend(list2)
print(list1)

#adding element to the list at the end
list2.append('cherry')
print(list2)
print(len(list2))

#insert values in a list
list2.insert(1, 'kiwi')
print(list2)

#remove a value from the list
list2.remove('banana')
print(list2)

#delete the whole list - we get an emoty list
list2.clear()
print(list2)

#get index number of an element
list2 = ['banana', 'apples', 'mango', 'oranges', 'mango']
print(list2.index('mango'))

#get count of an element occurring in the list
print(list2.count('mango'))

#sort list in ascending order
list3.sort()
print(list3)

#reverse a list
list2 = ['banana', 'apples', 'mango', 'oranges']
list2.reverse()
print(list2)

#duplicate a list
list4 = list2.copy
print(list4)

#remove the last value in a list - use pop()
list2.pop()
print(list2)

#delete value within the list
del list2[0]
print(list2)

#deleting a list will delete the list but clear will retain the list variable
del list2
print(list2)