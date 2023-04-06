#to execute in terminal:
# python .\09_01_files.py

# Use open function to read the content of a file!
# f = open('sample.txt', 'r')
f = open('sample.txt') # by default the mode is r
data1 = f.read(5)# reads first 5 characters from the file
data2 = f.read() # reads the rest of the file
print(data1)
print(data2)
f.close()