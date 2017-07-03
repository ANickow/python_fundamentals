def compare_arrays(arr1, arr2):
    # First checks if they are the same length.  If not, prints they are not the same and breaks
    if len(arr1) != len(arr2):
        print "The lists are not the same."
        return
    # Iterates through the indices of the arrays and compares.  Breaks if it finds non-matching values
    for index in range(0, len(arr1)):
        if arr1[index] != arr2[index]:
            print "The lists are not the same."
            return
    print "The lists are the same"

# Test cases

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
print "=" * 50
print "Expected: same"
compare_arrays(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
print "=" * 50
print "Expected: not the same"
compare_arrays(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
print "=" * 50
print "Expected: not the same"
compare_arrays(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
print "=" * 50
print "Expected: not the same"
compare_arrays(list_one, list_two)