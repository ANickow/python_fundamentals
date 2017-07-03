# Function from part 1 - commented out to modify for part 2
# def draw_stars(arr):
#     for item in arr:
#         print "*" * item

# Function from part 2 - started with part 1 and modified 
def draw_stars(arr):
    for item in arr:
        if isinstance(item, int):
            print "*" * item
        if isinstance(item, str):
            letter = item[0].lower()
            print letter * len(item)

# Test it out
# Tester list for part 1
# x = [4, 6, 1, 3, 5, 7, 25]
# Tester list for part 2
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)