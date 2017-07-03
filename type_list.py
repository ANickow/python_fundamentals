def type_list(arr):
    list_type = type(arr[0])
    if list_type is int:
        message_type = 'integer'
    if list_type is float:
        message_type = 'float'
    if list_type is str:
        message_type = 'string'
    arr_sum = 0
    arr_str = ""
    for item in arr:
        item_type = type(arr[1])
        # check to see if all items in the array are the same type.  
        # If not, save message_type as "mixed".
        if item_type != list_type:
            message_type = 'mixed'
        # If it's an integer or float, add it to the sum
        if isinstance(item, int) or isinstance(item, float):
            arr_sum += item
        # If it's a string, add it to the concatenated string
        if isinstance(item, str):
            arr_str += " " + item       
    # Print messages 
    print "The array you entered is of {} type".format(message_type)
    if message_type == 'string' or message_type == 'mixed':
        print "String:", arr_str
    if message_type == 'integer' or message_type == 'float' or message_type == 'mixed':
        print "Sum:", arr_sum

# Test using 3 sample lists
arr1 = ['magical unicorns', 19, 'hello', 98.98, 'world']
arr2 = [2,3,1,7,4,12]
arr3 = ['magical','unicorns']
print '=' * 50
print "Expected: Mixed, magical unicorns hello world, 117.98"
print "-" * 10
type_list(arr1)
print '=' * 50
print "Expected: Integer, 29"
print "-" * 10
type_list(arr2)
print '=' * 50
print "Expected: String, magical unicorns"
print "-" * 10
type_list(arr3)


