countries = ['United States', 'India', 'Canada', 'Australia', 'United Kingdom']
print(countries)

#print only first country
print(countries[0])

#get a country and the first letter of it
print(countries[2][0])

#get countries from a particular list element to end
print(countries[1:])

#get countries from a range
print(countries[1:3])

#type of the variable 'countries'
print(type(countries))

#change value in a list
countries[0] = 'France'
countries[3] = 'Italy'
print(countries)

#getting end of the list
print(countries[-1])

#(-)ve sign returns element from the back - getting second last item the list
print(countries[-2])

#length of the list
print(len(countries))

#instead of square brackets, a list contructor can be used to build lists
cities = list(('Dallas', 'Austin', 'San Francisco'))
cities2= ['Dallas', 'Austin', 'San Francisco']
print(cities)
print(cities2)
