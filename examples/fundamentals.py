# Strings
data = 'python program !'

print(data[0])
print(len(data))
print(data[15])
print(data)
print(" ")

# Number
value = 123.1
print(value)
value = 10
print(value)
print(" ")


# Boolean
a = True
b = False
print(a, b)
print(" ")

# Multiple Assignment
a, b, c = 1, 2, 3
print(a, b, c)
print(" ")

# No value
a = None
print(a)

# If conditions
value = 99
if value == 99:
    print ('That is fast')
elif value > 200:
    print ('That is too fast')
else:
    print ('That is safe')

# For-Loop
for i in range(10):
  print (i)


# While-Loop
i=0
while i < 10:
    print (i)
    i += 1

# Tuple
a = (1, 2, 3)
print (a)

# List
mylist = [1, 2, 3]
print('Zeroth Value {:d}'.format(mylist[0]))

mylist.append(4)
print('List Length: {:d}'.format(len(mylist)))

for value in mylist:
    print (value)

# Dictionary
mydict = {'a': 1, 'b': 2, 'c': 3}
print('A value: {:d}'.format(mydict['a']))

mydict['a'] = 11
print('A value: {:d}'.format(mydict['a']))

print("Key and String !")

print('Keys: {}'.format(mydict.keys()))
print('Values: {}'.format(mydict.values()))

print("All keys ")
for key in mydict.keys():
  print (mydict[key])

print("Test function")
# Sum function
def mysum(x, y):
    return x + y

# Test sum function
result = mysum(1, 3)
print(result)



