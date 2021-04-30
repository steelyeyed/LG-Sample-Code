# Use of Zip example

x = [1, 2, 3, 4, 5]
y = [ 6, 7, 8, 9, 10]
z = ['a', 'b', 'c','d','e']

for a,b in zip(x,y):
    print (a, b)

#  the following creates an obect
#  which is iterated over creating a tuple of values

for i in zip(x,y,z): 
    print (i)

# list comprehension with ZIP
[print(a,b,c) for a,b,c in zip(x,y,z)]

# creating a dictionary from ZIP
print(dict(zip(x,z)))


