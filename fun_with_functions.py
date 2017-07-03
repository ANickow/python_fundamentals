# Odd/Even
def odd_even():
    for number in range (1, 2001):
        if number % 2 == 0:
            oe = "even"
        else: 
            oe = "odd"
        response = "Number is {}.  This is an {} number.".format(number, oe)
        print response

# Multiply
def multiply(arr, m):
    for index in range (0, len(arr)):
        arr[index] *= m
    return arr

# Hacker Challenge
def layered_multiples(arr):
    new_array = []
    for item in arr:
        sub_array = []
        for x in range (0, item):
            sub_array.append(1)
        new_array.append(sub_array)
    return new_array


test the functions
odd_even()
a = [2, 4, 10, 16]
print multiply(a, 5)
x = layered_multiples(multiply([2,4,5],3))
print x