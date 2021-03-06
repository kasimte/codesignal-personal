"""https://app.codesignal.com/interview-practice/task/rMe9ypPJkXgk3MHhZ

You have a collection of coins, and you know the values of the coins
and the quantity of each type of coin in it. You want to know how many
distinct sums you can make from non-empty groupings of these coins.

Example

For coins = [10, 50, 100] and quantity = [1, 2, 1], the output should
be possibleSums(coins, quantity) = 9.

Here are all the possible sums:

50 = 50;
10 + 50 = 60;
50 + 100 = 150;
10 + 50 + 100 = 160;
50 + 50 = 100;
10 + 50 + 50 = 110;
50 + 50 + 100 = 200;
10 + 50 + 50 + 100 = 210;
10 = 10;
100 = 100;
10 + 100 = 110.

As you can see, there are 9 distinct sums that can be created from
non-empty groupings of your coins.
"""

def possibleSums(values, counts):
    '''
    Fill in code here.
    '''

    # establish set of unique sums
    # start with zero so we have something to iterate over
    sums = {0}

    # iterate over values and counts, zipped
    for v, c in zip(values, counts):
        # replace the set by
        # iterating over the sums already in the set
        # iterating over the different possible sums by the counts of this value
        # adding them to the distinct sums in the set
        temp = {
            sum + add
            for add in range(v, v*c+1, v)
            for sum in sums
            }

        for t in temp:
            sums.add(t)

        # A more efficient way to do this would be to use the bitwise
        # operator |= to set the new elements of the set, which will
        # not completely reset the set.

    return (len(sums) - 1)

def test():
    coins = [10, 50, 100]
    quantity = [1, 2, 1]
    print(possibleSums(coins, quantity)) # 9

    coins = [3, 1, 1]
    quantity = [111, 84, 104]
    print(possibleSums(coins, quantity)) # 521

if __name__ == '__main__':
    test()
