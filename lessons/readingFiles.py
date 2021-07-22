#read -r, write -w, append -a, reading and writing - r+
countryFile = open('countries.txt', 'r')
#Can the file be accessed?
print(countryFile.readable())

#print one line from the file contents
print(countryFile.readline())

#print another line from the file
print(countryFile.readline())

#print all lines
print(countryFile.readlines())

#other way to read file
for files in countryFile.readlines():
    print(files)

#always close the file
countryFile.close()