# Find and Replace
words = "It's thanksgiving day.  It's my birthday, too!"
print words.find('day')
print words.replace('day', 'month')

# Min and Max
x = [2, 54, -2, 7, 12, 98]
print min(x)
print max(x)


# First and Last
x = ['hello', 2, 54, -2, 7, 12, 98, 'world']
print x[0]
print x[len(x)-1]
y = [x[0], x[len(x)-1]]
print y

# New List
x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
x.sort()
y = x[:len(x)/2]
z = x[(len(x)/2 + 1):]
z.insert(0,y)
print z
