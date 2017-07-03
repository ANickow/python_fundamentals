def typeList(var):
    listType = type(var[0])
    print listType
    for element in var:
        # Determine if list is mixed or not
        if type(element) != listType:
            listType = "mixed"
        # Find integers and add to the sum
        if isinstance(element, int):
            listSum += element
        # Find strings and add to concatenated string
        if isinstance (element, str):
            listStr += element
        # Find lists and add to matrix
        if isinstance (element, list):
            listMtrx += element
    print listType


# Test the function
x = [4,3,2,1,"zero"]
typeList(x)