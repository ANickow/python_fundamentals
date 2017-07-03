def checkerboard():
    for row in range(0, 8):
        if row % 2 == 0:
            print "* " * 4
        else:
            print " *" * 4

checkerboard()