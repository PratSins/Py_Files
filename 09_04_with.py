with open('another.txt', 'r') as f:
    a = f.read()
    
print(a)

with open('another.txt', 'w') as f:
    a = f.write("me1 g")

print(a) # returns the length of the string written to the file