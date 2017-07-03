# Multiples Part I (using a for loop and a conditional to check if count is odd):
for count in range (1, 1000):
    if count % 2 == 1:
        print count

# Multiples Part II (using a for loop with a counter of 5):
for count in range (5, 1000001, 5):
    print count

# Sum List
a = [1,2,5,10,255,3]
sum = 0
for element in a:
    sum += element
print sum

# Average List (using the sum found above) - float used to ensure accurate response if not even division
avg = float(sum)/len(a)
print avg