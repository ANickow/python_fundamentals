columns ='x  1  2  3  4  5  6  7  8  9  10  11  12'

# create the row
def create_products_row(x):
    row = str(x)
    for y in range(1, 13):
        product = x * y
        row += "  " + str(product)
    return row

# iterate through rows and print full table
print columns
for x in range(1, 13):
    print create_products_row(x)
