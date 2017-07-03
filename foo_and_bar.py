for number in range(100, 100001):
    factors = []
    divisor = 1
    while (divisor <= number/divisor):
        # if it divides equally, add the pair of factors to the factor/pair list
        if number % divisor == 0:
            factors.append(divisor)
            # note - for perfect squares, this next line means the last two elements of the list will be the same
            factors.append(number/divisor)
        divisor += 1
    # prime numbers will have exactly 2 factors
    if len(factors) == 2:
        print "Foo"
    # perfect squares, the last two elements of the factors list will be the same
    elif factors[len(factors)-1] == factors[len(factors)-2]:
        print "Bar"
    else:
        print "FooBar"

