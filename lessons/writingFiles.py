#open the file to write in and create a new file if file doesn't exist
countryFile = open('C:/Users/Saloni/Visual Studio Code Workspace/Python Backend Web Development Course/lessons/country.txt', 'w')
countryFile.write('This is the new country file')

#change from w to a, so that matter can be appended to the file
countryFile = open('C:/Users/Saloni/Visual Studio Code Workspace/Python Backend Web Development Course/lessons/country.txt', 'a')
countryFile.write('This is a new line')

#the appended line is next to the original content, so we add new line character
countryFile = open('C:/Users/Saloni/Visual Studio Code Workspace/Python Backend Web Development Course/lessons/country.txt', 'a')
countryFile.write('\nThis is a new line')