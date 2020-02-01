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
    # establish set {0}
    sums = {0}
    print(sums)
    for value, count in zip(values, counts):        
        # |= is bitwise or operation
        # i.e., var |= value is short for var = var | value
        # https://stackoverflow.com/questions/3929278/what-does-ior-do-in-python

        # i.e., this sets it if it has not been set to the same thing

        # this is setting the whole hash
        sums |= {# existing sum + the choice
                 i + choice
                 # iterate over range of multiples for this value
                 for choice in range(value, value * count + 1, value)
                 # iterate over all existing sums
                 for i in sums}
        print(sums)
    # remove 0 from the set
    return len(sums) - 1

def test():
    coins = [10, 50, 100]
    quantity = [1, 2, 1]
    print(possibleSums(coins, quantity)) # 9
    
    # coins = [3, 1, 1]
    # quantity = [111, 84, 104]
    # print(possibleSums(coins, quantity)) # 521
    
if __name__ == '__main__':
    test()
