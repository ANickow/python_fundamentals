import random
def coin_tosses(rep):
    heads, tails = 0, 0
    for flip in range (1, rep+1):
        if round(random.random()) == 0:
            toss = 'head'
            heads += 1
        else:
            toss = 'tail'
            tails += 1
        print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(flip, toss, heads, tails)
    print "Ending the program, thank you!"


# Test the function
coin_tosses(5000)