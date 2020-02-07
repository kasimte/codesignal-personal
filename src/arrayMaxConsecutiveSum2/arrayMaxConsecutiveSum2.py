# https://app.codesignal.com/interview-practice/task/dQD4TCunke2JQ98rj

# Given an array of integers, find the maximum possible sum you can
# get from one of its contiguous subarrays. The subarray from which
# this sum comes must contain at least 1 element.

# Example

# For inputArray = [-2, 2, 5, -11, 6], the output should be
# arrayMaxConsecutiveSum2(inputArray) = 7.

# The contiguous subarray that gives the maximum possible sum is [2,
# 5], with a sum of 7.

def arrayMaxConsecutiveSum2(inputArray):
    # brute force, iterate all possibilities, not fast enough
    # hash = set()
    # length = len(inputArray)
    # for n in range(1, length + 1):
    #     for i in range(0, length - n + 1):
    #         subarray = inputArray[i:i+n]
    #         s = sum(subarray)
    #         hash.add(s)
    # return max(hash)

    # hints:
    
    # Make an array of prefix sums.

    # In O(inputArray.length) time, you can construct the prefix sum
    # array prefix, with inputArray + 1 elements. The first element
    # should be set to zero, and the sum of the all the elements up to
    # and including i are in prefix[i+1]. The sum of the elements from
    # i to j will be stored in prefix[j+1] - prefix[i].

    # Keep track of the minimum prefix sum you have seen so far in a
    # separate array (i.e. min[i] would be the minimum prefix sum you
    # get from the first i elements). By passing through the list
    # once, you can make min[i] an O(inputArray.length) operation. You
    # are interested in the maximum of prefix[i] and min[i].

    # optimized with prefix sums

    if max(inputArray) <= 0:
        return max(inputArray)
    
    prefix_sums = [0]

    for i in range(len(inputArray)):
        value = prefix_sums[i] + inputArray[i]
        prefix_sums.append(value)

    i = j = 0

    for k in range(len(prefix_sums)):
        if prefix_sums[k] >= i:
            i = prefix_sums[k]
            j = k

    return i - min(prefix_sums[0:j])

if __name__ == '__main__':
    print(arrayMaxConsecutiveSum2([-2, 2, 5, -11, 6]))
    print(arrayMaxConsecutiveSum2([-3, -2, -1, -4]))
    print(arrayMaxConsecutiveSum2([-3, 2, 1, -4]))
    print(arrayMaxConsecutiveSum2([1, -2, 3, -4, 5, -3, 2, 2, 2]))
    print(arrayMaxConsecutiveSum2([11, -2, 1, -4, 5, -3, 2, 2, 2]))
    print(arrayMaxConsecutiveSum2([89, 96, 60, 10, 24, 30, 72, 40, 74, 49, 38, 87, 55, 46, 44, 14, 49, 88, 93, 11]))
