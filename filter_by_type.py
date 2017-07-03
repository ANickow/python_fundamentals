def filter_by_type(var):
    # Find integers then choose response
    if isinstance(var, int):
        if var >= 100:
            print "That's a big number!"
        else:
            print "That's a small number."
    # Find strings then choose response
    if isinstance (var, str):
        if len(var) >= 50:
            print "Long sentence."
        else:
            print "Short sentence."
    # Find lists then choose response
    if isinstance (var, list):
        if len(var) >= 10:
            print "Big list!"
        else:
            print "Short list."

# Variables for testing the program
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

# Testing integer variables
print "INTEGERS - Expected: small, long, long, small small"
filter_by_type(sI)
filter_by_type(mI)
filter_by_type(bI)
filter_by_type(eI)
filter_by_type(spI)
# Testing string variables
print "STRINGS - Expected: short, long, long short"
filter_by_type(sS)
filter_by_type(mS)
filter_by_type(bS)
filter_by_type(eS)
# Testing list variables
print "LISTS - Expected: short, big, big, short short"
filter_by_type(aL)
filter_by_type(mL)
filter_by_type(lL)
filter_by_type(eL)
filter_by_type(spL)